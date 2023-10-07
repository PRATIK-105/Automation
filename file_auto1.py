from sys import * #used for command line arguments
import os


# def add(no1 , no2):
#     return no1 + no2

def directory_travel(Dirname):
    print("We are going to scan the directiory",Dirname)

    for foldername , subfoldername , filename in os.walk(Dirname):
        for fname in filename :
            print(fname)

def main():
    print("-----------------Automation Script--------------")
    print("Automation script name : ",argv[0])

    if(len(argv) != 2):
        print("Invalid no of arguments..")
        exit()

    
    if(argv[1] == "-h" or argv[1]== "-H"):    #flag for display help

        print("this automation script is used to perform file automations")
        exit()

    elif(argv[1] == "-u" or argv[1] == "-U"):    #flag for display usage of script

        print("usage : name_of_script First_argument ")
        print("Example : demo.py folder_name")
        exit()

    else:
        directory_travel(argv[1])
        exit()


if __name__ == "__main__":
    main()