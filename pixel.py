from PIL import Image

def pixelate_image(image_path, pixel_size, output_path):
    # Open the image file
    image = Image.open(image_path)
    image = image.convert('RGB')  # Ensure the image is in RGB mode

    # Resize the image to a smaller size
    small_image = image.resize(
        (image.width // pixel_size, image.height // pixel_size),
        resample=Image.NEAREST
    )

    # Resize the image back to its original size
    pixelated_image = small_image.resize(
        (image.width, image.height),
        Image.NEAREST
    )

    # Save the pixelated image as TIFF
    pixelated_image.save(output_path, format='TIFF')
    print(f"Pixelated image saved to {output_path}")

if __name__ == "__main__":
    input_image_path = "Yours_here"  # Path to your input image
    output_image_path = "Name_here"  # Path to save the pixelated image
    pixel_size = 100  # Size of the pixels

    pixelate_image(input_image_path, pixel_size, output_image_path)
