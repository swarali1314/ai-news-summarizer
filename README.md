# 📰 AI News Summarizer & Sentiment Analyzer

An AI-powered web application that summarizes news articles and analyzes their sentiment using Natural Language Processing (NLP).

The application allows users to paste a news article and instantly receive an AI-generated summary along with the sentiment and confidence score.

## 🚀 Features

- 📝 Accepts news articles directly from the user
- ✨ Text preprocessing before analysis
- 🤖 AI-powered text summarization
- 📊 Sentiment analysis
- 📈 Sentiment confidence score
- 🔢 Character and word counter
- ⚠️ Input validation for short articles
- 🗑️ Clear button to reset the input
- 🎨 Modern dark-themed Streamlit interface
- 📱 Simple and user-friendly UI
<img width="1880" height="902" alt="image" src="https://github.com/user-attachments/assets/226045af-79dc-485e-bff1-eb8fdbda3ee2" />
<img width="1880" height="902" alt="Screenshot 2026-08-28 120020" src="https://github.com/user-attachments/assets/226e94d0-a3b1-407b-a78a-81435120af6e" />



## 🧠 How It Works

The application follows this NLP pipeline:

User enters a news article
        ↓
Text preprocessing
        ↓
Text summarization using FLAN-T5
        ↓
Sentiment analysis
        ↓
Display summary + sentiment + confidence


### 1. Text Input

The user enters a news article through the Streamlit interface.

### 2. Text Preprocessing

The article is cleaned before being passed to the NLP models. This helps maintain consistent input for analysis.

### 3. Text Summarization

The application uses the **Google FLAN-T5-small** Transformer model to generate a concise summary of the article.

### 4. Sentiment Analysis

The application analyzes the overall sentiment of the article and classifies it as:

- 🟢 Positive
- 🔴 Negative
- 🟡 Neutral

A confidence score is also displayed.

### 5. Results

The application displays:

- Original article
- AI-generated summary
- Sentiment
- Confidence score

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Natural Language Processing (NLP)
- FLAN-T5
- Sentiment Analysis

## 📂 Project Structure

```text
AI News Summerizer/
│
├── app.py
├── style.css
├── requirements.txt
├── README.md
├── .gitignore
└── venv/              # Local virtual environment - not uploaded
