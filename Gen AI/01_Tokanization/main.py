import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

inputText = "Hi there! My name is Bhuvaa Rutvik"
tokens = enc.encode(inputText)

# Tokens:  [12194, 1354, 0, 3673, 1308, 382, 418, 6916, 107541, 80390, 24590]
print("Tokens: ", tokens)

outputText = enc.decode([12194, 1354, 0, 3673, 1308, 382, 418, 6916, 107541, 80390, 24590])

print("Text: ", outputText)