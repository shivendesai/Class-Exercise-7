#Written by Shiven Desai
# Define the food_items function to display the selected food items
def food_items():
    # Clear any previous selections
    food_selected.delete(0, END)
    
    # Get the selected food items from the listbox
    selected_items = [food_list.get(i) for i in food_list.curselection()]
    
    # Display the selected food items in the text widget
    for item in selected_items:
        food_selected.insert(END, item)

        # Print the selected food items to the console
        print(item)
        
# Create the main window
root = Tk()
root.title("Food Selector")

# Create a listbox containing food items
food_list = Listbox(root, selectmode=MULTIPLE)
food_list.insert(1, "Pizza")
food_list.insert(2, "Burger")
food_list.insert(3, "Taco")
food_list.insert(4, "Salad")
food_list.pack()

# Create a button to select food items
select_button = Button(root, text="Select", command=food_items)
select_button.pack()

# Create a text widget to display the selected food items
food_selected = Text(root)
food_selected.pack()

root.mainloop()
