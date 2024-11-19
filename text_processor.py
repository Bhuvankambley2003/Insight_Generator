import re

def preprocess_text(text):

    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,!?]', '', text)
    return text

def split_into_chunks(text, chunk_size=3):

    sentences = text.split('.')
    return ['. '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
