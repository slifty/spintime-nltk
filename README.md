# spintime-nltk

This repository contains some simple tips and tricks for analyzing the contents of transcripts.

## What's an N-gram
An n-gram is a cluster of "n" words that appear together in a piece of text.  It's a way of summarizing text and finding short phrases that are often seen together.

## Using A Website
The simplest way to start exploring n-grams is to check out this [n-gram analyser](http://guidetodatamining.com/ngramAnalyzer/).  Simply paste your text and play with the tools.

For instance, when running against the transcript from the first debate, I see that the top 4-grams are the following:

```
WE ARE GOING TO	12	0.07506098705198
TAKE A LOOK AT	8	0.050040658034653
WANT TO SEE THE	6	0.03753049352599
IS GOING TO BE	6	0.03753049352599
TO SEE THE COURT	5	0.031275411271658
YOU WANT TO SEE	5	0.031275411271658
MILLIONS OF PEOPLE THAT	4	0.025020329017327
ONE OF THE WORST	4	0.025020329017327
```

## Using NLTK
If you are feeling adventurous and ready to program, read on!

NLTK ("natural language toolkit") is a python library that provides a suite of tools for working with and analyzing text.  n-grams are one of the things it can do out of the box!

Take the following script as an example:

```python
from nltk import ngrams
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 6
sixgrams = ngrams(sentence.split(), n)
for grams in sixgrams:
  print grams
```

This example script creates 6-grams from the example sentence, and outputs all of them.  You could imagine creating an alternative source for the input (from a file, for instance), adjusting the "n" to be fewer than 6, or otherwise adding logic about which 6-grams you care about most.

To run this type of script you need to either install or make sure you already have:

1. Python 2.7 or 3.2+ (Google is your friend here; it will vary depending on your computer type)
2. NLTK (http://www.nltk.org/install.html)

If you need help ask in Slack!

An example script which will load a text file can be found in `scripts/nltk-example.py` from this repository.
