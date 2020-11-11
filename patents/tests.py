from django.test import TestCase
import spacy
import os
from spacy import displacy

# Create your tests here.

text = "Madrid is in Spain"
nlp = spacy.load("en_core_web_sm")

doc = nlp(text)
ents = [(e.text, e.label_) for e in doc.ents]
print(str(ents).strip('[]'))
print(os.getcwd())

k = spacy.load('chem_model')

d = k("Organice compound diphenylmethane is a checmical compound")
ents = [(e.text, e.label_) for e in d.ents]
print(ents)


