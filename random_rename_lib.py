'''
RANDOM JPG RENAMER CLASS
It is connected with_random_rename.py
Made by Alessandro Silvestri - 2023 <alessandro.silvestri.work@gmail.com>
'''

import os, random

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
    
    def rename_combined(self):
        self.rename_a()
        self.rename()

