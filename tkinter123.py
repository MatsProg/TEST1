import tkinter as tk
from tkinter.ttk import *

UPDATE_RATE = 1
class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.updater()
		# self.create_widgets()
		# self.Progressbar1(22)
	def add(a):
		# returning sum of a and b
		return a

	def updater(self):
		self.add()
		self.after(UPDATE_RATE, self.updater)

	def create_widgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Hello World\n(click me)"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")

		self.quit = tk.Button(self, text="QUIT", fg="red",
		                      command=self.master.destroy)
		self.quit.pack(side="bottom")

	def Progressbar1(self, w):
		self.paa1 = Progressbar(root, orient="horizontal", length=600, mode="determinate")
		self.paa1.pack()

		self.paa1['value'] = Application.add(w)

	def say_hi(self):
		print("hi there, everyone!")


		# app.Upd(4)
		#app.Progressbar1()


root = tk.Tk()

#app = Application(master=root)

#app.Progressbar1(55)
#app.mainloop()
"""

app = Application(master=root)
#app.Upd(4)
app.Progressbar1()
app.mainloop()
"""
