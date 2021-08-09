import subprocess

def add_counter(labels,i):
    labels[i] = labels[i] + 1

def count_labels(dataset_path, first_folder, last_folder):

    output_file_path = dataset_path + "/labels_count.csv"
    output_file = open(output_file_path, 'w')
    output_file.write("\"folder\",\"vessel\",\"plant\",\"pole\",\"bouy\",\"stone\",\"sand bank\",\"barrier\",\"twig\",\"obstacle\"\n")
   
    labels = [0,0,0,0,0,0,0,0,0]
    total = [0,0,0,0,0,0,0,0,0]
    
    labels_map = {
        "vessel": 0,
        "plant": 1,
        "pole": 2,
        "bouy": 3,
        "stone": 4,
        "sand bank": 5, 
        "barrier": 6,
        "twig": 7,
        "obstacle": 8 
    }
    
    for i in range(first_folder, last_folder + 1):
        outter_folder_name = str(i).zfill(3)
        input_file_path = dataset_path + "/" + outter_folder_name + "/" + outter_folder_name + ".csv"
        input_file = open(input_file_path, 'r')
        lines = input_file.readlines()

        for line in lines[1:]:
            args = line.split(",")
            index = labels_map[args[5].replace('\"', "").strip()]
            add_counter(labels,index)

        output_line = outter_folder_name

        for i in range(0,9):
            output_line = output_line + "," + str(labels[i])
        
        output_line = output_line + "\n"

        total = [total + labels for total, labels in zip(total, labels)]
        labels = [0,0,0,0,0,0,0,0,0]

        output_file.write(output_line)


    final_line = "TOTAL"

    for i in range(0,9):
        final_line = final_line + "," + str(total[i])

    output_file.write(final_line)
    output_file.close() 

def main():
    dataset_path = input("Enter the dataset path:\n>")
    print("Plese inform the dataset's portion you want to count the labels from:")
    first_folder = int(input("Enter the number(name) of the first folder\n>"))
    last_folder = int(input("Enter the number(name) of the last folder:\n>"))

    count_labels(dataset_path, first_folder, last_folder)

if __name__ == "__main__":
    main()
