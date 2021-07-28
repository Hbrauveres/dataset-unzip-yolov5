
import subprocess

def group_images(dataset_dir, first_folder, last_folder):
    
    counter = 1
    final_images_folder = dataset_dir + "/images"
    final_labels_folder = dataset_dir + "/labels"

    subprocess.run(["mkdir", final_images_folder])
    subprocess.run(["mkdir", final_labels_folder])

    
    for i in range(first_folder, last_folder+1):
        outter_folder_name = str(i).zfill(3)
        images_dir = dataset_dir + "/" + outter_folder_name + "/images"
        labels_dir = dataset_dir + "/" + outter_folder_name + "/labels"

        for j in range(1,121):
            img_name = str(j).zfill(3) + ".jpg"
            img_new_name = str(counter) + ".jpg"
            subprocess.run(["mv", images_dir + "/" + img_name, images_dir + "/" + img_new_name])
            subprocess.run(["mv", images_dir + "/" + img_new_name, final_images_folder])

            label_name = str(j).zfill(3) + ".txt"
            label_new_name = str(counter) + ".txt"
            subprocess.run(["mv", labels_dir + "/" + label_name, labels_dir + "/" + label_new_name])
            subprocess.run(["mv", labels_dir + "/" + label_new_name, final_labels_folder])

            counter += 1


def separate_labels(dataset_dir, first_folder, last_folder):
    
    labels = {
        "vessel"    : "0",
        "plant"     : "1",
        "pole"      : "2",
        "bouy"      : "3",
        "stone"     : "4",
        "sand bank" : "5",
        "barrier"   : "6",
        "twig"      : "7",
        "obstacle"  : "8"
    }

    for i in range(first_folder, last_folder + 1):
        outter_folder_name = str(i).zfill(3)
        in_file_dir = dataset_dir + "/" + outter_folder_name + "/" + outter_folder_name + ".csv"
        in_file = open(in_file_dir, 'r')
        subprocess.run(["mkdir", dataset_dir + "/" + outter_folder_name + "/labels"])

        for j in range(1,121):
            image_name = str(j).zfill(3)
            out_file_dir = dataset_dir + "/" + outter_folder_name + "/labels/" + image_name + ".txt"
            #/home/hbrauveres/Downloads/Dataset/001/labels
            out_file = open(out_file_dir, 'w')

            for line in in_file:
                args = line.split(",")
                if args[0][1:4] == image_name:

                    Xmax = float(args[3])
                    Xmin = float(args[1])
                    Ymax = float(args[4])
                    Ymin = float(args[2])
                    img_width = Xmax - Xmin
                    img_height = Ymax - Ymin
                    img_center_x = img_width/2 + Xmin
                    img_center_y = img_height/2 + Ymin

                    #resizing to fit yolov5 input:
                    img_center_x = (img_center_x/1280)
                    img_center_y = img_center_y/720
                    img_width = img_width/1280
                    img_height = img_height/720

                    yolov5_input = labels[args[5].replace('\"', "").strip()] + " " + str(img_center_x) + " " + str(img_center_y) + " " + str(img_width) + " " + str(img_height) + "\n"

                    out_file.write(yolov5_input)
            
            out_file.close()
            in_file.seek(0)
        
        in_file.close()


def unzip_dataset(dataset_dir, first_folder, last_folder):

    for folder_num in range (first_folder, last_folder +1):
        folder_name = str(folder_num).zfill(3) # 00X, 0X0, X00
        images_zip_dir = dataset_dir + "/" + folder_name # images_zip_dir = /home/~user/.../Dataset/00X
        extracted_dir = images_zip_dir + "/images"  # extracted_dir = /home/~user/.../Dataset/00X/images
        unzip(images_zip_dir + "/images.zip",extracted_dir)


def unzip(file_dir, dest_dir):
    subprocess.run(["unzip", file_dir, "-d", dest_dir])


def main():

    first_folder = 1
    last_folder = 205

    dataset_dir = input("Dataset directory:\n>") #/home/~user/Desktop/Dataset
    unzip_dataset(dataset_dir, first_folder, last_folder)
    separate_labels(dataset_dir, first_folder, last_folder)
    group_images(dataset_dir, first_folder, last_folder)
    

if __name__ == "__main__":
    main()
