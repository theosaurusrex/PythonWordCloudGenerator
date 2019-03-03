import wikipedia
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os
from PIL import Image
import numpy as np
currdir = os.path.dirname(__file__)

# class wordcloudGen:

def get_wiki(query):

    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content

def create_wordcloud(text):
    mask = np.array(Image.open(os.path.join(currdir, "thales-matt-bjj-cloud.png")))

    stopwords = set(STOPWORDS)

    wc = WordCloud(background_color="white",
        mask=mask,
        max_words=200,
        stopwords=stopwords)
        
    wc.generate(text)

    wc.to_file(os.path.join(currdir,"thales-matt-bjj-wc.png"))

create_wordcloud(get_wiki("brazilian jiu jitsu"))