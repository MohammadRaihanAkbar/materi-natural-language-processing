import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

teks = "Presiden Joko Widodo mengunjungi Universitas Indonesia Depok di hari Senin"
token = word_tokenize(teks)
filtered_token = []
stopword = set(stopwords.words('indonesian'))

for token in token:
    if token not in stopword:
        filtered_token.append(token)

print(filtered_token)
