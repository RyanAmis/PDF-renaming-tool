import os
import shutil

PATH = "//egnytedrive/diig/Private/portfolio/PDF Lease renaming tool file/Leases to process"
COMPLETE_PATH = "//egnytedrive/diig/Private/portfolio/PDF Lease renaming tool file/Completed Leases"
ERRORED_PATH = "//egnytedrive/diig/Private/portfolio/PDF Lease renaming tool file/Errored Leases"

for file in os.listdir(PATH):
    try:
        old_name = f'{file}'
        new_name = file.split(" ")[5]
        os.rename(f"{PATH}/{old_name}", f"{PATH}/{new_name}")
        sub_folder = f'{new_name}'
        os.makedirs(f'{COMPLETE_PATH}/{sub_folder}')
        shutil.move(f'{PATH}/{sub_folder}', f'{COMPLETE_PATH}/{sub_folder}')
        input()
        print(f"{old_name} is now complete ")
    except:
    # shutil.move(f'{PATH}/{sub_folder}', f'{COMPLETE_PATH}/{sub_folder}')
    pass









# Identify PDF files inserted into a lease folder on the Z drive
# Identify title number within name and strip everything else
# Save renamed document and please it in completed folder
# Any errored files are to go into an errored folder
