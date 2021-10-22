from tkinter import * 

text_anaylzer = Tk()

#App Title
text_anaylzer.title("Text Analyzer")

#Setting the window size
text_anaylzer.geometry("600x400")

Label(text_anaylzer, text="Please enter text").grid(row=0)

entry = Entry(text_anaylzer)

text_anaylzer.mainloop()