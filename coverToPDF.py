from PIL import Image

images = []

out = "WorkBookTable.pdf"
inp = 'C:\\Users\\Kunal\\Documents\\GitHub\\Redshelf_webscraper\\images_crop\\page_'

im1 = Image.open("Workbook_Table.png").convert("RGB")

numPages = 1
for i in range(1, numPages):
    img = Image.open(inp + str(i) + ".png")
    img = img.convert("RGB")
    images.append(img)

im1.save(out, resolution = 110.0, quality=110, save_all = True, append_images = images)