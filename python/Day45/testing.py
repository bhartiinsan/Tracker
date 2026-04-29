# from PIL import Image
# image_path= "C:/Users/BHARTI/Downloads/py.jpg"
# img= Image.open(image_path)
# print(img.size)


from PIL import Image

image_path = "C:/Users/BHARTI/Downloads/py.jpg"

img = Image.open(image_path)
img.show()   #Yeh image open karega
print(img.size)  #Yeh image ke size ko print karega
print(f'Image format: {img.format}')  #Yeh image ke format ko print karega  
print(f'Image mode: {img.mode}')  #Yeh image ke mode ko print karega