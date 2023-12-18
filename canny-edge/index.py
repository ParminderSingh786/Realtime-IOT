from skimage import io, color, feature

# Read the input image
input_image_path = 'download.jpeg'
output_image_path = 'output.jpg'

# Load the image
input_image = io.imread(input_image_path)

# Convert the image to grayscale
gray_image = color.rgb2gray(input_image)

# Apply Canny edge detection
edges = feature.canny(gray_image, sigma=2)

# Save the output image with edges
io.imsave(output_image_path, (edges * 255).astype('uint8'))

print(f'Canny edge detection completed. Output saved to {output_image_path}')