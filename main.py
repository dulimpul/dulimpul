#!/usr/bin/python

from tkinter import *

# mebuat kolom window
root =Tk()
root.geometry('250x250')
root.title('Cantatan mede in yusuf')

# membuat text box 
text = Text(root, font=('haveltical 15 bold'), bd=2)
text.focus()
text.pack()

 # membuat fungsi untuk perintah cut
 # pilihan texs

def cut_text():
    text.event_generate(('<<Cut>>'))

# mebuat fungsi mengcopy
# pilihan text
def copy_text():
    text.event_generate(('<<Copy>>'))

# membuat fungsi paste 

def paste_text():
    text.event_generate(('<<Paste>>'))

# membuat menubar
menu = Menu(root, tearoff= 0)
menu.add_command(label='Cut', command=cut_text)
menu.add_command(label='Paste', command=paste_text)
menu.add_command(label='Copy', command=copy_text)
menu.add_separator()
menu.add_command(label='Exit', command=root.destroy)


# mendifinisikan funsi popup
# cotex menu tombol klik kiri 

def context_menu(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()
    
# binding right click button to root
root.bind('<Button-3>', context_menu)
root.mainloop()
        