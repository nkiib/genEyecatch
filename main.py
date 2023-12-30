from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap

def main():
    baseImage = Image.open("baseImageHDcopy.png")

    dr = ImageDraw.Draw(baseImage)

    headline_1 = "Test1"
    headline_2 = "Test2"
    headline_3 = "Test3"

    fontFile = "NotoSansJP-ExtraBold.ttf" # フォントファイル
    fontSize = 75

    fnt = ImageFont.truetype(fontFile , fontSize)


    whidth, hight = baseImage.size                 # 画像の幅と高さ
    textColor = (0, 0, 0, 255)            # 文字の色

    wrap_list = textwrap.wrap(headline_1, 16)
    dr.text((30, 5), headline_1, textColor, font=fnt)
    

    dr.text((30, 170), headline_2, textColor, font=fnt)

    baseImage.save("img_3.png")  

main()