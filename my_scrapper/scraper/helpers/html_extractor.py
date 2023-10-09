import re
import nltk 
from nltk.tokenize import word_tokenize 
from nltk.tag import pos_tag
#https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da

#IOB Tag 
from nltk.chunk import conlltags2tree, tree2conlltags 
from pprint import pprint

#spacy 
import spacy
from spacy import displacy
from collections import Counter 
import en_core_web_sm 
nlp = en_core_web_sm.load()



p = re.compile('[a-z]+')
date_regex = re.compile('[0-9]{2}/[0-9]{2}/[0-9]+')
ex_text = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

file_text = open("freework.txt","r")
file_html = open("freework.html","r")

file_text_lines = file_text.readlines()
#file_html_lines =  file_html.readlines()

#Parse function 

def get_postags(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

def get_noun_phrase_pattern (sent) :
    pt_noun_phrase = 'NP: {<DT>?<JJ>*<NN>}'
    cp = nltk.RegexpParser(pt_noun_phrase)
    cs = cp.parse(sent)
    return cs

def parseHtml(html):
    print(html)
    return 0 

def parseText(text):
    #1 - Methode Procedural
    #print(text) #List of lines
    """
    print("type de mission ",text[0])
    print("compétences ",text[1])
    print("localisation ",text[2])
    print("Issuer ",text[3])
    print("Publiée ",text[6])
    print("Mobilité",text[10])
    print("Description","".join(text[11:]))
    """
    #Separate by /s,-

    #2 - Methode Regex 
    print("abc ",p.match("abc"))
    print("dates ",date_regex.findall(text[6]))
    
    #A part la date, aucune autre infos ne peut être retrouvée sans analyse
    
    #A- pos tags
    pos_tags = get_postags(ex_text)
    #print(pos_tags)

    # definir pattern
    NE_text = get_noun_phrase_pattern(pos_tags)
    print(NE_text)

    #IOB tag reprensentation of POS TAGS
    iob_tagged = tree2conlltags(NE_text)
    pprint(iob_tagged)

    ne_tree = nltk.ne_chunk(pos_tags)
    #ne_tree = ne_chunk(pos_tag(word_tokenize(ex)))
    print("tree NER", ne_tree)

    #using spacy model
    #NER is more accurate
    doc = nlp(ex_text)
    pprint([(X.text,X.label_) for X in doc.ents])
    pprint([(X, X.ent_iob_, X.ent_type_) for X in doc]) #avec BILUO
    #B - Hierarchiser , debut, milieu , fin, frequences



    #3 - Methode IA 
        #a -Vectoriser
        #b- utiliser le modele pour reconnaitre les pattern

    return 0


#parseHtml(file_html_lines)
parseText(file_text_lines)

