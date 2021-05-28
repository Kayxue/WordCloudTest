import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import jieba
import numpy as np

text = "你好嗎？我很好的。"


jieba.set_dictionary('dict.txt.big')
wordlist = jieba.cut(text)
words = " ".join(wordlist)

mask = np.array(Image.open('pic.png'))  

font = 'SourceHanSansTW-Regular.otf'

my_wordcloud = WordCloud(background_color='white',
                         mask=mask, font_path=font).generate(words)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file('word_cloud.png')
