import evaluate

bertscore = evaluate.load("bertscore")

reference =  ["Insulin resistance is when cells do not respond well to insulin."]
prediction = ["It happens when the body's cells stop responding properly to insulin."]

results = bertscore.compute(predictions=prediction, references = reference,lang="en")

print(f"bertscore F1:{results['f1'][0]:.3f}")