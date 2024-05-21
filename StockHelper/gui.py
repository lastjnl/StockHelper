import tkinter as tk
from tkinter import W, IntVar, ttk, messagebox
from inventory import load_stock, save_stock, add_item, remove_item
from models.product import Product
from models.setting import Setting

class StockHelperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Helper")
        self.root.geometry("900x500")
        self.stock = load_stock('data/stock.json')
        self.settings = Setting.load_all_settings()

        # Create frames
        self.top_frame = tk.Frame(root)
        self.top_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.left_frame = tk.Frame(root);
        self.left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.right_frame = tk.Frame(root)
        self.right_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Configure grid weights to make the right frame expand
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(1, weight=1)

        # Adding elements to top frame
        self.sort_label = tk.Label(self.top_frame, text="Sort by: ")
        self.sort_label.pack(pady=5)
        sort_column_var = IntVar()
        self.sorting_button_name = tk.Radiobutton(self.top_frame, text="Name", variable=sort_column_var, value="name", command=self.update_setting)
        self.sorting_button_quantity = tk.Radiobutton(self.top_frame, text="Quantity", variable=sort_column_var, value="quantity", command=self.update_setting)
        self.sorting_button_name.pack()
        self.sorting_button_quantity.pack()

        # Adding elements to left frame
        self.search_label = tk.Label(self.left_frame, text="Search...")
        self.search_label.pack(pady=5)
        self.search_entry = tk.Entry(self.left_frame)
        self.search_entry.pack(pady=0)

        self.search_button = tk.Button(self.left_frame, text="Search", command=self.search)
        self.search_button.pack(pady=15)

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

        # Setting up treeview
        self.tree = ttk.Treeview(self.right_frame, columns=("Name","Quantity"), show="headings")
        self.tree.heading("Name", text="Name") 
        self.tree.heading("Quantity", text="Quantity")
        self.tree.column("Name", anchor=tk.CENTER)
        self.tree.column("Quantity", anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.populate_tree()

    def update_setting(self):
        return

    def search(self):
        search_term = self.search_entry.get()
        self.stock = load_stock('data/stock.json', search_term)
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