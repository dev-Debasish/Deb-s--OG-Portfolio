from PIL import Image
import sys
import os

def remove_white_background(input_path, output_path):
    """
    Remove white background from an image and save it with transparency.
    """
    # Open the image
    img = Image.open(input_path)
    
    # Convert to RGBA if not already
    img = img.convert("RGBA")
    
    # Get the image data
    data = img.getdata()
    
    # Create a new list to hold the modified pixel data
    new_data = []
    
    # Define what we consider "white" (you can adjust these values)
    white_threshold = 240  # Values above this in R, G, B will be considered white
    
    # Process each pixel
    for item in data:
        # If the pixel is white (or close to white), make it transparent
        if item[0] > white_threshold and item[1] > white_threshold and item[2] > white_threshold:
            # Replace white with transparent
            new_data.append((255, 255, 255, 0))
        else:
            # Keep the original pixel
            new_data.append(item)
    
    # Update the image with the new data
    img.putdata(new_data)
    
    # Save the image with transparency
    img.save(output_path, "PNG")
    print(f"Image saved as {output_path}")

if __name__ == "__main__":
    input_file = "bg_og.png"
    output_file = "bg_transparent.png"
    
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        sys.exit(1)
    
    try:
        remove_white_background(input_file, output_file)
        print("Background removal completed successfully!")
    except Exception as e:
        print(f"Error processing image: {e}")
        sys.exit(1)
