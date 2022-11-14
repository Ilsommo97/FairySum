import spacy
from reading import extract_id, createDictionary, createCorpus


nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple is looking at buying U.K. startup for $1 billion") 
#doc is now a spacy class, accessing doc.ents gives us all 
#entity recoginzed by the model


PATH_FAIRY_TALES =   './FAIRY_TALE/texts/'
PATH_SHORT_STORIES = './SHORT_STORY/texts/'
FtDictionary = createDictionary(PATH_FAIRY_TALES)
SsDictionary = createDictionary(PATH_SHORT_STORIES)

corpus = ''

"""
One thing that is maybe worth trying is splitting the text into sentences as i may have read that this helps the already 
pretrained models on NER
"""
test = {}

test['ciao'] = 5
test['ciao'] = 6

print(test['k'])