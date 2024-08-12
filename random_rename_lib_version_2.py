'''
RANDOM JPG RENAMER CLASS
Version 2.0

new features:
    ask the user the source and destination folders
    create the folder in 2 destinations
    abrogated the low and high folder management
    improvements terminal interface 

Made by Alessandro Silvestri - 2024 <alessandro.silvestri.work@gmail.com>
'''

import os, random
from tkinter import filedialog

class Random_rename():
    def jpg_list_and_num(self):
        '''I define the current jpg list (self.jpg_list) and the number of jpg files (self.num_jpg_list)'''
        # defining len of the jpg list
        self.jpg_list = []
        for i in os.listdir():
            if ".jpg" in i or ".JPG" in i:
                self.jpg_list.append(i)
        # defining len of the jpg list
        self.num_jpg_list = len(self.jpg_list)

    def shuffle(self):
        '''create a list with only random numbers according the number of files'''
        self.random_nums = [i for i in range(self.num_jpg_list)]
        random.shuffle(self.random_nums)

    def rename(self):
        '''rename the jpg files in the directory'''
        self.jpg_list_and_num()
        self.shuffle()
        # actual renaming files loop 
        for i in range(self.num_jpg_list):
            file_name = self.jpg_list[i]
            new_file_name = f"{self.random_nums[i]}.jpg"
            os.rename(file_name, str(new_file_name))
    
    def rename_a(self):
        '''adding an "a" in front of the file name'''
        self.jpg_list_and_num() # redefine: "self.jpg_list", "self.num_jpg_list"      
        for i in self.jpg_list:
            file_name = i
            new_file_name = f"a{i}"
            os.rename(file_name, str(new_file_name))
    
    def last_item(self):
        return sorted(os.listdir(), key=lambda x: os.path.getmtime(x), reverse=True)[0]

    def rename_combined(self):
        self.rename_a()
        self.rename()


rename = Random_rename()


####### User terminal interface ########################################
last_directory = "" # just the name
last_directory_path = "" # path+name
# ask the paths
print("Open the source directory")
source_directory = filedialog.askdirectory()
# source_directory = "C:/Users/alexs/Documents/vanity studio/2023/October/28"
print("Open the destination directory")
destination_directory = filedialog.askdirectory()
# destination_directory = "C:/Users/alexs/Desktop/sculpt_files"
# change directory
os.chdir(destination_directory)


while True:
    print(f'''
    type ... - Creating a folder
    S        - Shuffle the folder: {last_directory}
    O        - Open directory
    Q        - Quit
    ''')
    choice = input('-> ').lower()
    last_directory_path = f"{destination_directory}/{last_directory}"
    if choice == 's':
        os.chdir(last_directory_path)
        rename.rename_combined()
    elif choice == 'o':
        # choose the folder you want rename
        choose_path = filedialog.askdirectory()
        os.chdir(choose_path)
        rename.rename_combined()
    elif choice == 'q':
        quit()
    else:
        choice = choice.title()
        # create the folder in 2 destinations
        os.mkdir(source_directory + "/" + choice)
        os.mkdir(destination_directory + "/" + choice)
        last_directory = choice
