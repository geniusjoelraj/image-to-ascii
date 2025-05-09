from PIL import Image, ImageOps

image_path="/home/tensai/Pictures/ASCII_logo.png"
quality=100
kanji="鬱森冊花代日三二一丶 "
ascii="#$%*(/=+_~-`,."
ascii_inverse=ascii[::-1]
kanji_inverse=kanji[::-1]
chars=ascii

def resize_img(img):
    width, height=img.size
    aspect_ratio=width/height
    height=quality
    width=int(height*aspect_ratio)
    return img.resize((width, height))

with Image.open(image_path) as im:
    im=im.rotate(90,expand=True)
    im=im.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    im=ImageOps.grayscale(im)
    im=resize_img(im)
    arr=[]
    w,h=im.size
    for i in range(w):
        for j in range(h):
            intensity=im.getpixel((i,j))
            assert isinstance(intensity, int)
            index=intensity*(len(chars)-1)//255
            if chars[index]==" ":
                arr.append(" ")
            arr.append(chars[index]+" ")
        arr.append("\n")
    image="".join(arr)
print(image)

