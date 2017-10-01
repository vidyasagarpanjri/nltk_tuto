from nltk.corpus import wordnet

syn = wordnet.synsets("girl")
print syn
print syn[0]
print syn[0].lemmas()

print syn[0].definition()
#print syn[0].lemmas()[:].antonyms()
for s in syn:
    for l in s.lemmas():
        if l.antonyms():
            print l.antonyms()
