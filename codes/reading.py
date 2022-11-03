import os

PATH_FAIRY_TALES =   '../FairySum/FAIRY_TALE/texts'
PATH_SHORT_STORIES = '../FairySum/SHORT_STORY/texts'


def extract_id(filename):
  first_underscore = False
  id = ''
  for char in filename:
    if char == '_':
      if first_underscore == True:
        break
      first_underscore = True
    id = id + char
  return id

l = os.getcwd()
file_list = os.listdir(PATH_FAIRY_TALES)



