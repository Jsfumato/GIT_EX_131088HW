from Tkinter import *

def callback():
	print 1
	button.configure(text="clicked!")

button = Button(None, text='button', command=callback)
button.pack()
mainloop()
