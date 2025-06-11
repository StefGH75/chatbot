from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

texts = [
    "Hello, how are you?",
    "I’m learning artificial intelligence.",
    "Hallo, wie geht es dir?",
    "Ich lerne künstliche Intelligenz.",
    "Datensicherheitsverordnung"
]

for text in texts:
    tokens = tokenizer.encode(text)
    print(f"Text: {text}")
    print(f"Anzahl Tokens: {len(tokens)}")
    print(f"Tokens: {tokens}\n")
