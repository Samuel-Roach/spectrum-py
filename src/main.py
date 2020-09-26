import tkinter as tk
from spectrum_gui import SpectrumApp

def main():
    #do some shit
    root = tk.Tk()
    app = SpectrumApp(master=root)
    app.mainloop()
    return

if __name__ == "__main__":
    main()