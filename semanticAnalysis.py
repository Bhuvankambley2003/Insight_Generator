from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('all-MiniLM-L6-v2')

def is_chunk_relevant(chunk, prompt, threshold=0.2):
    prompt_embedding = model.encode(prompt)
    chunk_embedding = model.encode(chunk)
    similarity = util.cos_sim(chunk_embedding, prompt_embedding)
    return similarity.item() > threshold 
