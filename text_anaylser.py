from tkinter import * 
text_anaylzer = Tk()

#App Title
text_anaylzer.title("Text Analyzer")

#Setting the window size
text_anaylzer.geometry("600x400")

#Declaring string variable for provide text
input_text = StringVar()

#Creating entry labels
entry_lb = Label(text_anaylzer, text= "Please provide text")
word_label = Label(text_anaylzer, text="Word Count")
char_label = Label(text_anaylzer, text="Character Count")
vowel_label = Label(text_anaylzer, text="Vowel Count")
pun_label = Label(text_anaylzer, text="Punctuation Count")

#Creating entries
entry = Entry(text_anaylzer, textvariable=input_text, width=50, font=('calibre', 10, 'normal'))
word_entry = Entry(text_anaylzer)
char_entry = Entry(text_anaylzer)
vowel_entry = Entry(text_anaylzer)
pun_entry = Entry(text_anaylzer)

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
    
    #Display word count
    word_entry.insert(0,f"{total_words}")
    
def char_count(text):
    """Counts the total amount of characters in a provide text. """
    chars = []
    for c in text:
        if c != ' ':
            chars.append(c)
    
    total_char = len(chars)
    
    #Display character count
    char_entry.insert(0, f"{total_char}")


def vowel_count(text):
    """Count the total amount of vowels in provide text."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    total_vowels = 0
    for l in text:
        if l.lower() in vowels:
            total_vowels += 1
       
    #Display vowel count
    vowel_entry.insert(0, f"{total_vowels}")

def pun_count(text):
    """Count the total amount of punctuations in provide text."""
    puns = [ '!', ',', '.', '-', ';', ':', '`']
    total_puns = 0
    for p in text:
        if p in puns:
            total_puns += 1
    
    pun_entry.insert(0, f"{total_puns}")

   
#Creating Anaylzer Button
anaylze_button = Button(text_anaylzer, text="Anaylze", command= get_text)

#Placing labels and entries 
entry_lb.pack(pady=5)
entry.pack(pady=5)
anaylze_button.pack(pady=5)
word_label.pack(pady=5)
word_entry.pack(pady=5)
char_label.pack(pady=5)
char_entry.pack(pady=5)
vowel_label.pack(pady=5)
vowel_entry.pack(pady=5)
pun_label.pack(pady=5)
pun_entry.pack(pady=5)

#Loop
text_anaylzer.mainloop()