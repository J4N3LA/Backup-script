import subprocess
import os
import datetime
def user_input():
    while True:
        dir_to_backup = os.path.expanduser(input("❔ Please enter directory path to backup >>> "))

        if not os.path.isdir(dir_to_backup):
            print(f"❗ Directory \"{dir_to_backup}\" does not exist. Please enter correct direcotory  path.")
        else: break


    while True:
        dest_dir = os.path.expanduser(input(f"❔ Please specify destionation directoy for backup archives >>> "))

        if not os.path.isdir(dest_dir):
            print(f"❗ Directory \"{dest_dir}\" does not exist. Please enter correct destination directory.")
        else:
            print(f"✅ Script will backup \"{dir_to_backup}\" directory.\n✅ Archives will be saved in: \"{dest_dir}\".")
            break

    while True: 
        algos = {"zip":False,"gzip":False,"bzip2":False}
        algo = input("\nThis script uses 'tar' to archive specified directories. Please type the algorithm to use for compression.\nSupported algorithms are ('zip','gzip','bzip2') >>> ")
        if not algo in algos:
            print("Typed compression algorithm not available. Please type one of these: ('zip','gzip','bzip2')")
        else:
            algos[algo] = True
            break

    return dir_to_backup,dest_dir,algo

def compress():
    date =  datetime.datetime.now().strftime("%d/%m/%Y-%H:%M")

    print(date)

compress()