import tkinter as tk

class SpectrumApp(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('960x550')

        self.main_frame = tk.Frame(master)
        self.main_frame.grid(row=0, column=0)

        self.create_menu(self.main_frame)
        master.config(menu=self.menubar)

        self.create_youtube_widgets(self.main_frame)

    def create_menu(self, frame):
        self.menubar = tk.Menu(frame)

        spectrum_menu = tk.Menu(self.menubar, tearoff=0)
        spectrum_menu.add_command(label='File') #change to spectrum_menu.add_command(label='File', command=openFileDialog) or some shit
        spectrum_menu.add_command(label='Youtube') #Access youtube
        spectrum_menu.add_command(label='Movie') #Access IMDB database or some shit
        self.menubar.add_cascade(label='Spectrum', menu=spectrum_menu)

    def create_youtube_widgets(self, frame):
        self.link_frame = tk.Frame(frame)
        self.link_frame.grid(row=0, column=0)

        self.youtube_link_entry = tk.Entry(self.link_frame, width=80)
        self.youtube_link_entry.insert(0, "YouTube Link")
        self.youtube_link_entry.grid(row=0, column=0, sticky=(tk.E, tk.W))

        self.youtube_find_button = tk.Button(self.link_frame, text="Find", width=8)
        self.youtube_find_button.grid(row=0, column=1, padx=5)

        