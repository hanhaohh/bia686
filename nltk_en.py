# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>


# <codecell>

# mac:
#     sudo pip install pandas 
#     sudo pip install nltk
# windows:
#     pip install nltk
#     pip install pandas

# <codecell>

import nltk
import re
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
text = """NLTK is a leading platform for building Python programs to work with 
human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources 
such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, 
tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion
forum. Thanks to a hands-on guide introducing programming fundamentals alongside topics in computational 
linguistics, plus comprehensive API documentation, NLTK is suitable for linguists, engineers, students, 
educators, researchers, and industry users alike. NLTK is available for Windows, Mac OS X, and Linux. 
Best of all, NLTK is a free, open source, community-driven project."""

# <codecell>

from nltk import sent_tokenize,word_tokenize

# Sentence Tokenize
string = "hello Mr. Smith, How  are you doing today? the waiter said"
#print sent_tokenize(string)
# word tokenzie
text_tokenize = word_tokenize(text)
fdist1 = nltk.FreqDist(text_tokenize)

fdist1.plot(50, cumulative=True)

# <codecell>

from nltk.corpus import stopwords
stopwords.words("english")

# <codecell>

from nltk.stem import PorterStemmer
new_text = """Stemming algorithms attempt to automatically remove suffixes (and in some 
cases prefixes) in order to find the "root word" or stem of a given word. This 
is useful in various natural language processing scenarios, such as search """
ps = PorterStemmer()
from nltk import word_tokenize
for i in word_tokenize(new_text):
    print ps.stem(i)

# <codecell>

def remove_non_ascii_2(text):
    return re.sub(r'[^\x00-\x7F]',' ', text)

# <codecell>

from nltk import sent_tokenize,word_tokenize
test_string = "hello Mr. Smith, How  are you doing today? the waiter said"
test_string_token = sent_tokenize(test_string)
a = word_tokenize(test_string_token[0])
nltk.pos_tag(a)


# <codecell>

import nltk
from nltk import sent_tokenize,word_tokenize
fw = open("064.txt")
sample = remove_non_ascii_2(fw.read())
#from nltk.tokenize import PunktSentenceTokenizer
tokenized = sent_tokenize(sample)# a list of sentence 
def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print tagged
            chunkGram = r"""Chunk: {<NNP>+}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            for subtree in chunked.subtrees():
                if subtree.label() == "Chunk":
                    print subtree.leaves
    except Exception as e:
        print(str(e))

process_content()

# <codecell>


# <codecell>

import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import LineTokenizer
from nltk.corpus import state_union
fw = open("064.txt")
text = remove_non_ascii_2(fw.read())

import nltk.data
sents = LineTokenizer(blanklines=u'discard').tokenize(text.strip())
for i in sents:
    words = nltk.word_tokenize(i)
    pos = nltk.pos_tag(words)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing isolated surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []
    print person_list 

#     print tagged
    print "******\n"

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>

import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import LineTokenizer
from nltk.corpus import state_union
fw = open("064.txt")
text = remove_non_ascii_2(fw.read())

import nltk.data
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
sents = LineTokenizer( blanklines=u'discard').tokenize(text.strip())
for i in sents:
    words = nltk.word_tokenize(i)
#   words = [word for word in words if word.lower() not in stopwords.words("english")]
#   words = [word for word in words if word.lower() not in string.punctuation]
    pos = nltk.pos_tag(words)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []
    print person_list 

#     print tagged
    print "******\n"

# <codecell>

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when

# <codecell>


