from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import nltk

nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")


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
            vector = self.vectorizer.fit_transform([content])
            terms = self.vectorizer.get_feature_names_out()
            tfidfScores = vector.toarray()[0]
            top_indices = tfidfScores.argsort()[-top_n:][-1]
            return [terms[i] for i in top_indices]
        
        X = self.vectorizer.transform([content])
        cluster_idx = self.model.predict(X)[0]
        cluster_docs = [self.fitted_docs[i] for i, label in enumerate(self.model.labels_) if label == cluster_idx]
        all_text = " ".join(cluster_docs + [content])
        vector = self.vectorizer.transform([all_text])
        terms = self.vectorizer.get_feature_names_out()
        tfidfScore =vector.toarray()[0]
        top_indices = tfidfScore.argsort()[-top_n:][::-1]
        lemmatized_terms = [
            self.lemmatizer.lemmatize(term) for term in terms
        ]
        return [lemmatized_terms[i] for i in top_indices]

    


docs = [
  "React ile frontend geliştirme",
  "Python ile makine öğrenmesi çalış",
  "Alışveriş listesi: süt, ekmek, yumurta",
  "Günlük koşu ve spor rutini"
]

t = Tagger()
t.fit_docs(docs, n_cluster=3)
print(t.suggest_tag("Bugün python öğren ve model eğit"))







