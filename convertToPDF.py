from PIL import Image

images = []

out = "Textbook.pdf"
inp = 'C:\\Users\\Kunal\\Documents\\GitHub\\Redshelf_webscraper\\images_crop\\page_'

im1 = Image.open(inp + str(1) + ".png").convert("RGB")

numPages = 562
for i in range(1, numPages):
    img = Image.open(inp + str(i+1) + ".png")
    img = img.convert("RGB")
    images.append(img)

im1.save(out, resolution = 110.0, quality=110, save_all = True, append_images = images)