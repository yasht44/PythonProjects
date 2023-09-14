import os

def list_files_in_directory(path=None):
    if path is None:
        path = os.getcwd()  # Default to the current working directory if path is not provided

    file_dict = {}

    def list_files_recursive(directory):
        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_info = {
                    "size_bytes": os.path.getsize(file_path),
                    "modification_time": os.path.getmtime(file_path),
                }
                file_dict[file_path] = file_info

    list_files_recursive(path)

    return file_dict

if __name__ == "__main__":
    # Prompt the user for the directory path
    custom_path = input("Enter the directory path to analyze (leave blank for current directory): ").strip()

    if custom_path == "":
        custom_path = os.getcwd()  # Use current directory if input is blank

    # Call the function to list files and store the result in a variable
    files_info = list_files_in_directory(custom_path)

    if files_info:
        # Print the dictionary of dictionaries
        for file_path, file_info in files_info.items():
            print("File:", file_path)
            for key, value in file_info.items():
                print(key + ":", value)
    else:
        print("No files found in the specified directoryy.")

    