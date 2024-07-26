import customtkinter as ctk

items = {}

class Item():
    def __init__(self, name, price, quantity, customer_name):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.customer_name = customer_name

class UserInput():
    def __init__(self, frame, recieptInstance):
        self.frame = frame
        self.recieptInstance = recieptInstance

        self.create_widgets()
    
    def add_to_cart(self):
        # Check if quantity is a valid input
        
        try:
            int(self.quantityEntry.get())
            price = float(self.priceEntry.get())

            recieptId = len(items.keys()) + 1
            items[str(recieptId)] = Item(self.itemNameEntry.get(), price, self.quantityEntry.get(), self.customerNameEntry.get())

            self.customerNameEntry.delete(0, ctk.END)
            self.itemNameEntry.delete(0, ctk.END)
            self.priceEntry.delete(0, ctk.END)
            self.quantityEntry.delete(0, ctk.END)

        except:
            errorWindow = ctk.CTk()
            errorWindow.title("Error")
            errorWindow.geometry("200x50")
            errorWindow.resizable(False, False)

            errorLabel = ctk.CTkLabel(errorWindow, text="Invalid quantity or price!", font=("Arial", 18))
            errorLabel.pack(anchor="center", pady=10)

            errorWindow.mainloop()

        
    def checkout(self):
        self.recieptInstance.update_widgets()

    def create_widgets(self):
        gridFrame = ctk.CTkFrame(self.frame)
        gridFrame.pack()

        # Labels
        customerName = ctk.CTkLabel(gridFrame, text="Customer Name:")
        itemName = ctk.CTkLabel(gridFrame, text="Item Name:")
        price = ctk.CTkLabel(gridFrame, text="Price:")
        quantity = ctk.CTkLabel(gridFrame, text="Quantity:")

        # Inputs
        self.customerNameEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter name")
        self.itemNameEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter item name")
        self.priceEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter price")
        self.quantityEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter quantity")

        # Buttons
        addToCart = ctk.CTkButton(self.frame, text="Add to Cart", command=self.add_to_cart)
        checkout = ctk.CTkButton(self.frame, text="Checkout", command=self.checkout)

        # Place on screen for mainloop to utilize (sticky = "E" for aligning on the right)
        customerName.grid(row=0, column=0, padx=10, pady=10, sticky="E")
        itemName.grid(row=1, column=0, padx=10, pady=10, sticky="E")
        price.grid(row=2, column=0, padx=10, pady=10, sticky="E")
        quantity.grid(row=3, column=0, padx=10, pady=10, sticky="E")
 
        # Sticky = "W" for aligning on the left
        self.customerNameEntry.grid(row=0, column=1, padx=10, pady=10, sticky="W")
        self.itemNameEntry.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        self.priceEntry.grid(row=2, column=1, padx=10, pady=10, sticky="W")
        self.quantityEntry.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        # Pack the buttons outside the grid frame
        addToCart.pack(padx=10, pady=10)
        checkout.pack(padx=10, pady=10)

class Reciept:
    def __init__(self, frame):
        self.frame = frame
        self.create_reciept_widgets()
    
    def create_reciept_widgets(self):
        self.reciept = ctk.CTkTextbox(self.frame, width=300, height=200)
        self.reciept.insert(ctk.END, "Receipt")
        self.reciept.configure(state="disabled")
        self.reciept.pack()

    def update_widgets(self):
        self.reciept.configure(state="normal")
        self.reciept.delete("1.0", ctk.END)
        
        tempStr = ""
        for key in items.keys():
            value = items[key]
            tempStr += f"Reciept ID: {key}\nCustomer Name: {value.customer_name}\nItem: {value.name}\nPrice: {value.price}\nQuantity: {value.quantity}\n\n"

        self.reciept.insert(ctk.END, tempStr)

        self.reciept.configure(state="disabled")

        print(tempStr)

if __name__ == "__main__":
    window = ctk.CTk()
    window.title("Julie's party hire shop")
    window.geometry("800x600")

    rectieptFrame = ctk.CTkFrame(window, width=300, height=200)
    rectieptFrame.grid(row=0, column=1, padx=10, pady=10)
    recieptInstance = Reciept(rectieptFrame)

    userInputFrame = ctk.CTkFrame(window, width=300, height=200)
    userInputFrame.grid(row=0, column=0, padx=10, pady=10)
    userInputInstance = UserInput(userInputFrame, recieptInstance)
    window.mainloop()

# TODO: Rename add to cart to checkout, remove checkout. add an admin place to remove orders via reciept ID.