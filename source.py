from Tkinter import *

def callback():
	print 3
	print HelloWorld
	button.configure(text="clicked!")

button = Button(None, text='button', command=callback)
button.pack()
mainloop()
