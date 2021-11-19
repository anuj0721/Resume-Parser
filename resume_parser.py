import nltk
nltk.download('stopwords')
import os
os.system('python -m spacy download en_core_web_sm')

from pyresparser import ResumeParser
import os

data = []
for file_name in os.listdir('Assignment'):
    data.append(ResumeParser(f'Assignment/{file_name}').get_extracted_data())

for i in range(len(os.listdir('Assignment'))):
  print(data[i]['name'])