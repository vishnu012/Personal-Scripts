# script to convert simplenote exported .txt files to .md files
# input - exported zip file from simplenote

import argparse
import zipfile
import os
import shutil

current_path = os.path.dirname(os.path.realpath(__file__))
source_path = current_path + '/notes.zip'
destination_path = current_path + '/output'

def txt_to_md(input_dir):
    if not os.path.exists(input_dir):
        print(f"Error: The directory '{input_dir}' does not exist.\n")
        return
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            txt_file = os.path.join(input_dir, filename)
            md_file = os.path.splitext(txt_file)[0] + ".md"
            with open(txt_file, 'r') as txt_f:
                txt_content = txt_f.read()

            with open(md_file, 'w') as md_f:
                md_f.write(txt_content)
            if os.path.exists(txt_file):
                os.remove(txt_file)
            print(f"Converted '{txt_file}' to '{md_file}'")

def extract_zip(zip_file_path, extract_to):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted files from {zip_file_path} to {extract_to}\n")

def del_exisiting_dest_folder(destination):
    try:
        shutil.rmtree(destination)
        print("Existing foler is deleted\n")
    except Exception as e:
        print("Error occured . Detailes : {}\n".format(e))

def cleanup_files_folders(input_dir):
    trash_dir = input_dir + '/trash'
    source_dir = input_dir + '/source'
    if os.path.exists(trash_dir):
        shutil.rmtree(trash_dir)
    if os.path.exists(source_dir):
        shutil.rmtree(source_dir)
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            old_file_path = os.path.join(input_dir, filename)
            new_filename = filename.lstrip('#')  # Remove the '#' character from the filename
            new_file_path = os.path.join(input_dir, new_filename)

            if old_file_path != new_file_path:
                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed '{filename}' to '{new_filename}'.")
                except Exception as e:
                    print(f"Error renaming '{filename}': {str(e)}")
def main():
    parser = argparse.ArgumentParser(description="Extract files from a zip archive.")

    parser.add_argument('--zip_file', '-z', type=str, help="zip file source", default=source_path)

    parser.add_argument('--destination', '-d', type=str, default=destination_path, 
                        help="Destination directory for extracted files (default: current directory).")

    args = parser.parse_args()

    if not os.path.exists(args.zip_file):
        print(f"Error: The file '{args.zip_file}' does not exist.\n")
        return
    if not zipfile.is_zipfile(args.zip_file):
        print(f"Error: The file '{args.zip_file}' is not a valid zip archive.\n")
        return

    del_exisiting_dest_folder(args.destination)
    extract_zip(args.zip_file, args.destination)
    txt_to_md(args.destination)
    cleanup_files_folders(args.destination)

if __name__ == "__main__":
    main()
