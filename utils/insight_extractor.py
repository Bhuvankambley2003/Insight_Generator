from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_insights(text):
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']