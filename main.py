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
        dest_dir = os.path.expanduser(input(f"❔ Please specify destination directoy for backup archives >>> "))

        if not os.path.isdir(dest_dir):
            try:
                print(f"❗ Directory \"{dest_dir}\" does not exist. Creating...")
                os.makedirs(dest_dir,exist_ok=True)
                print(f"✅ Script will backup \"{dir_to_backup}\" directory.\n✅ Archives will be saved in: \"{dest_dir}\".")
                break
            except Exception as e:
                print(f"❗ Could not create directory.\nERROR:\n{e}")
        else:
            print(f"✅ Script will backup \"{dir_to_backup}\" directory.\n✅ Archives will be saved in: \"{dest_dir}\".")
            break

    while True: 
        algos = {"xz":False,"gzip":False,"bzip2":False,"None":False}
        algo = input("\nThis script uses 'tar' to archive specified directories. Please type the algorithm to use for compression.\nSupported algorithms are ('xz','gzip','bzip2','None) >>> ")
        if not algo in algos:
            print("Typed compression algorithm not available. Please type one of these: ('xz','gzip','bzip2','None')")
        else:
            algos[algo] = True
            break

    return dir_to_backup,dest_dir,algos

def compress(src,dest,alg):
    date =  datetime.datetime.now().strftime("%d-%m-%Y-%H:%M")

    for i in alg:
        if alg.get(i)== True:
            compression = i
            break

    algorithms = {
        'xz': {"ext":".tar.xz", "options":["-cJf"]},
        'gzip': {"ext":".tar.gzip", "options":["-czf"]},
        'bzip2': {"ext":".tar.bzip2", "options":["-cjf"]},
        'None': {"ext":".tar", "options":["-cf"]},
    }

    compress_config = algorithms.get(compression)
    archive_name = dest+"/backup" + "--" + date + compress_config["ext"]
    src_target = os.path.basename(src)
    src_dir = os.path.dirname(src)


    # print(archive_name)
    cmd = ['tar'] + compress_config.get("options") + [archive_name,"-C", src_dir , src_target]

    print(cmd)

    subprocess.run(cmd)



    

    
dir_to_backup,dest_dir,algos =  user_input()
compress(dir_to_backup,dest_dir,algos)