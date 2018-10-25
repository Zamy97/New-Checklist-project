checklist = list()

# CREATE FUNCTION
def add_to_list(add_item_to_list):
    checklist.append(add_item_to_list)

# READ FUNCTION
def read(index):
    return checklist[index]

# Update Function
def update_item_in_the_list(index, add_item_to_list):
    checklist[index] = add_item_to_list

# REMOVE ITEM
def destroy_item_in_the_list(index):
    checklist.pop(index)

# FINDING ALL THE ITEMS FUNCTION
def list_all_item():
    number_items = 0
    for every_item in checklist:
        print(str(number_items) + " " + every_item)
        number_items += 1

# MARK COMPLECTED FUNCTION ON THE LIST
def mark_completed(index):
    checklist[index] = "√" + checklist[index]

#Changes the color of text in the terminal
print("\033[1;31;40m")

#USER INPUT FUNCTION
def user_prompt():

    print("press A to add to the list, R to remove, U to update item, p to show the list, C to mark as completed.")
    print("press Q to exit the program")
    user_input = input("")

    #ADD ITEM TO THE LIST
    if user_input == "A":
        input_item = input("ADD an item to LIST: ")
        add_to_list(input_item)

    #REMOVE FROM THE LIST
    elif user_input == "R":
        item_number = input("what do you want to delete? press x to cancel ")
        if(item_number != "X"):
            destroy_item_in_the_list(int(item_number))

    #UPDATE ITEM IN LIST
    elif user_input == "U":
        item_number = input("what do you want to update? press x to cancel")
        if item_number != "X":
            input_item = input("Enter a new item: ")
            update(int(item_number), input_item )

    # MARK ITEM AS COMPLETED
    elif user_input == "C":
        item_number = input("which item you want to mark completed: ? x to cancel ")
        if item_number != "X":
            mark_completed(int(item_number))


    #PRINT ALL ITEMS OF THE LIST
    elif user_input == "P":
        list_all_item()

    #FINISH RUNNING THE LOOP IF THEY TYPE Q
    elif user_input == "Q":
        return False

    #CATCH ALL
    else:
        print("Unknown error")

    return True

#INFINITE LOOP
running = True

while running:
    running = user_prompt()


# # TEST FUNCTION
# def test():
#
#     create("purple sox")
#     create("red clock")
#     create("Computer")
#     create("Pencil")
#     create("Notebook")
#     create("Desktop")
#
#     print(read(0))
#     print(read(1))
#
#     update(0, "purple socks")
#     destroy(1)
#
#     print(read(0))
#
#     # LET'S TEST CREATE ITEM IN SELECT FUNCTION
#     select("C")
#     #VIEW ALL THE RESULTS
#     list_all_item()
#     #CALL FUNCTION WITH NEW VALUE
#     select("R")
#     #VIEW RESULTS
#     list_all_item()
#
#     #USER INPUT test
#     user_value = user_input("Please enter a vlue: ")
#     print(user_value)
#
#     test()
#     # list_all_item()
#     # mark_complected(2)
# #WHILE LOOP TO CONTINUE RUNNING THE PROGRAM
