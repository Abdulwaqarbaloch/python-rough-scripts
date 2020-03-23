import os



def main():
    
    path = "c:\\users\\wiki\\downloads\\"
    directories = os.listdir(path)
    
    for ff in directories:
        
        if os.path.isdir(path+ff):
            print(ff, "is a directory")
        
        else:
            print(ff, "is a file")       

        print()
if __name__ == "__main__":
    main()