import numpy as np
import pandas as pd
import cv2
import pytesseract
from glob import glob
#import spacy
import re
import string
#from spacy import displacy

panNum = input("Enter your pan card number:")


def cleanText(txt):
    whitespace = string.whitespace
    punctuation = '!"#$%&\'()*+,/:;<=>?@[\]^_`{|}~'
    tableWhitespace = str.maketrans('', '', whitespace)
    tablePunctuation = str.maketrans('', '', punctuation)

    text = str(txt)
    #text = text.lower()
    removewhitespace = text.translate(tableWhitespace)
    removepunctuation = removewhitespace.translate(tablePunctuation)

    return str(removepunctuation)


#Load Image
image = cv2.imread('./Dataset/Test/pan.jpeg')
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#extract data using pytesseract
tessData = pytesseract.image_to_data(image)

#convert data into dataframe
tessList = list(map(lambda x:x.split('\t'), tessData.split('\n')))
df = pd.DataFrame(tessList[1:], columns = tessList[0])
df.dropna(inplace=True)
df['text'] = df['text'].apply(cleanText)

#convert data into content
df_clean = df.query('text != " " ')
content = " ".join([w for w in df_clean['text']])

verify = 0
for i in content:
    if panNum in content:
        verify = 1

if (verify == 1):
    print('Verified')
else:
    print('Not Verified')



