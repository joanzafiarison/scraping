from bs4 import BeautifulSoup 
import requests
import re 
import spacy
from spacy import displacy
import fr_core_news_sm 
from collections import Counter


nlp = fr_core_news_sm.load()
url_protected = "https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news"
url_scrapable = "https://preply.com/fr/blog/mots-et-phrases-en-chinois-pour-debutants/"
def url_to_string(url):
    res = requests.get(url)
    html = res.text 
    soup = BeautifulSoup(html,features="lxml")
    for script in soup(["script","style", "aside"]):
        script.extract()
    return " ".join(re.split(r'[\n\t]+',soup.get_text()))

ny_bb = url_to_string(url_scrapable)
article = nlp(ny_bb)
# number of entities print(len(article.ents))
labels = [x.label_ for x in article.ents]
items = [x.text for x in article.ents]
sentences = [x for x in article.sents]
print(Counter(labels))
#print(Counter(items).most_common(10))
#displacy.render(nlp(str(sentences[20])),jupyter=True,style='ent')


