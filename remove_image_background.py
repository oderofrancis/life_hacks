from rembg import remove
from PIL import Image

output_path = 'output.png'

# Load image

img = Image.open('rhino.jpg')

# Remove background

output = remove(img)

# Save image
output.save(output_path)