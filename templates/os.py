from PIL import Image,ImageEnhance,ImageFilter
img1=Image.open("ph1.jfif")
max_size=(1500,500)
img1.thumbnail(max_size)
img1.save('ph1.jpg')
#import os
#for item in os.listdir():
    #if item.endswith('.jpg'):
        #img1=Image.open(item)
        #filename,extension=os.path.splitext(item)
#img1.save(f'cab33.jpg')
#img1=Image.open('ccat.jpg')
#enhancer=ImageEnhance.Brightness(img1)
#img2=enhancer.enhance(2)
#img2=img1.filter(ImageFilter.GaussianBlur(radius=4))
#img2.save('xcat.jpg')