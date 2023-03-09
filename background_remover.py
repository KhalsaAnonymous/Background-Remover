from rembg import remove
import os

input_dir = "images"  # directory containing input images
output_dir = "output"  # directory to store output images

# create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# get list of files in input directory
files = os.listdir(input_dir)

print(f"Total number of images found: {len(files)}\n")

# loop through each file in the input directory and process it
for i, filename in enumerate(files):
    input_path = os.path.join(input_dir, filename)  # full path of input file
    output_path = os.path.join(output_dir, filename)  # full path of output file

    # read input file
    with open(input_path, "rb") as f:
        input_data = f.read()

    # process input image to remove background
    output_data = remove(input_data)

    # save output image
    with open(output_path, "wb") as f:
        f.write(output_data)

    # print progress
    print(f"Finished processing image {i+1}/{len(files)}: {filename}\n")

print("All images have been processed!")
