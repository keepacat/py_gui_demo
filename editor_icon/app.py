from PIL import Image
from PIL import ImageEnhance

 
#原始图像
image = Image.open("logo2.png")  # 读取照片

image = image.convert("RGBA")    # 转换格式，确保像素包含alpha通道
width, height = image.size     # 长度和宽度
for i in range(0,width):     # 遍历所有长度的点
    for j in range(0,height):       # 遍历所有宽度的点
        data = image.getpixel((i,j))  # 获取一个像素
        if (data.count(255) == 4):  # RGBA都是255，改成透明色
            image.putpixel((i,j),(255,255,255,0))

image.save("logo3.png")  # 保存图片
image = Image.open('logo3.png')
 
#亮度增强
enh_bri = ImageEnhance.Brightness(image)
brightness = 1.5
image_brightened = enh_bri.enhance(brightness)
 
#色度增强
enh_col = ImageEnhance.Color(image)
color = 1.5
image_colored = enh_col.enhance(color)
 
#对比度增强
enh_con = ImageEnhance.Contrast(image)
contrast = 1.5
image_contrasted = enh_con.enhance(contrast)
 
#锐度增强
enh_sha = ImageEnhance.Sharpness(image)
sharpness = 3.0
image_sharped = enh_sha.enhance(sharpness)
image_sharped.save("logo4.png")  # 保存图片


image = Image.open("logo4.png")
image.save("logo.ico")