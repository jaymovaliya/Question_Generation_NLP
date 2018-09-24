from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import operator
import string


def TermFreq(wordDict, text):
    tfDict = {}
    totlen = len(text)
    for w, cnt in wordDict.items():
        tfDict[w] = cnt / float(totlen)
    return tfDict


f = open('image.txt', encoding="utf8")
content = f.read().lower()
stop_words = set(stopwords.words('english'))
stop_words.add("’")
data = word_tokenize(content)
sentenses = sent_tokenize(content)
print(sentenses)
filter_text = []
for w in data:
    if w not in stop_words and w not in string.punctuation:
        filter_text.append(w)
wordDict = dict.fromkeys(filter_text, 0)
for w in filter_text:
    wordDict[w] += 1
print(wordDict)
tf = TermFreq(wordDict, filter_text)
sorted_tf = sorted(tf.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_tf)
senDict = dict.fromkeys(sentenses, 0)
for s in sentenses:
    tok = word_tokenize(s)
    length = 0
    weight = 0
    for w in tok:
        if (w in tf.keys()):
            length += 1
            weight += tf[w]
    senDict[s] = weight / length
print(senDict)
sorted_sd = sorted(senDict.items(), key=operator.itemgetter(1), reverse=True)
for sen, val in sorted_sd:
    print(sen)
    print(val)
