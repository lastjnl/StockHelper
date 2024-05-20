import tkinter as tk
from tkinter import messagebox
from inventory import load_stock, save_stock, add_item, remove_item

class StockHelperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Helper")
        self.root.geometry("900x500")
        self.stock = load_stock('data/stock.json')

        self.item_label = tk.Label(root, text="Item")
        self.item_label.pack()
        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        self.quantity_label = tk.Label(root, text="Quantity")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Item", command=self.remove_item)
        self.remove_button.pack()

        self.show_button = tk.Button(root, text="Show Stock", command=self.show_stock)
        self.show_button.pack()

        self.save_button = tk.Button(root, text="Save", command=self.save_stock)
        self.save_button.pack()

    def add_item(self):
        item = self.item_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            self.stock = add_item(self.stock, item, quantity)
            messagebox.showinfo("Success", f"Added {quantity} of {item}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity")

    def remove_item(self):
        item = self.item_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            self.stock = remove_item(self.stock, item, quantity)
            messagebox.showinfo("Success", f"Removed {quantity} of {item}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity")

    def show_stock(self):
        stock_str = '\n'.join([f"{item}: {quantity}" for item, quantity in self.stock.items()])
        messagebox.showinfo("Stock", stock_str if stock_str else "Stock is empty")

    def save_stock(self):
        save_stock('data/stock.json', self.stock)
        messagebox.showinfo("Success", "Stock saved successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockHelperApp(root)
    root.mainloop()