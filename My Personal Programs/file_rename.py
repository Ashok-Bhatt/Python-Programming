
import os

folder_path = input("Enter the folder path:").replace("/", "//")

numbering = 'num'
file_pattern = input("Enter the pattern in existing files:")
update_pattern = f"DPP{numbering}.pdf"
file_no = 1

while True:

    flag = False
    for filename in os.listdir(folder_path):
        # print("filename: " + filename + "\npattern: " + file_pattern.replace(numbering, str(file_no)))
        if filename == file_pattern.replace(numbering, str(file_no)):
            old_name = folder_path + "\\" + filename
            new_name = folder_path + "\\" + update_pattern.replace(numbering, str(file_no))
            os.rename(old_name, new_name)
            flag = True
    
    if flag == True:
        file_no = file_no + 1
    else: 
        break