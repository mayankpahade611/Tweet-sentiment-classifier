import streamlit as st
import pickle
import re

# 📦 Load the model and vectorizer
model = pickle.load(open('models/sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('models/tfidf_vectorizer.pkl', 'rb'))

# 🧹 Clean function (same as in training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    
    # Optional: remove stopwords
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered = [word for word in words if word not in stop_words]
    return ' '.join(filtered)

# 🚀 Streamlit UI
st.set_page_config(page_title="Tweet Sentiment Classifier", layout="centered")
st.title("🧠 Tweet Sentiment Classifier")
st.write("Enter a tweet below to predict its sentiment:")

tweet = st.text_area("📨 Enter Tweet Here:")

if st.button("Predict Sentiment"):
    if tweet.strip() == "":
        st.warning("Please enter a tweet!")
    else:
        cleaned = clean_text(tweet)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]
        
        if prediction == 1:
            st.success("✅ **Sentiment:** Positive 😀")
        else:
            st.error("⚠️ **Sentiment:** Negative 😠")
