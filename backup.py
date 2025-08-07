#!/usr/bin/python3

import subprocess
import os
import datetime


def user_input():

    while True:
        dir_to_backup = os.path.expanduser(input("❔ Please enter directory path to backup >>> "))

        if not os.path.isdir(dir_to_backup):
            print(f"❗ Directory \"{dir_to_backup}\" does not exist. Please enter correct direcotory  path.")
        else: 
            if os.access(dir_to_backup,os.R_OK):
                break
            else: 
                print(f"❗Your user does not have permission to read this directory\n")


    while True:
        dest_dir = os.path.expanduser(input(f"❔ Please specify destination directoy for backup archives >>> "))

        if not os.path.isdir(dest_dir):
            base_dir = os.path.dirname(dest_dir)
            if os.access(base_dir,os.W_OK):
                print(f"🛈 Directory \"{dest_dir}\" does not exist. Creating...")
                try:
                    os.makedirs(dest_dir,exist_ok=True)
                    print(f"✅ Directory - {dest_dir} has been created.")
                    break
                except Exception as e:
                    print(f"❗ Could not create directory.\nERROR:\n{e}")
            else:
                print(f"❗ You don't have write permission to create '{dest_dir}' in {base_dir}")
        else:
            if os.access(dest_dir,os.W_OK):
                break
            else: 
                print(f"❗ You don't have write permission inside: '{dest_dir}'")


    while True: 
        algos = {"xz","gzip","bzip2","None"}

        algo = input("\n🛈 This script uses 'tar' to archive specified directories. Please type the algorithm to use for compression.\nSupported algorithms are ('xz','gzip','bzip2','None) >>> ")
        if not algo in algos:
            print("Selected compression algorithm not available. Please type one of these: ('xz','gzip','bzip2','None')")
        else: break

    return dir_to_backup,dest_dir,algo

def compress(src,dest,algo):
    date =  datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")

    algorithms = {
        'xz': {"ext":".tar.xz", "options":["-cJf"]},
        'gzip': {"ext":".tar.gz", "options":["-czf"]},
        'bzip2': {"ext":".tar.bz2", "options":["-cjf"]},
        'None': {"ext":".tar", "options":["-cf"]},
    }
    
    src_target,src_dir = os.path.basename(src), os.path.dirname(src)

    compress_config = algorithms.get(algo)

    archive_name = dest+"/"+src_target + "--" + date + compress_config["ext"]

    cmd = ['tar'] + compress_config.get("options") + [archive_name,"-C", src_dir , src_target]

    print(f"🛈 Script will backup \"{dir_to_backup}\" directory.\n🛈 Backup will be saved in: \"{dest_dir}\".")

    try:
        print(f"🛈 Started backup process for {src}...")
        subprocess.run(cmd,check=True)
        print(f"✅ Done\n")
    except Exception as e:
        print(f"❗ ERROR\n{e}")



    

    
dir_to_backup,dest_dir,algo =  user_input()
compress(dir_to_backup,dest_dir,algo)
