import os



def main():
    
    path = "c:\\users\\wiki\\downloads\\"
    directories = os.listdir(path)
    
    for ff in directories:
        
        if os.path.isdir(path+ff):
            print(ff, "is a directory")
        
        elif os.path.isfile(path+ff):
            print("executable code")
        
        else:
            print(ff, "is a file")       
          
        print()
if __name__ == "__main__":
    main()
