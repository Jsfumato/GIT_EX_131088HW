from Tkinter import *

def callback():
	print 2
	button.configure(text="clicked!")

button = Button(None, text='button', command=callback)
button.pack()
mainloop()
