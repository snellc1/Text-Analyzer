from tkinter import * 
text_anaylzer = Tk()

#App Title
text_anaylzer.title("Text Analyzer")

#Setting the window size
text_anaylzer.geometry("800x600")

#Declaring string variable for provide text
input_text = StringVar()

#Creating entry label
entry_lb = Label(text_anaylzer, text= "Please provide text:")

#Creating Entry
entry = Entry(text_anaylzer, textvariable=input_text, font=('calibre', 10, 'normal'))

#Placing label and entry 
entry.grid(row=0, column=1)
entry_lb.grid(row=0, column=0)

#Loop
text_anaylzer.mainloop()