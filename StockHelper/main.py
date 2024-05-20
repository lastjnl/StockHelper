from inventory import load_stock, save_stock, add_item, remove_item
from gui import StockHelperApp

import tkinter as tk

def main():
    root = tk.Tk()
    app = StockHelperApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()