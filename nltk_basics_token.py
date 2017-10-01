from nltk.stem import WordNetLemmatizer

ltz = WordNetLemmatizer()


print (ltz.lemmatize("better",pos='a'))
print (ltz.lemmatize("best",pos='a'))
