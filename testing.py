checklist = list()

def add_to_list(note):
    checklist.append(note)

def show_list():
    number = 0
    for item in checklist:
        print(str(number) + " " + item)
        number += 1

def update_item(index, note):
    checklist[index] = note

def remove_item(index):
    checklist.pop(index)

def complete_item(index):
    checklist[index] = "**Completed** " + checklist[index]

def user_prompt():

    print("Press A to Add to list, R to Remove, U to Update item, C to mark as Completed, and P to show list.")
    print("Press Q to get out of this world")
    user_input = input("")

    #Add Note to list
    if user_input == "A":
        user_note = input("Add to List: ")
        add_to_list(user_note)

    #Remove note from list
    elif user_input == "R":
        item_number = input("Which item to delete? X to Cancel")
        if(item_number != "X"):
            remove_item(int(item_number))

    #Update Item in List
    elif user_input == "U":
        item_number = input("Which item to update? X to Cancel")
        if item_number != "X":
            user_note = input("Enter new note: ")
            update_item(int(item_number), user_note)

    #Mark item as completed
    elif user_input == "C":
        item_number = input("Which item to Mark Completed? X to Cancel ")
        if item_number != "X":
            complete_item(int(item_number))

    #Print contents of list
    elif user_input == "P":
        show_list()
    elif user_input == "Q":
        return False
    else:
        print("Unknown Option")

    return True

# if __name__ == "__main__":
running = True

while running:
    running = user_prompt()
