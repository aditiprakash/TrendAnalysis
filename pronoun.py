import nltk
import urllib.request 
from bs4 import BeautifulSoup

address = 'http://celebscinema.com/india/rajinikanth-next-president-india/5982/'
soup = BeautifulSoup(urllib.request.urlopen(address).read(), "html.parser")
span = soup.find("p", {"style":"text-align: justify;"})  
paras = [x for x in span.findAllNext("p")]

start = span.string
middle = "\n\n".join(["".join(x.findAll(text=True)) for x in paras[:-1]])
last = paras[-1].contents[0]
text = "%s\n\n%s\n\n%s" % (start, middle, last)




#text = """The Buddha, the Godhead, resides quite as comfortably in the circuits of a digital
#computer or the gears of a cycle transmission as he does at the top of a mountain
#or in the petals of a flower. To think otherwise is to demean the Buddha...which is
#to demean oneself."""

sentence_re = r'[a-zA-Z]+'
lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()
grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
        
    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)

toks = nltk.regexp_tokenize(text, sentence_re)
postoks = nltk.tag.pos_tag(toks)



def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()

def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    word = stemmer.stem(word)
    word = lemmatizer.lemmatize(word)
    return word

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    accepted = bool(2 <= len(word) <= 40
        and word.lower() not in stopwords)
    return accepted


def get_terms(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term

tree = chunker.parse(postoks)

from nltk.corpus import stopwords
stopwords = stopwords.words('english')

for leaf in leaves(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        print(term)
