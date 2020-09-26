import tkinter as tk

class SpectrumApp(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('960x550')

        self.main_frame = tk.Frame(master)

        self.create_menu(self.main_frame)
        master.config(menu=self.menubar)

        self.create_widgets()

    def create_menu(self, frame):
        self.menubar = tk.Menu(frame)

        spectrum_menu = tk.Menu(self.menubar, tearoff=0)
        spectrum_menu.add_command(label='File') #change to spectrum_menu.add_command(label='File', command=openFileDialog) or some shit
        spectrum_menu.add_command(label='Youtube') #Access youtube
        spectrum_menu.add_command(label='Movie') #Access IMDB database or some shit
        self.menubar.add_cascade(label='Spectrum', menu=spectrum_menu)

    def create_widgets(self):
        return