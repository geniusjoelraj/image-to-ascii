from PIL import Image, ImageOps

with Image.open("/home/tensai/Downloads/Ado's best adobum cover.webp") as im:
    im=ImageOps.grayscale(im)
    im=im.resize((50,50))
    im=im.rotate(270)
    ascii="#$%*(/=+_~-`,."
    arr=[]
    for i in range(49,0,-1):
        for j in range(50):
            intensity=im.getpixel((i,j))
            assert isinstance(intensity, int)
            index=intensity*13//255
            arr.append(ascii[index]+" ")
        arr.append("\n")
    image="".join(arr)
print(image)
