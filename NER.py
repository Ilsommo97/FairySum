from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from reading import extract_id, createDictionary

PATH_FAIRY_TALES =   './FAIRY_TALE/texts/'
PATH_SHORT_STORIES = './SHORT_STORY/texts/'



FtDictionary = createDictionary(PATH_FAIRY_TALES)
SsDictionary = createDictionary(PATH_SHORT_STORIES)



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
for text in SsDictionary:
    result = nlp(SsDictionary[text])
    print(SsDictionary[text])
    print(result)
    break

