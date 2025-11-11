from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

reference = "Insulin resistance is when cells do not respond well to insulin."
prediction = "It happens when the body's cells stop responding properly to insulin."

ref_emb = model.encode([reference])
pred_emb = model.encode([prediction])

similarity = cosine_similarity(ref_emb,pred_emb)[0][0]

print(f"Similarity score : {similarity:.3f}")