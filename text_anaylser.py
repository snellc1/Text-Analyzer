# Function to get text and determine word, character, vowel and punctuation count.
def get_text():
    """Get text or paragraph from users. """
    text = input("Please begin typing: ")
    word_count(text)
    char_count(text)
    vowel_count(text)
    pun_count(text)

def word_count(text):
    """Count the total amount of words in provide text."""
    words = text.split()
    total_words = len(words)
    print(f'Word Count: {total_words}')
    
def char_count(text):
    """Counts the total amount of characters in a provide text. """
    chars = []
    for c in text:
        if c != ' ':
            chars.append(c)
    
    total_char = len(chars)
    print(f'Character Count: {total_char}')

def vowel_count(text):
    """Count the total amount of vowels in provide text."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    total_vowels = 0
    for l in text:
        if l.lower() in vowels:
            total_vowels += 1
       
    
    print(f'Vowel Count: {total_vowels}')

def pun_count(text):
    """Count the total amount of punctuations in provide text."""
    puns = [ '!', ',', '.', '-', ';', ':', '`']
    total_puns = 0
    for p in text:
        if p in puns:
            total_puns += 1

    print(f'Punctuation Count: {total_puns}')
get_text()
