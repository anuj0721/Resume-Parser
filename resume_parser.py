import nltk
nltk.download('stopwords')

from pyresparser import ResumeParser
import os

data = []
for file_name in os.listdir('Assignment'):
    data.append(ResumeParser(f'Assignment/{file_name}').get_extracted_data())

for i in range(len(os.listdir('Assignment'))):
  print(data[i]['name'])