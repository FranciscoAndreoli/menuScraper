
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Web Scraper')
        self.geometry('300x200')
    
        # Web Page Combobox
        self.lbl_webpage = tk.Label(self, text="Web Page:")
        self.lbl_webpage.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        
        self.combo_webpage = ttk.Combobox(self, state='readonly')
        self.combo_webpage.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self.combo_webpage['values'] = ["Uber Eats", "Deliveroo", "Just Eat", "Glovo"]
        self.combo_webpage.set("Uber Eats")

         # Browser Combobox
        self.lbl_browser = tk.Label(self, text="Browser:")
        self.lbl_browser.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        
        self.combo_browser = ttk.Combobox(self, state='readonly')
        self.combo_browser.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
        self.combo_browser['values'] = ["Chrome", "Firefox", "Edge"]
        self.combo_browser.set("Chrome")
        
        # Link Entry
        self.lbl_link = tk.Label(self, text="Link:")
        self.lbl_link.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        
        self.entry_link = tk.Entry(self)
        self.entry_link.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        
        # Scrap Button
        self.btn_scrap = tk.Button(self, text="Scrap")
        self.btn_scrap.grid(row=4, column=0, columnspan=2, pady=10)

        # Configure the grid
        self.grid_columnconfigure(1, weight=1)

    def displayMessage(self, messageType, message):
        messagebox.showerror(messageType, message)
