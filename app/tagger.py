from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import nltk
from nltk.corpus import stopwords
import string


# nltk.download("punkt_tab")
# nltk.download("wordnet")
# nltk.download("omw-1.4")
#nltk.download("stopwords")
sw = set(stopwords.words("english"))



class Tagger:
    lemmatizer = nltk.WordNetLemmatizer()
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.fitted_docs = []
        self.model = None

    def fit_docs(self,docs,n_cluster:int = 5):
        if not docs:
            return "Docs is Empty!!"
        self.fitted_docs = docs
        vectorized_docs = self.vectorizer.fit_transform(docs)
        self.model = KMeans(n_clusters=min(n_cluster,len(docs)),random_state=42)
        self.model.fit(vectorized_docs)

    
    def suggest_tag(self,content,top_n:int = 3):
        if not self.model:
            return "Model not found!!"
        
        X = self.vectorizer.transform([content])
        cluster_idx = self.model.predict(X)[0]
        cluster_docs = [self.fitted_docs[i] for i, label in enumerate(self.model.labels_) if label == cluster_idx]
        all_text = " ".join(cluster_docs + [content])

        translator = str.maketrans('', '', string.punctuation)
        tokenized_allText = [word.translate(translator) for word in all_text.split()]

        sw_set = set(word.lower() for word in sw)
        sw_filtered = [word for word in tokenized_allText if word.lower() not in sw_set]

        vector = self.vectorizer.transform([" ".join(sw_filtered)])
        terms = self.vectorizer.get_feature_names_out()
        tfidfScore = vector.toarray()[0]
        top_indices = tfidfScore.argsort()[-top_n:][::-1]

        fullFiltered_terms = [self.lemmatizer.lemmatize(term) for term in terms]

        return [fullFiltered_terms[i] for i in top_indices]

    


# Test BLock :)

# docs = [
#   "React ile frontend geliştirme",
#   "Python ile makine öğrenmesi çalış",
#   "Alışveriş listesi: süt, ekmek, yumurta",
#   "Günlük koşu ve spor rutini"
# ]

# t = Tagger()
# t.fit_docs(docs, n_cluster=3)
# print(t.suggest_tag("Bugün python öğren ve model eğit"))







for i in sw:
    if i == "with":
        print(i)