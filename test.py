from groq import Groq

client = Groq(api_key="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")
models = client.models.list()
for m in models.data:
    print(m.id)
