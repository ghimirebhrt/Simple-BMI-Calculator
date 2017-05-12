from Tkinter import *
import webbrowser

results = [0,]
global results

class Page(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
	def show(self):
		self.lift()


class resultpage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		self.config(background = 'white')
		bmilabel = Label(self, bg = 'white')
		bmilabel.pack()

		comment = Label(self, bg = 'white')
		comment.pack()

		global bmilabel
		global comment

		b = Label(self, text = "Go Back", cursor = 'hand2', fg = 'blue', bg = 'white')
		b.pack()
		b.place(y = 50, x = 170)

		b.bind("<Button-1>", self.goback)

		close = Label(self, text = "Close", cursor = 'hand2', fg = 'red', bg = 'white')
		close.pack()
		close.place(x = 180, y = 80)

		close.bind("<Button-1>", self.close)

	def close(self, event):
		root.destroy()


	def update(self):
		if(results[0] == 'Error'):
			bmilabel['text'] = "Error"
		else:
			bmilabel['text'] = "BMI = "+str(round(results[0], 2))

			if(results[0] < 18.0):
				comment['text'] = "You are under weight."
				comment['fg'] = 'red'
			elif(results[0] >= 18.0 and results[0] <= 25.0):
				comment['text'] = "You are fit."
				comment['fg'] = 'green'
			else:
				comment['text'] = "You are over weight."
				comment['fg'] = 'red'

	def goback(self, event):
		hp.show()

class homepage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		self.config(background = 'white')
		label = Label(self, text = "Weight in Kg", bg = 'white')
		label.pack()

		entry = Entry(self)
		entry.pack()

		label1 = Label(self, text = "Height in meters", bg = 'white')
		label1.pack()

		entry1 = Entry(self)
		entry1.pack()

		global entry
		global entry1

		b = Label(self, text = "Calculate BMI", cursor = 'hand2', fg = 'blue', bg = 'white')
		b.pack(pady = 10)

		b.bind("<Button-1>", self.calc_bmi)

		clr = Label(self, text = "Clear entries", cursor = 'hand2', fg = 'blue', bg = 'white')
		clr.pack(pady = 5)

		clr.bind("<Button-1>", self.clear)

		close = Label(self, text = "Close", cursor = 'hand2', fg = 'red', bg = 'white')
		close.pack(pady = 5)

		close.bind("<Button-1>", self.close)

	def close(self, event):
		root.destroy()

	def calc_bmi(self, event):

		try:

			wt = float(entry.get())
			ht = float(entry1.get())

			bmi = wt*(ht**(-2))
			results[0] = bmi
		except:
			results[0] = "Error"

		rpage.update()
		rpage.show()

	def clear(self, event):
		entry1.delete(0, END)
		entry.delete(0, END)


class MainView(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)

		hp = homepage(self)
		rpage = resultpage(self)

		global hp
		global rpage

		container = Frame(self)
		container.pack(side = 'top', fill = 'both', expand = True)

		hp.place(in_ = container, x = 0, y = 0, relwidth = 1, relheight = 1)
		rpage.place(in_ = container, x = 0, y = 0, relwidth = 1, relheight = 1)

		hp.show()

def open_src():
	webbrowser.open("http://www.github.com/hmnhGeek/bmigui")

if __name__ == '__main__':
	root = Tk()
	global root
	main = MainView(root)
	main.pack(side="top", fill="both", expand=True)
	root.wm_geometry("400x200")
	root.resizable(height = 0, width = 0)
	root.title("BMI Calculator")

	menubar = Menu(root, bg = 'white', activebackground = 'white', activeforeground = 'blue')
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Source Code", command=open_src)
	filemenu.add_separator()
	filemenu.add_command(label="Close", command=root.destroy)
	menubar.add_cascade(label="File", menu=filemenu)
	root.config(menu = menubar)

	root.mainloop()