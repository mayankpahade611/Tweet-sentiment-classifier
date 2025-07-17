# 🐦 Tweet Sentiment Classifier

A machine learning web app that classifies the **sentiment** of a tweet as **Positive**, **Negative**, or **Neutral** using Natural Language Processing and Scikit-learn.  
This project uses **TF-IDF Vectorization**, **Logistic Regression**, and is deployed with **Streamlit**.

> ⚠️ Note: The original CSV dataset (`tweet.csv`) has been removed from this repository due to GitHub's 100MB file size limit. See [🔽 Dataset Download Instructions](#-dataset-download-instructions) below.

---

## 🚀 Live Demo

🔗 [**Click here to open the app**](https://your-streamlit-app-url)

> Replace the URL above with your actual deployed Streamlit Cloud link.

---

## 📌 Features

- Cleans and processes tweet text (stopwords, punctuation, lowercase, etc.)
- Converts text to numerical form using TF-IDF
- Predicts sentiment using Logistic Regression
- Simple Streamlit interface
- Fully open-source and easy to extend

---

## 📂 Project Structure


---

## 🔽 Dataset Download Instructions

Due to GitHub’s file size restrictions, the dataset (`tweet.csv`, ~227MB) is not included in this repository.  

To use this project locally:

1. Go to [this Kaggle dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)
2. Download the file and extract it
3. Place the CSV file inside a `data/` folder in your project directory:

---

## 💻 Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Phantom611/Tweet-sentiment-classifier.git
   cd Tweet-sentiment-classifier
2. (Optional) Create a virtual environment
    python -m venv venv
    source venv/bin/activate  ## On Windows: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Download NLTK stopwords (first time only)
   import nltk
   nltk.download('stopwords')

5. Run the app
   streamlit run app.py

🙋‍♂️ Author
Mayank Pahade
- GitHub: @Phantom611
- LinkedIn: Coming soon

