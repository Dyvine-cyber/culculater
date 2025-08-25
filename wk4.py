import os
filename=input("please enter you filename:")

def process_file():
    try:
        
        input_filename = input("Enter the input filename: ")
        
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")
        
        if not os.access(input_filename, os.R_OK):
            raise PermissionError(f"No read permission for '{input_filename}'.")
        
        output_filename = f"modified_{input_filename}"
        
        if os.path.exists(output_filename):
            overwrite = input(f"'{output_filename}' already exists. Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                print("Operation cancelled.")
                return
        
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()
            
            modified_content = content.upper()
            
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(modified_content)
                
        print(f"Successfully created '{output_filename}' with modified content.")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except UnicodeDecodeError:
        print("Error: Unable to read the file. It may not be a text file or may have encoding issues.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    process_file()