import os

def isBinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()

    if "binod" in fileContent.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    # Listing the cotents of the folder   
    dir_contents=os.listdir("C:/Users/vb/PycharmProjects/FirstProg/Binod detector")
    nBinod = 0

    # For each text file , detect Binod it them 
    for item in dir_contents :
        if item.endswith("txt") :
            print(f'Detecting Binod in {item}')
            flag = isBinod(item)
            if(flag):
                print(f"Binod found in {item}!!!!!!!!!")
                nBinod += 1
            else:
                print(f"Binod not found in {item}")

    print("Binod Summary : \n")
    print(f"Total files spammed with is {nBinod}")