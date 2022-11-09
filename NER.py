from venv import create
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from reading import extract_id, createDictionary, createCorpus


#Handling the texts
PATH_FAIRY_TALES =   './FAIRY_TALE/texts/'
PATH_SHORT_STORIES = './SHORT_STORY/texts/'
FtDictionary = createDictionary(PATH_FAIRY_TALES)
SsDictionary = createDictionary(PATH_SHORT_STORIES)


corpus = createCorpus(PATH_SHORT_STORIES, PATH_FAIRY_TALES)

print(corpus)




#Creating the bert model
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)



"""
Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. 
This may not generalize well for all use cases in different domains.
!!!
Furthermore, the model occassionally tags subword tokens as entities and post-processing of 
results may be necessary to handle those cases.
!!!
"""
""" for text in SsDictionary:
    result = nlp(SsDictionary[text])
    print(SsDictionary[text])
    print(result)
    break
 """


def TSV(path: str, dictionary_short: dict, dictionary_tales: dict):
    """
    This function will output the tsv file with the predicted result in the required TSV format.
    For the time being, we have several problems. The biggest one is probably the one regarding
    subwords getting tagged. We need to post process the results and try to approach the NER tagging
    from different directions, i.e finding wikipedia references, using different models and maybe even create
    a gold dataset for this specific problem and train an existing NER tagger on the created dataset.
    """

    with open(path + 'result.tsv', 'w') as w:
        for i in range(10):
            w.write('hey' + '\t ciao' + '\t just another one\n')
         

""" 
    
TSV('./', SsDictionary, FtDictionary)

 """