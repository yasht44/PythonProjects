# PythonProjects
## Description
Python File Analyzer is a simple Python script that allows you to list and analyze files in a directory and its subdirectories. It provides information such as file sizes and modification times.

## Features
- Lists files in a specified directory and its subdirectories.
- Displays file sizes in bytes and modification times.
- User-friendly command-line interface.

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Running the Script
1. Clone this repository to your local machine or download the script file.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the following command:

    ```shell
    python file_analyzer.py
    ```

5. You will be prompted to enter the directory path you want to analyze. You can leave it blank to analyze the current directory.
6. The script will list the files in the specified directory and display their sizes and modification times.

## Example

```shell
Enter the directory path to analyze (leave blank for current directory): /path/to/your/directory
File: /path/to/your/directory/file1.txt
size_bytes: 1024
modification_time: 1631268166.345678

File: /path/to/your/directory/file2.jpg
size_bytes: 2048
modification_time: 1631268220.987654
