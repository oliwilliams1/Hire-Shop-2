import customtkinter as ctk
from PIL import Image
import random

# To install Libraries run the following commands in your terminal
# pip install customtkinter
# pip install pillow
# If there is a problem with pip, consault me

# Global variables
MAIN_WINDOW_WIDTH = 865
MAIN_WINDOW_HEIGHT = 370
PDG = 10 # Padding, all padding is the same because of my theme
GST = 0.15

items = {} # Stored as string RecieptID : Item class\
itemHistory = [] # No item gets deleted from here, it is a full history

# I use classes instead of multidimensional arrays as they are more efficient, appliccable and easier to use
class Item(): # A class holding neccassary data of an item
    def __init__(self, name, price, quantity, customer_name):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.customer_name = customer_name

# Helpfer function, returns the total price of an item from the Item class
def calculateTotalPrice(item : Item) -> float:
    return float(item.price) * float(item.quantity)

# Helper function, gets an item and makes a readable reciept from the class
def make_reciept_entry(reciept_id : str, item : Item) -> str:
    # Create a string to store the reciept entry
    # "\n" = new line
    recieptId_s = f"Reciept ID: {reciept_id}"
    customerName_s = f"Customer Name: {item.customer_name}"
    item_s = f"Item: {item.name}"
    price_s = f"Price: ${item.price:.2f}"
    quantity_s = f"Quantity: {item.quantity}"
    totalPrice_s = f"Total Price: ${calculateTotalPrice(item):.2f}"
    print(f"{recieptId_s}\n{customerName_s}\n{item_s}\n{price_s}\n{quantity_s}\n{totalPrice_s}\n\n")
    return f"{recieptId_s}\n{customerName_s}\n{item_s}\n{price_s}\n{quantity_s}\n{totalPrice_s}\n\n"

# An error window class to have a pop up with whatever error
def error_window(errorMessage : str):
    # Initialize a new window with correct settings
    errorWindow = ctk.CTk()
    errorWindow.title("Error")
    errorWindow.geometry("350x50")
    errorWindow.resizable(False, False)

    # Make a simple label storing the error message passed into the function
    errorLabel = ctk.CTkLabel(errorWindow, text=errorMessage, font=("Arial", 18))
    errorLabel.pack(anchor="center", pady=PDG)

    # Run mainloop to display the window until closed
    errorWindow.mainloop()

# Gets the total of all items in item history
def getTotal() -> float:
    price = 0
    for item in itemHistory:
        price += calculateTotalPrice(item)
    return price

def generate_example_data():
    # Set a few variables with names and stuff
    firstNames = ["John", "Jane", "Bob", "Alice", "Charlie", "Daisy", "Ethan", "Fiona", "George", "Hannah"]
    LastNames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    birthdayServices = ["Baloons", "Cakes", "Photography", "Decorations", "Music", "Food", "Drinks"]

    # Delete all entries for items
    items.clear()
    itemHistory.clear()

    # Make 3 entries
    for i in range(3):
        # Get data needed to populate item class
        recieptId = str(i + 1)
        name = f"{random.choice(firstNames)} {random.choice(LastNames)}"
        service = random.choice(birthdayServices)
        price = abs(random.random()) * 250
        price = round(price, 2)
        quantity = random.randint(1, 5)
        
        # Generate the Item class
        item = Item(name=service, price=price, quantity=quantity, customer_name=name)

        # Add them to dictionary and list
        items[recieptId] = item
        itemHistory.append(item)

# Adds an image (logo) to the top of the window on init
def addImageInit():
    # Open image using PIL
    logo = Image.open("Logo.png")

    # Convert to CTkImage
    logoCTk = ctk.CTkImage(light_image=logo, size=(95, 41))

    # Place the image
    ctk.CTkLabel(window, image=logoCTk, text="").grid(row=0, column=1, pady=PDG)

class UserInput(): # A class that deals with user input and interacts with the items dictionary and reciept viewer
    def __init__(self, frame, recieptInstance):
        # This class is passed a frame which is in the main window, the frame is used for placing widgets for user input
        self.frame = frame

        # This class is passed with a recieptInstance so I can call functions from it, e.g. update the reciept
        self.recieptInstance = recieptInstance

        # Initialise the widgets via a subroutine
        self.create_widgets()
    
    # Initialises widgets for user to interact with
    def create_widgets(self):
        # Make a grid inside the frame to deal with positioning of everything
        gridFrame = ctk.CTkFrame(self.frame)
        gridFrame.pack()

        # Labels, inside grid
        customerName = ctk.CTkLabel(gridFrame, text="Customer Name:")
        recieptId = ctk.CTkLabel(gridFrame, text="Reciept ID:")
        itemName = ctk.CTkLabel(gridFrame, text="Item Name:")
        price = ctk.CTkLabel(gridFrame, text="Price:")
        quantity = ctk.CTkLabel(gridFrame, text="Quantity:")

        # Place on screen for mainloop to utilize (sticky = "E" for aligning on the right)
        customerName.grid(row=0, column=0, padx=PDG, pady=PDG, sticky="E")
        recieptId.grid(row=1, column=0, padx=PDG, pady=PDG, sticky="E")
        itemName.grid(row=2, column=0, padx=PDG, pady=PDG, sticky="E")
        price.grid(row=3, column=0, padx=PDG, pady=PDG, sticky="E")
        quantity.grid(row=4, column=0, padx=PDG, pady=PDG, sticky="E")

        # User inputs, inside grid
        # All the entries are under self (variables in the class scope) so it can be acsessed outside of this initialiser funtion
        self.customerNameEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter name")
        self.recieptIDEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter reciept ID")
        self.itemNameEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter item name")
        self.priceEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter price")
        self.quantityEntry = ctk.CTkEntry(gridFrame, placeholder_text="Enter quantity")

        # Sticky = "W" for aligning on the left
        self.customerNameEntry.grid(row=0, column=1, padx=PDG, pady=PDG, sticky="W")
        self.recieptIDEntry.grid(row=1, column=1, padx=PDG, pady=PDG, sticky="W")
        self.itemNameEntry.grid(row=2, column=1, padx=PDG, pady=PDG, sticky="W")
        self.priceEntry.grid(row=3, column=1, padx=PDG, pady=PDG, sticky="W")
        self.quantityEntry.grid(row=4, column=1, padx=PDG, pady=PDG, sticky="W")

        # Buttons, in main frame, outside grid
        checkoutButton = ctk.CTkButton(self.frame, text="Hire", command=self.checkout)

        # Place itt outside grid, so is aligned in the center
        checkoutButton.pack(padx=PDG, pady=PDG)

    def checkout(self):
        # Bunch of checks to check of boxes are not empty
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

        # Checking if necessary inputs can be converted to a number before going ahead
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
        
        # The number input boxes (reciept ID, quantity, and price) are all numbers
        # Now we check if they are negative

        if int(self.recieptIDEntry.get()) < 0:
            error_window("Reciept ID can not be less that 0")
            return
        
        if int(self.quantityEntry.get()) < 0:
            error_window("Quantity cannot be negative")
            return
        
        if float(self.priceEntry.get()) < 0:
            error_window("Price cannot be negative")
            return
        
        # Check if reciept ID is already in the dictionary
        if self.recieptIDEntry.get() in items.keys():
            error_window("Reciept ID already exists")
            return
        
        if int(self.recieptIDEntry.get()) > 9999:
            error_window("Reciept ID must be less than 10000")
            return
    
        if int(self.quantityEntry.get()) > 99:
            error_window("Quantity must be less than 100")
            return

        if float(self.priceEntry.get()) > 9999:
            error_window("Price must be less than 10000")
            return

        # If it gets here, all checks are a sucssess!

        # Store the entry
        int(self.quantityEntry.get())
        price = float(self.priceEntry.get())
        recieptId = self.recieptIDEntry.get()

        # Note im using a class to store this instead of a multidimensional array as its better practice for cleaner code
        item = Item(self.itemNameEntry.get(), 
            price, 
            self.quantityEntry.get(), 
            self.customerNameEntry.get())
        items[recieptId] = item
        
        # Add to the list that has the full history of items
        itemHistory.append(item)

        # Delete entries, fresh for a new input
        self.customerNameEntry.delete(0, ctk.END)
        self.recieptIDEntry.delete(0, ctk.END)
        self.itemNameEntry.delete(0, ctk.END)
        self.priceEntry.delete(0, ctk.END)
        self.quantityEntry.delete(0, ctk.END)

        # Update the reciept viewer via the instance
        self.recieptInstance.update_widgets()

class Reciept: # A reciept viewer class to view items currently on hire etc
    def __init__(self, frame):
        # This class is passed a frame which is in the main window, the frame is used for placing widgets to display the entries
        self.frame = frame
        self.create_reciept_widgets()
    
    # Creates nessacary widgets, applied to self
    def create_reciept_widgets(self):
        self.reciept = ctk.CTkTextbox(self.frame, width=300, height=240)
        self.reciept.insert(ctk.END, "No items on hire")
        self.reciept.configure(state="disabled") # Lock the text box so it cannot be edited
        self.reciept.pack()

    # Update the reciept viewer, called from other classes
    def update_widgets(self):
        self.reciept.configure(state="normal") # Unlock the text box
        self.reciept.delete("1.0", ctk.END) # Delete everything
        
        tempStr = "" # Make a temporary string to add onto

        # Iterate through items and generate entries to display
        for key in items.keys():
            value = items[key]
            tempStr += make_reciept_entry(key, value)

        # Get the total including GST, and display it
        total = getTotal()
        tempStr += f"Total since started incl GST: {total:.2f}\n"

        # Get total excluding GST, which acts as money Julie gets
        tempStr += f"Total since started excl GST: {total / (1 + GST):.2f}"

        self.reciept.insert(ctk.END, tempStr) # Display all the data formatted in tempStr
        self.reciept.configure(state="disabled") # Lock it again

class EntryRemover(): # Removes entrys i.e. item is returned
    def __init__(self, frame, recieptInstance):
        # Initialize variables
        self.frame = frame
        self.create_widgets()
        self.recieptInstance = recieptInstance
    
    def gen_example_data(self):
        generate_example_data()
        recieptInstance.update_widgets()

    # Initialise correct widgets
    def create_widgets(self):
        # Describe this section of the GUI
        label = ctk.CTkLabel(self.frame, text="Remove entry by Reciept ID")
        label.pack(padx=PDG, pady=PDG)

        # Entry for user input, requireing a reciept ID to delete
        self.entry = ctk.CTkEntry(self.frame, width=200, height=30, placeholder_text="Enter Reciept ID")
        self.entry.pack(padx=PDG, pady=PDG)

        # A button that attempts to remove the entry from the reciept
        self.removeButton = ctk.CTkButton(self.frame, text="Remove", command=self.remove_entry)
        self.removeButton.pack(padx=PDG, pady=PDG)

        self.exampleDataButton = ctk.CTkButton(self.frame, text="Example Data", command=self.gen_example_data)
        self.exampleDataButton.pack(padx=PDG, pady=PDG)

    def remove_entry(self): # Remove an entry
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

# Code starts here
if __name__ == "__main__":
    # Make a window with correct settings
    window = ctk.CTk()
    window.title("Julie's party hire shop")
    window.geometry(f"{MAIN_WINDOW_WIDTH}X{MAIN_WINDOW_HEIGHT}")
    window._set_appearance_mode("dark")
    window.resizable(False, False)

    # Adds an image (logo) in init (initialization of window)
    addImageInit()

    # Make frames for classes to populate
    # Reciept viewer (items currently on hire) on the middle
    recieptFrame = ctk.CTkFrame(window, width=300, height=200)
    recieptFrame.grid(row=1, column=1, padx=PDG)

    # User input (add) on the left
    userInputFrame = ctk.CTkFrame(window, width=300, height=200)
    userInputFrame.grid(row=1, column=0, padx=PDG, pady=PDG)

    # User input (remoev items) on the right
    recieptRemoverFrame = ctk.CTkFrame(window, width=300, height=200)
    recieptRemoverFrame.grid(row=1, column=3, padx=PDG, pady=PDG)

    # Run the classes so they populate the frames and run independantly
    recieptInstance = Reciept(recieptFrame)
    userInputInstance = UserInput(userInputFrame, recieptInstance) # Add recieptInstance as a parameter so it can be used in the class
    recieptRemoverInstance = EntryRemover(recieptRemoverFrame, recieptInstance) # Add recieptInstance as a parameter so it can be used in the class

    # Display the window
    window.mainloop()