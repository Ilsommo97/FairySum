from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from reading import extract_id, createDictionary, createCorpus
import spacy


#Handling the texts
PATH_FAIRY_TALES =   './FAIRY_TALE/texts/'
PATH_SHORT_STORIES = './SHORT_STORY/texts/'
FtDictionary = createDictionary(PATH_FAIRY_TALES)
SsDictionary = createDictionary(PATH_SHORT_STORIES)

""" 
#Creating the bert model
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
"""

"""
Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. 
This may not generalize well for all use cases in different domains.
!!!
"""

"""
The list of entities that spacy model can return is :
('CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 
'MONEY', 'NORP', 'ORDINAL', 'ORG', 'PERCENT', 'PERSON', 'PRODUCT', 'QUANTITY', 'TIME', 'WORK_OF_ART')

PERSON:      People, including fictional.
NORP:        Nationalities or religious or political groups.
FAC:         Buildings, airports, highways, bridges, etc.
ORG:         Companies, agencies, institutions, etc.
GPE:         Countries, cities, states.
LOC:         Non-GPE locations, mountain ranges, bodies of water.
PRODUCT:     Objects, vehicles, foods, etc. (Not services.)
EVENT:       Named hurricanes, battles, wars, sports events, etc.
WORK_OF_ART: Titles of books, songs, etc.
LAW:         Named documents made into laws.
LANGUAGE:    Any named language.
DATE:        Absolute or relative dates or periods.
TIME:        Times smaller than a day.
PERCENT:     Percentage, including ”%“.
MONEY:       Monetary values, including unit.
QUANTITY:    Measurements, as of weight or distance.
ORDINAL:     “first”, “second”, etc.
CARDINAL:    Numerals that do not fall under another type.

"""


def add_value(dict_obj, key, value):
    ''' Adds a key-value pair to the dictionary.
        If the key already exists in the dictionary, 
        it will associate multiple values with that 
        key instead of overwritting its value'''
    if key not in dict_obj:
        dict_obj[key] = value
    elif isinstance(dict_obj[key], list):
        dict_obj[key].append(value)
    else:
        dict_obj[key] = [dict_obj[key], value]




def TSV(path: str, dictionary_short: dict, dictionary_tales: dict):
    """
    This function will output the tsv file with the predicted result in the required TSV format.
    For the time being, we have several problems. The biggest one is probably the fact a single entity gets 
    tagged to different entitities throughout the text it belongs to. We need to post process the results trying to look for
    each entity that gets categorized differently throughout the tale/story on a online source, like babelnet. Other than this,
    the next approach would be to count the occurrunces of the labels of the named entities throughout the text and choose
    the most frequent one. Moreover, since the model seems to perform very poorly, one could take into account different models 
    in this count, i.e nltk ecc..
    """
    nlp = spacy.load("en_core_web_sm")
    with open(path + 'result.tsv', 'w') as w:
        for text in dictionary_tales:
            doc = nlp(dictionary_tales[text])
            id = text
            pred_dict = {}
            for entity in doc.ents:
                
                #Storing each line to print in the tsv inside a list of lists:
                add_value(pred_dict, entity.text, entity.label_)
        print(pred_dict)

                    
                        

                
                


        """ #Checking for the entities, we just need PER LOC ORG
                #Moreover, we're going to categorize GPE entity with LOC, NORP with PER and FAC with ORG
                if entity.label_ == 'GPE' or entity.label_ =='LOC':
                    w.write(id + '\t' + str(entity.start_char) + '\t' +  str(entity.end_char) + '\t' + 'LOC \t' )
                if entity.label_ == 'PERSON' or entity.label_ == 'NORP':
                    w.write(id + '\t' + str(entity.start_char) + '\t' +  str(entity.end_char) + '\t' + 'PER \t' )
                if entity.label_ == 'ORG' or entity.label_ == 'FAC':
                    w.write(id + '\t' + str(entity.start_char) + '\t' +  str(entity.end_char) + '\t' + 'ORG \t' )
                w.write(entity.text + '\n')

#               w.write(id + '\t' + str(entity.start_char) + '\t' +  str(entity.end_char) + '\t' + entity.label_ + '\t' + entity.text+ '\n')



        for text in dictionary_short:
            doc = nlp(dictionary_short[text])
            id = text
            for entity in doc.ents:
                #Checking for the entities, we just need PER LOC ORG
                #Moreover, we're going to categorize GPE entity with LOC
                if entity.label_ == 'GPE' or entity.label_ =='LOC':
                    w.write(id + '\t' + str(entity.start_char) + '\t' +  str(entity.end_char) + '\t' + 'LOC \t' )
                if entity.label_ == 'PERSON' or entity.label_ == 'NORP':
                    w.write(id + '\t' + str(entity.start_char) + '\t' +  str(entity.end_char) + '\t' + 'PER \t' )
                if entity.label_ == 'ORG' or entity.label_ == 'FAC':
                    w.write(id + '\t' + str(entity.start_char) + '\t' +  str(entity.end_char) + '\t' + 'ORG \t' )
                w.write(entity.text + '\n')
 """



TSV('./', SsDictionary, FtDictionary)


