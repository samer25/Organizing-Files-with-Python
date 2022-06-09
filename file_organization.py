import os
import glob
import pickle
import shutil

extensions = {
    "jpg": "images",
    "png": "images",
    "ico": "images",
    "gif": "images",
    "svg": "images",
    "sql": "sql",
    "exe": "programs",
    "msi": "programs",
    "pdf": "pdf",
    "xlsx": "excel",
    "csv": "excel",
    "rar": "archive",
    "zip": "archive",
    "gz": "archive",
    "tar": "archive",
    "docx": "word",
    "torrent": "torrent",
    "txt": "text",
    "ipynb": "python",
    "pptx": "powerpoint",
    "ppt": "powerpoint",
    "mp3": "audio",
    "wav": "audio",
    "mp4": "video",
    "m3u8": "video",
    "webm": "video",
    "ts": "video",
    "json": "json",
    "css": "web",
    "js": "web",
    "html": "web",
    "apk": "apk",
    "sqlite3": "sqlite3",

}


# Geting the data form the file or `returning None`
def get_dict_extensions_file_data():
    loaded_dict = None
    try:
        with open('saved_extensions.pkl', 'rb') as f:
            loaded_dict = pickle.load(f)
        return loaded_dict
    except FileNotFoundError:
        return loaded_dict


# updating data or creating a file if not exists
def update_dict_extensions_file_data(dict_extensions):
    try:
        with open('saved_extensions.pkl', 'wb') as f:
            pickle.dump(dict_extensions, f)
    except FileNotFoundError:
        raise FileNotFoundError


def file_organization(path, file_extensions):
    if not os.path.exists(path):
        print("Folder not found")
        path = input("Ender full path, that you want to be organized\n")
        file_organization(path, file_extensions)
    else:
        for extension, folder_name in file_extensions.items():
            files = glob.glob(os.path.join(path, f"*.{extension}"))
            print(f"[*] {len(files)} files was found with {extension} extension")
            if not os.path.isdir(os.path.join(path, folder_name)) and files:
                # create the folder if it does not exist.
                print(f"[+] Folder with {folder_name} name was created")
                os.mkdir(os.path.join(path, folder_name))
            for file in files:
                # for each file in that extension, move it to the corresponding folder
                basename = os.path.basename(file)
                dst = os.path.join(path, folder_name, basename)

                print(f"[*] Moving {file} to {dst}")
                shutil.move(file, dst)


# first we call the `update_dict_extensions` to create a file with default data from dictionary `extensions`.
# checking if file exists, if not, passing dictionary extensions to create one
if get_dict_extensions_file_data() is not None:
    update_dict_extensions_file_data(get_dict_extensions_file_data())
else:
    update_dict_extensions_file_data(extensions)

# printing data from the file
print("All extensions with folder names\n")
for key, value in get_dict_extensions_file_data().items():
    print("Extension: " + key + " => Folder: " + value)

print(
    "If you don't see an extension that you want to organize add a custom one, or you can change the folder name of the extension that exists")

custom = input("Do you like to add custom extension or change folder name? y/n\n")

extensions = get_dict_extensions_file_data()
while True:
    if custom.lower() == 'y':
        extensions.update({input("Enter an extension without a dot\n"): input("Enter a name for the folder\n")})
        update_dict_extensions_file_data(extensions)
    if custom.lower() == 'n':
        break

    custom = input("Do you want to add more? y/n")

path = input("Ender full path, that you want to be organized\n")  # r"/home/sammy-code/Downloads"
file_organization(path, get_dict_extensions_file_data())
