"""

Build a Text Analysis Tool that performs the following operations on user input text:
Core Features:

1. Character Analysis:
    - Count total characters (with and without spaces)
    - Count vowels and consonants separately
    - Find most frequent character

2. Word Analysis:
    - Count total words
    - Find longest and shortest words
    - Count words starting with vowels vs consonants

3. String Transformations:
    - Convert to title case, upper case, lower case
    - Create acronym from first letter of each word
    - Reverse the entire string and each word individually
    
Example Result

Enter text: The Quick Brown Fox Jumps Over The Lazy Dog

=== TEXT ANALYSIS REPORT ===
Character Analysis:
- Total characters: 43 (with spaces), 35 (without spaces)
- Vowels: 12 (e, u, i, o, o, u, o, e, e, a, o)
- Consonants: 23
- Most frequent: 'o' (appears 4 times)

Word Analysis:
- Total words: 9
- Longest word: "Quick" (5 letters)
- Shortest word: "The" (3 letters)
- Words starting with vowels: 1 ("Over")
- Words starting with consonants: 8

Transformations:
- Title Case: The Quick Brown Fox Jumps Over The Lazy Dog
- Upper Case: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
- Lower Case: the quick brown fox jumps over the lazy dog
- Acronym: TQBFJOTLD
- Reversed Text: goD yzaL ehT revO spmuJ xoF nworB kciuQ ehT
- Words Reversed: ehT kciuQ nworB xoF spmuJ revO ehT yzaL goD

USE: len(), split(), count(), upper(), lower(), title(), slicing operations

"""
text = input("Enter text: ")
vowels = "aeiouAEIOU"
words = text.split()

# Character analysis
with_space = len(text)
without_space = len(text.replace(" ", ""))
vowel_list = [c for c in text if c in vowels]
vowel_count = len(vowel_list)
consonant_count = sum(1 for c in text if c.isalpha() and c not in vowels)
most_char = max(set(text.replace(" ", "")), key=text.count)
most_count = text.count(most_char)

# Word analysis
longest = max(words, key=len)
shortest = min(words, key=len)
start_vowel = sum(1 for w in words if w[0].lower() in vowels)
start_cons = len(words) - start_vowel

# Transformations
title_case = text.title()
upper_case = text.upper()
lower_case = text.lower()
acronym = "".join(w[0].upper() for w in words)
reversed_text = text[::-1]
words_reversed = " ".join(w[::-1] for w in words)

# Output
print("\n=== TEXT ANALYSIS REPORT ===")
print("Character Analysis:")
print(f"- Total characters: {with_space} (with spaces), {without_space} (without spaces)")
print(f"- Vowels: {vowel_count} ({', '.join(vowel_list)})")
print(f"- Consonants: {consonant_count}")
print(f"- Most frequent: '{most_char}' (appears {most_count} times)\n")

print("Word Analysis:")
print(f"- Total words: {len(words)}")
print(f"- Longest word: \"{longest}\" ({len(longest)} letters)")
print(f"- Shortest word: \"{shortest}\" ({len(shortest)} letters)")
print(f"- Words starting with vowels: {start_vowel}")
print(f"- Words starting with consonants: {start_cons}\n")

print("Transformations:")
print(f"- Title Case: {title_case}")
print(f"- Upper Case: {upper_case}")
print(f"- Lower Case: {lower_case}")
print(f"- Acronym: {acronym}")
print(f"- Reversed Text: {reversed_text}")
print(f"- Words Reversed: {words_reversed}")
