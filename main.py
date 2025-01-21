import pyfiglet
import os
from datetime import datetime
from rembg import remove
from PIL import Image

def generate_ascii_art(name):
    # Generate ASCII art from the given name
    ascii_art = pyfiglet.figlet_format(name)
    return ascii_art

def remove_background(input_path):
    # Remove background from the image
    output_folder = 'output'
    os.makedirs(output_folder, exist_ok=True)
    
    # Get the original file name without the extension
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_folder, f"{base_name}_{current_time}.png")
    
    with open(input_path, 'rb') as input_file:
        input_image = Image.open(input_file)
        output_image = remove(input_image)
        output_image.save(output_path)
    
    return output_path

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Create ASCII Art")
    print("2. Remove Background from Image")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        name = input("Enter your name: ")
        art = generate_ascii_art(name)
        print(art)
    elif choice == '2':
        input_path = input("Enter the file path of the image: ")
        output_path = remove_background(input_path)
        print(f"Background removed. Output saved to: {output_path}")
    else:
        print("Invalid choice. Please enter 1 or 2.")
