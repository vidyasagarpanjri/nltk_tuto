#!/usr/bin/python
import string
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk import WordNetLemmatizer,pos_tag
#from nltk.logic
import email_parser
import glob
#Email body
body = email_parser.message_body(r'/home/vidyasagar/automation/messages/dat2/2683277295')                                               

def msg_preprocessor(body):
    #word token
    words = wordpunct_tokenize(body)
    #without puct
    word_puct=[w for w in words if w not in string.punctuation]
    #Stopwords
    word_stop_token=[w for w in word_puct if w not in stopwords.words('english')]
    #stem
    ps = SnowballStemmer('english')
    word_stem = [ps.stem(w) for w in word_stop_token]
    #print word_stem,len(word_stem)
    #lemma
    lemm = WordNetLemmatizer()
    word_lemma=[(lemm.lemmatize(t),tg) for t,tg in pos_tag(word_stem)]

    return word_lemma

#print msg_preprocessor(body)
dating_word=[]
folder = glob.glob(r'/home/vidyasagar/automation/messages/dat2/*')
for f in folder:
    body = email_parser.message_body(f)
    dating_word.extend(msg_preprocessor(body))
folder = glob.glob(r'/home/vidyasagar/automation/messages/phish1/*')
phish_word=[]
for f in folder:
    body = email_parser.message_body(f)
    phish_word.extend(msg_preprocessor(body))    
#print dating_word,len(dating_word)
fd = nltk.FreqDist(dating_word)
fdp = nltk.FreqDist(phish_word)
print phish_word[5]
feature_set_train = [({i:j},'dat') for i,j in fd.most_common(100)]
feature_set_train.extend([({i:j},'phish') for i,j in fdp.most_common(100)])
clf = nltk.NaiveBayesClassifier.train(feature_set_train)
print clf.classify({'login':'NN'})
#i=[i for i,j in dating_word]
#print i
##print len(words)
##print len(word_puct)
##print len(word_stop_token)
##print len(word_stem)
##print len(word_lemma)

#preprocess    
#feature
#classifiesr
