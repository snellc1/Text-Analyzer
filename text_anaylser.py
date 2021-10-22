from tkinter import * 
text_anaylzer = Tk()

#App Title
text_anaylzer.title("Text Analyzer")

#Setting the window size
text_anaylzer.geometry("300x150")

#Declaring string variable for provide text
input_text = StringVar()

#Creating entry label
entry_lb = Label(text_anaylzer, text= "Please provide text:")

#Creating Entry
entry = Entry(text_anaylzer, textvariable=input_text, font=('calibre', 10, 'normal'))

# Function to get text and determine word, character, vowel and punctuation count.
def get_text():
    """Get text or paragraph from users. """
    text = input_text.get()
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

#Creating Anaylzer Button
anaylze_button = Button(text_anaylzer, text="Anaylze", command= get_text)


#Placing label and entry 
entry.grid(row=1, column=1)
entry_lb.grid(row=1, column=0)
anaylze_button.grid(row=2, column=1)

#Loop
text_anaylzer.mainloop()