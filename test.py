from wordcloud import *
import matplotlib.pyplot as plt
import jieba
import numpy as np
from PIL import Image

text = open("test2.txt").read()

wordlist_after_jieba = jieba.cut(text)  # cut the sentences
space_join_text = " ".join(wordlist_after_jieba)
print(space_join_text)

image = np.array(Image.open("image3.jpg"))  # get the image
image_colors = ImageColorGenerator(image)  # create coloring from image

font = r'C:\Windows\Fonts\msyh.ttc'
# font = r'C:\Windows\Fonts\simfang.ttf'
# wc = WordCloud(background_color="white", font_path=font, width=1000, height=860,
#                max_font_size=120, collocations=False)
wc = WordCloud(background_color="white", font_path=font, max_words=2000, max_font_size=80, mask=image, collocations=False)
wc.generate(space_join_text)

plt.imshow(wc)
# plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")

wc.to_file('wordcloud.png')  # 把词云保存下来
