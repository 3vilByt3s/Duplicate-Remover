import os

def remove_duplicates(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f"The file {input_file} does not exist.")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"Read {len(lines)} lines from {input_file}.")
        
        unique_lines = set(lines)
        print(f"Found {len(unique_lines)} unique lines.")

        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(unique_lines)
            print(f"Wrote {len(unique_lines)} unique lines to {output_file}.")

    except UnicodeDecodeError as e:
        print(f"An encoding error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = 'list.txt'
    output_file = 'output.txt'
    
    print(f"Removing duplicates from {input_file} and writing to {output_file}...")
    remove_duplicates(input_file, output_file)
    print("Process completed.")
