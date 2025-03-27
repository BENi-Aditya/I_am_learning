import rawpy
import imageio
import os

def convert_cr2_to_jpg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file in os.listdir(input_folder):
        if file.lower().endswith(".cr2"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace(".cr2", ".jpg"))
            
            with rawpy.imread(input_path) as raw:
                rgb_image = raw.postprocess()
                imageio.imwrite(output_path, rgb_image, quality=95)
            
            print(f"Converted: {file} -> {output_path}")

# Example usage
input_folder = "/Users/tripathd/Downloads/test_input"  # Change this to your folder containing CR2 images
output_folder = "/Users/tripathd/Downloads/test_output"  # Change this to your desired output folder
convert_cr2_to_jpg(input_folder, output_folder)
