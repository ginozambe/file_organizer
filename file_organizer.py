# file organizer program
# a program that tidies up files in a specified directory by organizing them into folders based on their file type/extensions.

import os
import shutil


def organize_directory(directory):
    # Mapping of file extensions to folder names
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
        # Add more mappings as required
    }

    #  organize files in the specified directory into subfolders based on their file extensions.
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
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

    print("Files have been organized.")


def main():
    # Get directory input from user
    directory = input("Enter the path of the directory to organize: ")

    # Check if the directory is valid
    if os.path.isdir(directory):
        organize_directory(directory)
    else:
        print("The provided path is not a valid directory.")


if __name__ == "__main__":
    main()
