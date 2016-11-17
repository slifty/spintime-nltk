import nltk
from nltk import ngrams

# Load the transript
with open ("transcript.txt", "r") as myfile:
    transcript = myfile.read()

# Generate 3-grams
n = 3
grams = ngrams(transcript.split(), n)

# Count how often each gram appears
fdist = nltk.FreqDist(grams)
for k,v in fdist.most_common(50):
    print k,v
