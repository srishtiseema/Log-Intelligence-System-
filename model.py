from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import IsolationForest

def train_model(messages):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(messages)

    model = IsolationForest(contamination=0.3)
    model.fit(X)

    return model, vectorizer

def detect_anomalies(model, vectorizer, messages):
    X = vectorizer.transform(messages)
    preds = model.predict(X)
    
    return preds  # -1 = anomaly, 1 = normal