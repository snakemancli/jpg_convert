import os
from PIL import Image

def convert_webp_to_jpg(folder_path):
    if not os.path.isdir(folder_path):
        raise ValueError(f"The provided path '{folder_path}' is not a valid directory.")
      
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.webp'):
            webp_path = os.path.join(folder_path, filename)
            jpg_path = os.path.splitext(webp_path)[0] + '.jpg'
            
            
            with Image.open(webp_path) as img:
                # Convert the image to RGB mode (required for saving as JPG)
                rgb_img = img.convert('RGB')
                # Save the image as JPG
                rgb_img.save(jpg_path, 'JPEG')
                print(f"Converted {webp_path} to {jpg_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python convert.py <folder_path>")
        sys.exit(1)
    folder_path = sys.argv[1]
    convert_webp_to_jpg(folder_path)
