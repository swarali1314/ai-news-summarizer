# 📰 AI News Summarizer & Sentiment Analyzer

An AI-powered web application that uses **Natural Language Processing (NLP)** to summarize news articles and analyze their sentiment.

Users can paste a news article and receive an **AI-generated summary, sentiment classification, and confidence score** through an interactive Streamlit interface.

## 🌐 Live Demo

👉 https://ai-news-summarizer-jsh8gz27q3aplyy9lwskca.streamlit.app/

## 💻 GitHub Repository

👉 https://github.com/swarali1314/ai-news-summarizer

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
- 📱 Simple and user-friendly interface

## 📸 Application Preview

### 🖥️ Application Interface

The main interface allows users to enter a news article and start the AI analysis.

<img width="1880" height="902" alt="AI News Summarizer Interface" src="https://github.com/user-attachments/assets/226045af-79dc-485e-bff1-eb8fdbda3ee2" />

### 🤖 AI Analysis Result

After processing the article, the application displays an AI-generated summary, sentiment classification, and confidence score.

<img width="1802" height="590" alt="AI News Summarizer Results" src="https://github.com/user-attachments/assets/0abd466f-2805-41e7-bd5e-456c786e175f" />

## 🧠 How It Works

The application follows this NLP pipeline:

```text
User enters a news article
          ↓
Text preprocessing
          ↓
Text summarization using FLAN-T5
          ↓
Sentiment analysis
          ↓
Summary + Sentiment + Confidence Score
```

### 1. 📝 Text Input

The user enters a news article through the Streamlit interface.

### 2. 🧹 Text Preprocessing

Basic preprocessing is applied to clean and prepare the article before it is passed to the NLP models.

### 3. 🤖 Text Summarization

The application uses the pretrained **Google FLAN-T5-small** Transformer model to generate a concise summary of the article.

### 4. 📊 Sentiment Analysis

The application analyzes the article and classifies its overall sentiment as:

- 🟢 Positive
- 🔴 Negative
- 🟡 Neutral

A confidence score is also displayed with the prediction.

### 5. 📄 Results

The application displays:

- Original article
- AI-generated summary
- Sentiment classification
- Confidence score

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Hugging Face Transformers**
- **PyTorch**
- **Natural Language Processing (NLP)**
- **FLAN-T5**
- **Sentiment Analysis**
- **CSS**

## 📂 Project Structure

```text
AI-News-Summarizer/
│
├── app.py
├── style.css
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation & Setup

### Prerequisites

Make sure the following are installed on your system:

- Python 3.x
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/swarali1314/ai-news-summarizer.git
```

### 2. Navigate to the Project Directory

```bash
cd ai-news-summarizer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 📊 Example

### Input

```text
The technology company reported strong financial results for the
latest quarter. Revenue increased significantly due to growing
customer demand for its new products and services. The company
also announced plans to invest more in artificial intelligence,
research, and product development.
```

### Output

**AI Generated Summary**

The technology company reported strong financial results driven by increased customer demand. The company plans to invest more in artificial intelligence, research, and product development.

**Sentiment:** Positive

**Confidence:** 99%+

> Note: The exact generated summary and confidence score may vary depending on the input article and model prediction.

## 🎯 Project Objective

The objective of this project is to demonstrate the practical application of **NLP and Transformer-based models** for automated news analysis.

The project combines text preprocessing, AI-based summarization, and sentiment analysis into a single interactive web application.

## 🎓 Learning Outcomes

Through this project, I practiced:

- Python programming
- Natural Language Processing
- Text preprocessing
- Transformer-based NLP models
- Hugging Face Transformers
- Sentiment classification
- Model inference
- Streamlit application development
- Git and GitHub

## 🔮 Future Improvements

- 🌐 Accept news article URLs directly
- 📰 Integrate a News API
- 🌍 Support multiple languages
- 📊 Add sentiment visualization
- 💾 Allow users to download analysis results
- ⚡ Improve model inference speed
- 🔍 Add keyword and topic extraction
- ☁️ Further optimize deployment

## 👨‍💻 Author

**Swarali Gurav**

AI/NLP portfolio project demonstrating practical implementation of text summarization, sentiment analysis, text preprocessing, and Streamlit application development.
