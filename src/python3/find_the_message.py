import re

# Read the text from a file
with open('data/assignment_2/paragraph.txt', 'r') as file:
    text = file.read()

# Split text into sentences using regex for sentence-ending punctuation
sentences = re.split(r'[.!?]\s+', text)
num_sentences = len(sentences)

# Print number of sentences
print(f"Number of sentences: {num_sentences}")

# Split text into words and clean punctuation
words = re.findall(r'\b\w+\b', text.lower())

# Count unique words using a set
unique_words = set(words)
num_unique_words = len(unique_words)

# Print number of unique words
print(f"Number of unique words: {num_unique_words}")

# Indices for hidden message
hidden_indices = [60, 26, 10, 10, 41, 35, 26, 44,48]

# Ensure the correct message by adjusting word extraction
hidden_message = ''.join([words[i][0].upper() for i in hidden_indices])

# Print the hidden message
print(f"Hidden message: {hidden_message}")