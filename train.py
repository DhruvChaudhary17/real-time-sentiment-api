import pandas as pd, joblib, re, string, nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

nltk.download("stopwords")
STOPWORDS = set(nltk.corpus.stopwords.words("english"))

def clean(text):
    text = text.lower()
    text = re.sub(r"http\S+|@\w+|#\w+", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = [w for w in text.split() if w not in STOPWORDS]
    return " ".join(tokens)

cols = ["ID", "Entity", "Sentiment", "Tweet"]
df = pd.read_csv("data/twitter_training.csv", names=cols)
df = df.dropna(subset=["Tweet"]).drop_duplicates()
df["clean"] = df["Tweet"].apply(clean)

le = LabelEncoder()
df["y"] = le.fit_transform(df["Sentiment"])

X_train, X_test, y_train, y_test = train_test_split(
    df["clean"], df["y"], test_size=0.2, stratify=df["y"], random_state=42
)

pipe = Pipeline([
    ("tfidf", TfidfVectorizer(min_df=3, ngram_range=(1,2))),
    ("clf", LogisticRegression(max_iter=300, n_jobs=-1, C=4.0)),
])
pipe.fit(X_train, y_train)

print("accuracy:", accuracy_score(y_test, pipe.predict(X_test)))
print(classification_report(y_test, pipe.predict(X_test), target_names=le.classes_))

joblib.dump(pipe, "model/model.joblib")
joblib.dump(le, "model/label_encoder.joblib")