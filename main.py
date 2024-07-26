import customtkinter as ctk

class App():
    def __init__(self, window):
        self.window = window
        self.window.title("Julie's party hire shop")
        self.window.geometry("800x600")
        self.items = []

        self.create_widgets()
    
    def add_to_cart(self): ...
    def checkout(self): ...

    def create_widgets(self):
        frame = ctk.CTkFrame(self.window)
        frame.pack(padx=20, pady=20)
        gridFrame = ctk.CTkFrame(frame)
        gridFrame.pack()

        # Labels
        customerName = ctk.CTkLabel(gridFrame, text="Customer Name:")
        itemName = ctk.CTkLabel(gridFrame, text="Item Name:")
        quantity = ctk.CTkLabel(gridFrame, text="Quantity:")

        # Inputs
        self.customerNameEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter name")
        self.itemNameEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter item name")
        self.quantityEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter quantity")

        # Buttons
        addToCart = ctk.CTkButton(frame, text="Add to Cart", command=self.add_to_cart)
        checkout = ctk.CTkButton(frame, text="Checkout", command=self.checkout)

        # Place on screen for mainloop to utilize (sticky = "E" for aligning on the right)
        customerName.grid(row=0, column=0, padx=10, pady=10, sticky="E")
        itemName.grid(row=1, column=0, padx=10, pady=10, sticky="E")
        quantity.grid(row=2, column=0, padx=10, pady=10, sticky="E")
 
        # Sticky = "W" for aligning on the left
        self.customerNameEntry.grid(row=0, column=1, padx=10, pady=10, sticky="W")
        self.itemNameEntry.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        self.quantityEntry.grid(row=2, column=1, padx=10, pady=10, sticky="W")

        # Pack the buttons outside the grid frame
        addToCart.pack(padx=10, pady=10)
        checkout.pack(padx=10, pady=10)
    
if __name__ == "__main__":
    window = ctk.CTk()
    app = App(window)
    window.mainloop()