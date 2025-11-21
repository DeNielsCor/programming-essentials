import re
import string

def normalize_punctuation_spacing(text: str) -> str:
    punct_class = re.escape(string.punctuation)
    text = re.sub(r'([' + punct_class + r']+)[ \t]+', r'\1 ', text)
    text = re.sub(r'([' + punct_class + r']+)([^\s\n])', r'\1 \2', text)
    return text

# Process the file
input_path  = 'Files Chapter 7/hamlet.txt'
output_path = 'Files Chapter 7/hamlet2.txt'

with open(input_path, 'r', encoding='utf-8') as inputfile:
    text = inputfile.read()

normalized = normalize_punctuation_spacing(text)

with open(output_path, 'w', encoding='utf-8') as outputfile:
    outputfile.write(normalized)

print("Done — wrote normalized text to:", output_path)
