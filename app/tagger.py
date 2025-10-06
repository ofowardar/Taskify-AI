from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

class Tagger:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.model = None
        self.fitted_docs = []

    
    def fit(self,docs,n_clusters=5):
        if not docs:
            return
        self.fitted_docs = docs
        X = self.vectorizer.fit_transform(docs)
        self.model = KMeans(n_clusters=min(n_clusters,len(docs)),random_state=42)
        self.model.fit(X)

    def suggest_tags(self,content,top_n=3):
        """
        Suggest tags for new tasks content
        """

        if not self.model:
            vector = self.vectorizer.fit_transform([content])
            terms = self.vectorizer.get_feature_names_out()
            tfidf_scores = tfidf_scores.argsort()[-top_n:][::-1]







