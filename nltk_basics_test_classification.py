import nltk
import random
from nltk.corpus import movie_reviews 

doc = []
for f in movie_reviews.feilds('pos'):
    print f
