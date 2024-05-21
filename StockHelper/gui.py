from itertools import product
from queue import Empty
import tkinter as tk
from tkinter import ttk, messagebox
from inventory import load_stock, save_stock, add_item, remove_item
from models.product import Product

class StockHelperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Helper")
        self.root.geometry("900x500")
        self.stock = load_stock('data/stock.json')

        # Create frames
        self.left_frame = tk.Frame(root);
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.right_frame = tk.Frame(root)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Configure grid weights to make the right frame expand
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)

        self.name_label = tk.Label(self.left_frame, text="Name")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.left_frame)
        self.name_entry.pack(pady=5)

        self.quantity_label = tk.Label(self.left_frame, text="Quantity")
        self.quantity_label.pack(pady=5)
        self.quantity_entry = tk.Entry(self.left_frame)
        self.quantity_entry.pack(pady=5)

        self.add_button = tk.Button(self.left_frame, text="Add product", command=self.add_item)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.left_frame, text="Remove product", command=self.remove_item)
        self.remove_button.pack(pady=5)

        self.tree = ttk.Treeview(self.right_frame, columns=("Name","Quantity"), show="headings")
        self.tree.heading("Name", text="Name") 
        self.tree.heading("Quantity", text="Quantity")
        self.tree.column("Name", anchor=tk.CENTER)
        self.tree.column("Quantity", anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.populate_tree()

    def populate_tree(self):
        for item in self.tree.get_children():
            if item:
                self.tree.delete(item)
        if self.stock:
            for product in self.stock:
                self.tree.insert("", "end", values=(product.name, product.quantity))

    def add_item(self):
        try:
            name = self.name_entry.get()
            quantity = int(self.quantity_entry.get())
            product = Product(name, quantity)
            self.stock = add_item(self.stock, product)
            self.save_stock()
            self.populate_tree()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity")

    def remove_item(self):
        try:
            name = self.name_entry.get()
            quantity = int(self.quantity_entry.get())
            product = Product(name, quantity)
            self.stock = remove_item(self.stock, product)
            self.save_stock()
            self.populate_tree()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity")

    def save_stock(self):
        save_stock('data/stock.json', self.stock)

if __name__ == "__main__":
    root = tk.Tk()
    app = StockHelperApp(root)
    root.mainloop()