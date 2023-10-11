>>>Definir les data a extraire

>>>Extraire
Permettre le scrapping 

Immo, Recette ,Phrases, voyage


>> POS TAG PATTERN 
récupérer POS TAG 
JJ adjectif
NN/NNS nom commun 
NNP 
CD chiffres
DT déterminant
VB verbe
VBG verbe on going
VBD verbe au passé

exemple 'NP: {<DT>?<JJ>*<NN>}'
notre pattern est entre parenthèse

Resultat :
(S
  European/JJ
  authorities/NNS
  fined/VBD
  Google/NNP
  (NP a/DT record/NN)
  $/$
  5.1/CD
  billion/CD
  on/IN
  Wednesday/NNP
  for/IN
  abusing/VBG
  its/PRP$
  (NP power/NN)
  in/IN
  (NP the/DT mobile/JJ phone/NN)
  (NP market/NN)
  and/CC
  ordered/VBD
  (NP the/DT company/NN)
  to/TO
  alter/VB
  its/PRP$
  practices/NNS)


  Using IOB Tag to have context

  B-NP beginning of noun phrase 
  I-NP inside of the current noun-phrase

  B-VP/I-VP beginning and inside of Verb phrase

SPACY 
  NORD (nationalities or religious or political groups),
  MONEY
  DATE

fr_core_news_sm 
eng_core_web_sm

USING BILUO notation
Beginning
Inner
Last
Unit 
Out

