from PIL import Image, ImageOps

quality=20
kanji="鬱森冊花代日三二一丶"
ascii="#$%*(/=+_~-`,."
kanji_inverse="丶一二三日代花冊森鬱"
chars=kanji_inverse
with Image.open("/home/tensai/Pictures/archlinux-icon.png") as im:
    im=ImageOps.grayscale(im)
    im=im.resize((quality,quality))
    im=im.rotate(270)

    arr=[]
    for i in range(quality-1,0,-1):
        for j in range(quality):
            intensity=im.getpixel((i,j))
            assert isinstance(intensity, int)
            index=intensity*(len(chars)-1)//255
            arr.append(chars[index]+"")
        arr.append("\n")
    image="".join(arr)
print(image)
