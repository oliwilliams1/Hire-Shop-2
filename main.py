import customtkinter as ctk

items = {}
recieptIDs = []

def error_window(errorMessage : str):
    errorWindow = ctk.CTk()
    errorWindow.title("Error")
    errorWindow.geometry("300x50")
    errorWindow.resizable(False, False)

    errorLabel = ctk.CTkLabel(errorWindow, text=errorMessage, font=("Arial", 18))
    errorLabel.pack(anchor="center", pady=10)

    errorWindow.mainloop()

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
    
    def checkout(self):
        # Check if boxes are not empty
        if self.customerNameEntry.get() == "":
            error_window("Please enter a customer name")
            return
        
        if self.recieptIDEntry.get() == "":
            error_window("Please enter a reciept ID")
            return

        if self.itemNameEntry.get() == "":
            error_window("Please enter an item name")
            return
        
        if self.priceEntry.get() == "":
            error_window("Please enter a price")
            return
        
        if self.quantityEntry.get() == "":
            error_window("Please enter a quantity")
            return

        # Checking if types are correct
        try: 
            int(self.recieptIDEntry.get())
        except:
            error_window("Please enter a valid reciept ID")
            return

        try:
            int(self.quantityEntry.get())
        except:
            error_window("Please enter a valid quantity")
            return
        
        try:
            float(self.priceEntry.get())
        except:
            error_window("Please enter a valid price")
            return
        
        # Check if reciept ID is already in the list
        if self.recieptIDEntry.get() in items.keys():
            error_window("Reciept ID already exists")
            return
        
        # All checks are a sucssess!
        int(self.quantityEntry.get())
        price = float(self.priceEntry.get())
        recieptId = int(self.recieptIDEntry.get())
        items[str(recieptId)] = Item(self.itemNameEntry.get(), price, self.quantityEntry.get(), self.customerNameEntry.get())

        # Delete entries, fresh for a new input
        self.customerNameEntry.delete(0, ctk.END)
        self.recieptIDEntry.delete(0, ctk.END)
        self.itemNameEntry.delete(0, ctk.END)
        self.priceEntry.delete(0, ctk.END)
        self.quantityEntry.delete(0, ctk.END)

        # Update the reciept viewer via the instance
        self.recieptInstance.update_widgets()

    def create_widgets(self):
        gridFrame = ctk.CTkFrame(self.frame)
        gridFrame.pack()

        # Labels
        customerName = ctk.CTkLabel(gridFrame, text="Customer Name:")
        recieptId = ctk.CTkLabel(gridFrame, text="Reciept ID:")
        itemName = ctk.CTkLabel(gridFrame, text="Item Name:")
        price = ctk.CTkLabel(gridFrame, text="Price:")
        quantity = ctk.CTkLabel(gridFrame, text="Quantity:")

        # Inputs
        self.customerNameEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter name")
        self.recieptIDEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter reciept ID")
        self.itemNameEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter item name")
        self.priceEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter price")
        self.quantityEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter quantity")

        # Buttons
        checkout = ctk.CTkButton(self.frame, text="Hire", command=self.checkout)

        # Place on screen for mainloop to utilize (sticky = "E" for aligning on the right)
        customerName.grid(row=0, column=0, padx=10, pady=10, sticky="E")
        recieptId.grid(row=1, column=0, padx=10, pady=10, sticky="E")
        itemName.grid(row=2, column=0, padx=10, pady=10, sticky="E")
        price.grid(row=3, column=0, padx=10, pady=10, sticky="E")
        quantity.grid(row=4, column=0, padx=10, pady=10, sticky="E")
 
        # Sticky = "W" for aligning on the left
        self.customerNameEntry.grid(row=0, column=1, padx=10, pady=10, sticky="W")
        self.recieptIDEntry.grid(row=1, column=1, padx=10, pady=10, sticky="W")
        self.itemNameEntry.grid(row=2, column=1, padx=10, pady=10, sticky="W")
        self.priceEntry.grid(row=3, column=1, padx=10, pady=10, sticky="W")
        self.quantityEntry.grid(row=4, column=1, padx=10, pady=10, sticky="W")

        # Pack the buttons outside the grid frame
        checkout.pack(padx=10, pady=10)

def calculateTotalPrice(item : Item) -> float:
    return float(item.price) * float(item.quantity)

def make_reciept_entry(reciept_id : str, item : Item) -> str:
    tempStr = ""
    tempStr += f"Reciept ID: {reciept_id}\n"
    tempStr += f"Customer Name: {item.customer_name}\n"
    tempStr += f"Item: {item.name}\n"
    tempStr += f"Price: ${item.price}\n"
    tempStr += f"Quantity: {item.quantity}\n"
    tempStr += f"Total Price: ${calculateTotalPrice(item)}\n\n"
    return tempStr

class Reciept:
    def __init__(self, frame):
        self.frame = frame
        self.create_reciept_widgets()
    
    def create_reciept_widgets(self):
        self.reciept = ctk.CTkTextbox(self.frame, width=300, height=240)
        self.reciept.insert(ctk.END, "No items on hire")
        self.reciept.configure(state="disabled")
        self.reciept.pack()

    def update_widgets(self):
        self.reciept.configure(state="normal")
        self.reciept.delete("1.0", ctk.END)
        
        tempStr = ""
        for key in items.keys():
            value = items[key]
            tempStr += make_reciept_entry(key, value)

        self.reciept.insert(ctk.END, tempStr)

        self.reciept.configure(state="disabled")

        print(tempStr)

class EntryRemover():
    def __init__(self, frame, recieptInstance):
        # Initialize variables
        self.frame = frame
        self.create_widgets()
        self.recieptInstance = recieptInstance

    def remove_entry(self):
        try:
            # Delete the entry from the dictionary
            del items[self.entry.get()]

        except:
            # If failed, the reicept ID doesnt exist in that dictionary so throw an error window
            error_window("Invalid Reciept ID")    

        # Update reciept viewer
        self.recieptInstance.update_widgets()

        # Remove any text in the entry fresh for new input
        self.entry.delete(0, ctk.END)

    def create_widgets(self):
        label = ctk.CTkLabel(self.frame, text="Remove entry by Reciept ID")
        label.pack(padx=10, pady=10)
        self.entry = ctk.CTkEntry(self.frame, width=200, height=30, placeholder_text="Enter Reciept ID")
        self.entry.pack(padx=10, pady=10)

        self.remove_button = ctk.CTkButton(self.frame, text="Remove", command=self.remove_entry)
        self.remove_button.pack(padx=10, pady=10)

if __name__ == "__main__":
    window = ctk.CTk()
    window.title("Julie's party hire shop")
    window.geometry("865x310")

    rectieptFrame = ctk.CTkFrame(window, width=300, height=200)
    rectieptFrame.grid(row=0, column=1, padx=10, pady=10)
    recieptInstance = Reciept(rectieptFrame)

    userInputFrame = ctk.CTkFrame(window, width=300, height=200)
    userInputFrame.grid(row=0, column=0, padx=10, pady=10)
    userInputInstance = UserInput(userInputFrame, recieptInstance)

    recieptRemoverFrame = ctk.CTkFrame(window, width=300, height=200)
    recieptRemoverFrame.grid(row=0, column=3, padx=10, pady=10)
    recieptRemoverInstance = EntryRemover(recieptRemoverFrame, recieptInstance)
    window.mainloop()