from PIL import Image

img = Image.open(f"generated_images/{input('What image would you like to upscale?'+chr(10))}.png")
img.resize((1000, 1000), Image.NEAREST).show()
