import nltk
nltk.download('punkt')
nltk.download('stopwords')

from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def extract_keywords(messages, top_n=5):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(" ".join(messages).lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]
    return [word for word, _ in Counter(words).most_common(top_n)]

def extract_tfidf_keywords(messages, top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([" ".join(messages)])
    scores = zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[0])
    sorted_words = sorted(scores, key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words[:top_n]]
