# coding:utf-8

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import math

class genImage:

    def __init__(self):
        # 吹き出しのサイズ
        self.canbas_height = 130
        self.canbas_width = 1400
        # 吹き出しの余白
        self.margin = 50
        # 文字の挿入位置 
        # 203 , 47
        self.height = 25
        self.width = 47
        # 行間
        self.space_between_lines = 3
        # フォント情報
        self.font_color = (22, 22, 22)
        self.font_path = "NotoSansJP-ExtraBold.ttf"
        # 元画像ファイルのパス
        self.base_image_path = "baseImageHD.png"
        # 挿入するテキスト
        self.base_text ="Intel、最新のCPUアーキテクチャとNPUを備えたMeteor Lakeを発表"
        # 保存する画像ファイルのパス
        self.save_image_path = "img_3.png"


    def run(self):
        self.base_image = Image.open(self.base_image_path).copy()
        self.font_size = self.culculate_text_size(self.base_text)
        self.insert_text = self.split_text(self.base_text, self.font_size)
        self.img = self.insert_split_texts(self.base_image, self.insert_text, self.font_size, self.height)
        self.img.save(self.save_image_path)


    # フォントサイズ計算
    def culculate_text_size(self, text):
        text_length = len(text)
        canbas_area_size = (self.canbas_height - self.margin)*(self.canbas_width - self.margin)
        font_size = math.floor(math.sqrt(canbas_area_size / text_length))

        return font_size

    # 改行する単位でテキストをリスト化
    def split_text(self, text, font_size):
        text_length = len(text)
        text_in_one_line = self.canbas_width // font_size
        text_list = [text[i: i + text_in_one_line] for i in range(0, len(text), text_in_one_line)]

        return text_list

    # 画像の指定位置にテキスト追加
    def add_text_to_image(self, img, text, font_size, height):
        position = (self.width, height)
        font = ImageFont.truetype(self.font_path, font_size)
        draw = ImageDraw.Draw(img)

        draw.text(position, text, self.font_color, font=font)

        return img

    # テキストのリストを画像に挿入
    def insert_split_texts(self, image, split_text, font_size, height):
        for texts in split_text:
            img = self.add_text_to_image(image, texts, font_size, height)
            height += (font_size)

        return img


gi = genImage()
gi.run()
