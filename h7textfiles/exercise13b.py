def remove_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""
    for ch in s:
        if ch not in vowels:
            result += ch
    return result


input_path = "Files Chapter 7/hamlet2.txt"
output_path = "Files Chapter 7/hamlet3.txt"

chars_read = 0
chars_written = 0

with open(input_path, "r", encoding="utf-8") as infile, \
     open(output_path, "w", encoding="utf-8") as outfile:

    for line in infile:            # read line-by-line
        chars_read += len(line)

        no_vowels = remove_vowels(line)
        chars_written += len(no_vowels)

        outfile.write(no_vowels)

print("Characters read:   ", chars_read)
print("Characters written:", chars_written)
