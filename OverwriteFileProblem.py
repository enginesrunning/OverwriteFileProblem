import os
import shutil
import argparse
 
def copy_file(source_path, destination_path):
    # Check if the source file exists
    if not os.path.exists(source_path):
        print(f"Source file '{source_path}' does not exist.")
        return
 
    # Check if the destination file exists
    if not os.path.exists(destination_path):
        print(f"Destination file '{destination_path}' does not exist.")
        return
 
    # Overwrite destination file
    shutil.copy(source_path, destination_path)
 
    print("File copied successfully.")
 
 
if __name__ == '__main__':
   
    parser = argparse.ArgumentParser(description='Overwrite file.')
    parser.add_argument('-a', '--source', type=str, help='Source path')
 
    parser.add_argument('-b', '--destination', type=str, help='Destination path')
 
    # Parse the command-line arguments
    args = parser.parse_args()
 
    source_path = args.source
    destination_path = args.destination
    copy_file(source_path, destination_path)