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
#print body
print email_parser.message_body(r'/home/vidyasagar/git_repo/nltk_tuto/spam/0001.bfc8d64d12b325ff385cca8d07b84288') 
def msg_preprocessor(body):
    #word token
    words = wordpunct_tokenize(body)
    #without puct
    word_puct=[w for w in words if w not in string.punctuation]
    #without Stopwords
    word_stop_token=[w for w in word_puct if w not in stopwords.words('english')]
    #stemmed
    ps = SnowballStemmer('english')
    word_stem = [ps.stem(w) for w in word_stop_token]
    #print word_stem,len(word_stem)
    #lemmanteised 
    lemm = WordNetLemmatizer()
    word_lemma=[(lemm.lemmatize(t),tg) for t,tg in pos_tag(word_stem)]

    return word_lemma

#def feature_extraction(feature,lable):
#    feature_set=[]

#print msg_preprocessor(body)
##dating_word=[]
##folder = glob.glob(r'/home/vidyasagar/automation/messages/dat2/*')
##for f in folder:
##    body = email_parser.message_body(f)
##    dating_word.extend(msg_preprocessor(body))
##folder = glob.glob(r'/home/vidyasagar/automation/messages/phish1/*')
##phish_word=[]
##for f in folder:
##    body = email_parser.message_body(f)
##    phish_word.extend(msg_preprocessor(body))    
#print dating_word,len(dating_word)
#fd = nltk.FreqDist(dating_word)
#fdp = nltk.FreqDist(phish_word)
#fd.pprint()
#fdp.pprint()
#print phish_word[5:50]
##feature_set_train = [({i:j},'dat') for i,j in fd.most_common(100)]
##feature_set_train.extend([({i:j},'phish') for i,j in fdp.most_common(100)])
##print feature_set_train[100:-1]
##clf = nltk.NaiveBayesClassifier.train(feature_set_train)
##print clf.classify({('m','NN'):2})
##print nltk.classify.accuracy(clf,{('messag','NN'):1})
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
