from PIL import Image, ImageOps

with Image.open("/home/tensai/Downloads/Ado's best adobum cover.webp") as im:
    im=ImageOps.grayscale(im)
    im=im.resize((30,30))
    ascii="#$%*(/=+_~-`,."
    arr=[]
    for i in range(30):
        for j in range(30):
            intensity=im.getpixel((i,j))
            assert isinstance(intensity, int)
            index=intensity*13//255
            arr.append(ascii[index])
        arr.append("\n")
    image="".join(arr)
print(image)
