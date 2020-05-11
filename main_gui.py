"""
Raspberry PIE
Kaveh Tehrani
"""

import datetime
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import reddit

class RPIE_GUI:
    def __init__(self, master, l_tz=None, num_max_clocks=20):
        self.master = master
        self.master.title('RPIE_TOUCH')

        self.frame = ttk.Frame()
        self.frame.pack()
        self.create_gui()
        self.r = reddit.rpie_reddit()
        self.wnd_joke = None

    def create_gui(self):
        self.l_entries = []
        self.l_dd = []

        self.l_name = ttk.Label(self.frame, text='Christie is a QT')
        self.l_name.grid(row=0, column=0)
        self.l_name = ttk.Label(self.frame, text='')
        self.l_name.grid(row=1, column=0)


        self.bt_update = ttk.Button(self.frame, text="Dad Joke!", command=self.gui_dad_joke)
        self.bt_update.grid(row=2, column=0, columnspan=1)

        self.bt_update = ttk.Button(self.frame, text="Smol!", command=self.gui_smolcat)
        self.bt_update.grid(row=3, column=0, columnspan=1)

    def gui_dad_joke(self):
        str_joke, str_punchline = self.r.get_dadjoke()
        self.pop_text_window(f"{str_joke}...\n\n{str_punchline}")

    def gui_smolcat(self):
        self.r.get_smol_cat()

    def pop_text_window(self, str_text):
        if self.wnd_joke:
            self.wnd_joke.destroy()

        self.wnd_joke = tk.Toplevel(self.master)
        l = ttk.Label(self.wnd_joke, text=str_text, wrap=250)
        l.grid(row=0, column=0)

if __name__ == '__main__':
    root = ThemedTk(themebg=True)
    app = RPIE_GUI(master=root)
    root.set_theme('radiance')
    root.iconbitmap(r'panda.ico')

    root.mainloop()
