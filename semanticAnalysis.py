from sentence_transformers import SentenceTransformer, util

# Load the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to encode the prompt and compare it with text chunks
def is_chunk_relevant(chunk, prompt, threshold=0.2):
    prompt_embedding = model.encode(prompt)
    chunk_embedding = model.encode(chunk)
    similarity = util.cos_sim(chunk_embedding, prompt_embedding)
    return similarity.item() > threshold  # Return True if similarity exceeds threshold
