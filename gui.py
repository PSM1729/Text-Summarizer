#Main packages for gui
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog

#GUI window setup
root= Tk()
root.title("TEXT SUMMARYZER")
root.geometry("800x720")
root.config(background='lightgoldenrodyellow')

#TABS
tab_control=ttk.Notebook(root)

tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab3=ttk.Frame(tab_control)
tab4=ttk.Frame(tab_control)

#Adding tabs to notebook
tab_control.add(tab1, text=f'{"HOME":^20s}')
tab_control.add(tab2, text=f'{"FILE":^20s}')
tab_control.add(tab3, text=f'{"URL":^20s}')
tab_control.add(tab4, text=f'{"COMPARE":^20s}')


label1 = Label(tab1, text='Basic Summaryzer',padx=5, pady=5)
label1.place(x=350,y=5)

label2 = Label(tab2, text='File Processing',padx=5, pady=5)
label2.grid(column=1, row=0)

label3 = Label(tab3, text='URL Based Summarizer',padx=5, pady=5)
label3.place(x=350,y=5)

label4 = Label(tab4, text='Compare Summarizers',padx=5, pady=5)
label4.place(x=345,y=5)


tab_control.pack(expand=1, fill="both")

############################################# Main Summarizer menu widgets##############################################

###Functions for main menu
def clear_text_main():
    entry.delete('1.0',END)

def clear_textbox():
    tab1_display.delete('1.0', END)

#def basic_summarizer():



label_m=Label(tab1, text='ENTER THE TEXT', pady=5)
label_m.place(x=359,y=40)
entry=ScrolledText(tab1,height=13, width=93, padx=6, pady=5,state='normal')
entry.place(x=10,y=75)

#Summary TextBox
tab1_display = Text(tab1,height=19, width=95)
tab1_display.place(x=10, y=350)

#Buttons
button1=Button(tab1,text="Reset",command=lambda: [clear_textbox(),clear_text_main()], width=12,bg='#03A9F4',fg='#000')
button1.place(x=270,y=310)

button2=Button(tab1,text="Summarize",width=12,bg='#ced',fg='#000')
button2.place(x=450,y=310)


################################################## File processing Summarizer##########################################

###Function for file processing
def clear_text_file():
    displayed_file.delete('1.0',END)

def clear_textbox2():
    tab2_display_text.delete('1.0', END)

def open_files():
	file1 = tk.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)


displayed_file = ScrolledText(tab2,height=15,width=93)
displayed_file.grid(row=2,column=0, columnspan=3,padx=5,pady=3)

b0=Button(tab2,text="Open File",command=open_files, width=12,bg='#c5cae9')
b0.grid(row=3,column=0,padx=10,pady=10)

b1=Button(tab2,text="Reset",command=lambda: [clear_textbox2(),clear_text_file()], width=12,bg="#b9f6ca")
b1.grid(row=3,column=1,padx=10,pady=10)

b2=Button(tab2,text="Summarize", width=12,bg='#F5EABA',fg='#000')
b2.grid(row=3,column=2,padx=10,pady=10)

tab2_display_text = ScrolledText(tab2,height=20,width=93)
tab2_display_text.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


################################################## URL BASED SUMMARIZER#################################################

label_u= Label(tab3, text="Enter the url : ",pady=3)
label_u.place(x=50,y=40)

raw_ip=StringVar()
text_u=Entry(tab3,textvariable=raw_ip,font = ('calibre',10,'normal'),width=60)
text_u.place(x=150,y=40)
burl=Button(tab3,text="Get Text", width=12,bg='#0A0823',fg='#FEFEFE')
burl.place(x=600,y=35)

#Text from url
displayed_text = ScrolledText(tab3,height=15,width=95)
displayed_text.place(x=5,y=70)

#Buttons
button1_URL=Button(tab3,text="Reset", width=12,bg='#03A9F4',fg='#000')
button1_URL.place(x=270,y=330)

button2_URL=Button(tab3,text="Summarize",width=12,bg='#ced',fg='#000')
button2_URL.place(x=450,y=330)

#Displaying the result
tab3_display_text = ScrolledText(tab3,height=18,width=95)
tab3_display_text.place(x=5,y=370)


################################################## COMPARING SUMMARIZER#################################################

label_cmp=Label(tab4, text='ENTER THE TEXT', pady=5)
label_cmp.place(x=359,y=40)
entry_cmp=ScrolledText(tab4,height=13, width=93, padx=6, pady=5,state='normal')
entry_cmp.place(x=10,y=75)

#Buttons
button1_cmp=Button(tab4,text="Reset", width=12,bg='#FAA601',fg='#FFFECF')
button1_cmp.place(x=50,y=310)

button2_cmp=Button(tab4,text="NLTK Summarizer",width=20,bg='#7A01FA',fg='#FFFECF')
button2_cmp.place(x=310,y=310)

button3_cmp=Button(tab4,text="SpaCy Summarizer",width=20,bg='#FA0101',fg='#FFFECF')
button3_cmp.place(x=600,y=310)

#Summary TextBox
tab1_display_cmp = Text(tab4,height=19, width=95).place(x=10, y=350)


root.mainloop()


