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
        self.setup_frame = tk.Frame(frame)
        self.setup_frame.grid(row=0, column=0)

        self.youtube_link_entry = tk.Entry(self.setup_frame, width=80)
        self.youtube_link_entry.insert(0, 'YouTube Link')
        self.youtube_link_entry.grid(row=0, column=0, columnspan=4, sticky=(tk.E, tk.W), pady=10)

        self.youtube_canvas_width_label = tk.Label(self.setup_frame, text='Width')
        self.youtube_canvas_width_label.grid(row=1, column=0, sticky=tk.E)

        self.youtube_canvas_width_entry = tk.Entry(self.setup_frame, width=20)
        self.youtube_canvas_width_entry.grid(row=1, column=1, sticky=tk.W)
        self.youtube_canvas_width_entry.insert(0, 'From input')
        self.youtube_canvas_width_entry.config(state='disabled')

        self.youtube_canvas_height_label = tk.Label(self.setup_frame, text='Height')
        self.youtube_canvas_height_label.grid(row=1, column=2, sticky=tk.E)
    
        self.youtube_canvas_height_entry = tk.Entry(self.setup_frame, width=20)
        self.youtube_canvas_height_entry.grid(row=1, column=3, sticky=tk.W)
        self.youtube_canvas_height_entry.insert(0, '100')

        self.youtube_run_button = tk.Button(self.setup_frame, text='Run', width=20)
        self.youtube_run_button.grid(row=2, column=0, columnspan=4, pady=10)
        