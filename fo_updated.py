# file organizer program
# a program that tidies up files in a specified directory by organizing them into folders based on their file type/extensions.


import os
import shutil


def organize_directory(directory, mapping, is_top_level=True):
    #  organize files in the specified directory into subfolders based on their file extensions.
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            # recursively process subdirectories
            organize_directory(file_path, mapping, is_top_level=False)
        # Check if it's a file
        elif os.path.isfile(file_path):
            # Extract file extension and convert to lower case
            # The _ (underscore) is a placeholder variable to hold the name section of the filename (it will be ignored)
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            # Check if the file extension is in the mapping
            if ext in mapping:
                # Folder path for this type of file
                folder_path = os.path.join(directory, mapping[ext])

                # Create folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move file to the appropriate folder
                shutil.move(file_path, folder_path)
            else:
                # If extension is not in the mapping, move to "Others" folder
                others_folder = os.path.join(directory, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, others_folder)
    if is_top_level:
        print("Files have been organized.")


def get_custom_mapping():
    custom_mapping = {}
    while True:
        extension = input(
            "Enter a file extension (e.g., .xyz) or press Enter to finish: ").lower()
        if not extension:
            break
        if not extension.startswith('.'):
            print(
                "Invalid extension format. Please start the extension with a period (e.g., .xyz).")
            continue

        folder = input("Enter the folder name for this extension: ")
        while not folder:
            print("Folder name cannot be empty. Please provide a folder name.")
            folder = input("Enter the folder name for this extension: ")

        custom_mapping[extension] = folder
    return custom_mapping


def main():
    while True:
        directory = input("Enter the path of the directory to organize: ")

        if os.path.isdir(directory):
            mapping = {
                '.pdf': 'PDFs',
                '.jpg': 'Images',
                '.jpeg': 'Images',
                '.png': 'Images',
                '.txt': 'TextFiles',
                '.xml': 'Spreadsheets',
                '.xls': 'Spreadsheets',
                '.doc': 'Documents',
                '.docx': 'Documents',
                '.mp3': 'Music',
                '.mp4': 'Videos'
            }

            print(
                "Do you want to define your own extensions & what folders they go into? (y/n)")
            custom_mappings_option = input().lower()
            if custom_mappings_option == 'y':
                custom_mapping = get_custom_mapping()
                mapping.update(custom_mapping)

            organize_directory(directory, mapping)
            break
        else:
            print("The provided path is not a valid directory. Please try again.")


if __name__ == "__main__":
    main()
