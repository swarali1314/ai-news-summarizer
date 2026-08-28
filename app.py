import streamlit as st
from pathlib import Path
from html import escape

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    pipeline
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI News Summarizer & Sentiment Analyzer",
    page_icon="📰",
    layout="centered"
)


# =========================================================
# LOAD CSS
# =========================================================

def load_css():

    css_path = Path(__file__).parent / "style.css"

    with open(css_path, "r", encoding="utf-8") as file:
        css = file.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )


load_css()


# =========================================================
# LOAD AI MODELS
# =========================================================

@st.cache_resource
def load_models():

    # Summarization model
    tokenizer = AutoTokenizer.from_pretrained(
        "google/flan-t5-small"
    )

    summarization_model = AutoModelForSeq2SeqLM.from_pretrained(
        "google/flan-t5-small"
    )

    # Sentiment model
    sentiment_analyzer = pipeline(
        "sentiment-analysis"
    )

    return (
        tokenizer,
        summarization_model,
        sentiment_analyzer
    )


tokenizer, summarization_model, sentiment_analyzer = load_models()


# =========================================================
# TEXT PREPROCESSING
# =========================================================

def preprocess_text(article):

    # Remove leading and trailing spaces
    article = article.strip()

    # Remove unnecessary spaces and line breaks
    article = " ".join(article.split())

    return article


# =========================================================
# SUMMARIZATION
# =========================================================

def summarize_text(article):

    words = article.split()

    chunk_size = 400

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(
            words[i:i + chunk_size]
        )

        chunks.append(chunk)

    summaries = []

    for chunk in chunks:

        prompt = (
            "Write a concise 2 to 3 sentence summary "
            "of this news article. Include the main event, "
            "important details, and outcome:\n\n"
            + chunk
        )

        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            max_length=512,
            truncation=True
        )

        summary_ids = summarization_model.generate(
            inputs["input_ids"],
            max_new_tokens=100,
            min_new_tokens=35,
            num_beams=4,
            length_penalty=1.2,
            early_stopping=True
        )

        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )

        summaries.append(summary)

    final_summary = " ".join(summaries)

    return final_summary


# =========================================================
# SENTIMENT ANALYSIS
# =========================================================

def analyze_sentiment(article):

    result = sentiment_analyzer(article)

    label = result[0]["label"]

    confidence = result[0]["score"]

    return label, confidence


# =========================================================
# CLEAR FUNCTION
# =========================================================

def clear_article():

    st.session_state.article_input = ""


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
"""
<div class="hero">
<div class="hero-title">AI News Analyzer</div>
<div class="hero-subtitle">Transform lengthy news articles into concise summaries and understand their sentiment using AI-powered NLP.</div>
</div>
""",
unsafe_allow_html=True
)


# =========================================================
# INPUT LABEL
# =========================================================

st.markdown(
"""
<div class="section-label">Enter your news article</div>
""",
unsafe_allow_html=True
)


# =========================================================
# TEXT AREA
# =========================================================

article = st.text_area(
    label="Article",
    placeholder="Paste your news article here...",
    height=300,
    key="article_input",
    label_visibility="collapsed"
)


# =========================================================
# ARTICLE STATISTICS
# =========================================================

if article:

    word_count = len(article.split())
    character_count = len(article)

    st.caption(
        f"Characters: {character_count}  |  Words: {word_count}"
    )


# =========================================================
# BUTTONS
# =========================================================

col1, col2 = st.columns(2)


with col1:

    analyze_button = st.button(
        "🔍 Analyze Article",
        type="primary",
        use_container_width=True
    )


with col2:

    clear_button = st.button(
        "🗑️ Clear",
        type="secondary",
        use_container_width=True,
        on_click=clear_article
    )


# =========================================================
# ANALYZE ARTICLE
# =========================================================

if analyze_button:

    # -----------------------------------------------------
    # EMPTY ARTICLE
    # -----------------------------------------------------

    if not article.strip():

        st.warning(
            "⚠️ Please enter a news article."
        )


    # -----------------------------------------------------
    # ARTICLE TOO SHORT
    # -----------------------------------------------------

    elif len(article.split()) < 20:

        st.warning(
            "⚠️ Please enter a longer article "
            "(at least 20 words)."
        )


    # -----------------------------------------------------
    # PROCESS ARTICLE
    # -----------------------------------------------------

    else:

        try:

            # =============================================
            # PREPROCESSING
            # =============================================

            clean_article = preprocess_text(
                article
            )


            # =============================================
            # GENERATE SUMMARY
            # =============================================

            with st.spinner(
                "🤖 Generating AI summary..."
            ):

                summary = summarize_text(
                    clean_article
                )


            # =============================================
            # SENTIMENT ANALYSIS
            # =============================================

            with st.spinner(
                "📊 Analyzing sentiment..."
            ):

                sentiment, confidence = analyze_sentiment(
                    clean_article
                )


            # =============================================
            # SUCCESS MESSAGE
            # =============================================

            st.success(
                "✅ Analysis completed successfully!"
            )


            # =============================================
            # SUMMARY CARD
            # =============================================

            safe_summary = escape(summary)

            st.markdown(
f"""
<div class="result-card">
<div class="section-label">📄 AI Generated Summary</div>
<div class="summary-text">{safe_summary}</div>
</div>
""",
unsafe_allow_html=True
            )


            # =============================================
            # SENTIMENT + CONFIDENCE
            # =============================================

            col1, col2 = st.columns(2)


            # =============================================
            # SENTIMENT CARD
            # =============================================

            with col1:

                st.markdown(
f"""
<div class="metric-card">
<div class="metric-title">😊 Sentiment</div>
<div class="metric-value">{sentiment}</div>
</div>
""",
unsafe_allow_html=True
                )


            # =============================================
            # CONFIDENCE CARD
            # =============================================

            with col2:

                st.markdown(
f"""
<div class="metric-card">
<div class="metric-title">📊 Confidence</div>
<div class="metric-value">{confidence * 100:.2f}%</div>
</div>
""",
unsafe_allow_html=True
                )


        # =============================================
        # ERROR HANDLING
        # =============================================

        except Exception as e:

            st.error(
                "❌ Something went wrong while "
                "processing the article."
            )

            st.caption(
                f"Error details: {str(e)}"
            )