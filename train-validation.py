import os, os.path
import random
import subprocess

def random_pick(train_images, num_images, train_size):
    for i in range(int(train_size)):
        numb = random.randrange(num_images)

        while numb in train_images:
            numb = random.randrange(num_images)   
        
        train_images.append(numb)


def main():
    images_dir = input("Enter the images directory:\n>") 
    labels_dir = input("Enter the images directory:\n>")
    num_images = len([name for name in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, name))])
    train_size = float(input("Enter in % the sample size for training:\n>"))/100 * num_images
    train_images = []

    train_dir = images_dir + "/train"
    validation_dir = images_dir + "/validate"

    if not (os.path.isdir(train_dir)):
        subprocess.run(["mkdir",train_dir])
        subprocess.run(["mkdir",train_dir + "/images"])
        subprocess.run(["mkdir",train_dir + "/labels"])
    if not (os.path.isdir(validation_dir)):
        subprocess.run(["mkdir",validation_dir])
        subprocess.run(["mkdir",validation_dir + "/images"])
        subprocess.run(["mkdir",validation_dir + "/labels"])

    random_pick(train_images,num_images, train_size)
    
    for i in range(1, num_images+1):
        img_name = str(i) + ".jpg"
        label_name = str(i) + ".txt"
        
        if i in train_images:
            subprocess.run(["mv", images_dir + "/" + img_name, train_dir + "/images" ])
            subprocess.run(["mv", labels_dir + "/" + label_name, train_dir + "/labels" ])
        else:
            subprocess.run(["mv", images_dir + "/" + img_name, validation_dir + "/images" ])
            subprocess.run(["mv", labels_dir + "/" + label_name, validation_dir + "/labels" ])
            
        


if __name__ == "__main__":
    main()