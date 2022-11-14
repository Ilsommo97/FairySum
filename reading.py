import os

def extract_id(filename: str):
  """
  A simple helper function to extract the id from each text filename
  """
  size = len(filename)
  id = filename[:size - 4]   # This line of code will remove the last four charachters i.e .txt
  return id


def createDictionary(path: str):

  """
  This function takes as input the relative path to the texts provided and outputs a dictionary composed of paired id-text
  """
  dictionary = {}
  file_list = os.listdir(path) # Here put PATH_FAIRY_TALES
  for text in file_list:  
    with open(path + text, 'r') as r:
      #text holds the id and the name of the story (we actually dont need the name of the story)
      #r.read() reads and returns the text of the story
      dictionary[extract_id(text)] = r.read()

      
  return dictionary


def createCorpus(pathToShort: str, pathToTales: str):
  """
  This function is gonna create a unique document containing the texts in the fairy tale and short stories directories
  Applying the BERT NER tagger directly to the output of this function is going to directly give us the required starting and 
  ending offset charachter of each entity in the texts
  """

  file_list_tales = os.listdir(pathToTales) 
  file_list_stories = os.listdir(pathToShort)
  unique_document = ''
  for text in file_list_tales:
    with open(pathToTales + text, 'r') as r:
      unique_document = unique_document + r.read()

  for text in file_list_stories:
    with open(pathToShort + text, 'r') as r:
      unique_document = unique_document + '\n' +  r.read()

  return unique_document










