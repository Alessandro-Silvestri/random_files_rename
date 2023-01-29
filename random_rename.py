import os, random, time

class Random_rename():
    def __init__(self):
        pass

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
            print(file_name, new_file_name)
            os.rename(file_name, str(new_file_name))
 
    def user_interface(self):
        self.rename()
        usr = input('Do you want to shuffle the files again?: (y/n) > ')

################################ UNTIL HERE   ################################
        if usr == 'y':
            self.jpg_list.clear()
            self.jpg_list_and_num() # redefine: "self.jpg_list", "self.num_jpg_list"
            
            for i in range(self.num_jpg_list):
                file_name = self.jpg_list[i]
                new_file_name = f"a{i}.jpg"
                print(file_name, new_file_name)
                os.rename(file_name, str(new_file_name))
                # # time.sleep(1)
                # self.rename()
############################################################################

        else:
            print('Bye!')
            quit()
    

ren_obj = Random_rename()
ren_obj.user_interface()
ren_obj.user_interface()
ren_obj.user_interface()


