from PIL import Image 
 
  


inp = "C:\\Users\\Kunal\\Documents\\GitHub\\Redshelf_webscraper\\images2\\page_"
out = 'C:\\Users\\Kunal\\Documents\\GitHub\\Redshelf_webscraper\\images2_crop\\page_'
numPages = 389
for i in range(389):
    
    img = Image.open(inp + str(i+1) + ".png")
 
    #constants found in a photo editing program
    left = 115
    right = 1340
    top = 0
    bottom = 1584
    
    
    img_res = img.crop((left, top, right, bottom)) 
    img_res.save(out + str(i+1) + ".png")
 
# img_res.show() 