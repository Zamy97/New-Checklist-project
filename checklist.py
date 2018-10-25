checklist = list()

# CREATE FUNCTION
def add_to_list(item):
    checklist.append(item)

# READ FUNCTION
def read(index):
    return checklist[index]

# Update Function
def update(index, item):
    checklist[index] = item

# DESTROY FUNCTION
def destroy(index):
    checklist.pop(index)

# FINDING ALL THE ITEMS FUNCTION
def list_all_item():
    number = 0
    for every_item in checklist:
        print(str(number) + " " + every_item)
        number += 1

# MARK COMPLECTED FUNCTION ON THE LIST
def mark_complected(index):
    checklist[index] = "√" + checklist[index]

#Changes the color of text in the terminal
print("\033[1;31;40m")

#USER INPUT FUNCTION
def user_input():
    print("press C to add to the list, R to remove, U to update item, p to show the list")
    print("press Q to exit the program")
    user_input = input("")

    #CREATE ITEM
    if user_input == "A":
        input_item = input("ADD to LIST: ")
        add_to_list(input_item)

    #REMOVE FROM THE LIST
    elif user_input == "R":
        item_number = input("what do you want to delete? press x to cancel ")
        if(item_number != "x"):
            destroy(int(item_number))

    #UPDATE ITEM IN LIST
    elif user_input == "U":
        item_number = input("what do you want to update? press x to cancel")
        if item_number != "x":
            update(int(item_number))

    # MARK ITEM AS COMPLECTED
    elif user_input == "C":
        item_number = input("which item you want to mark complected: ? x to cancel ")
        if item_number != "x":
            mark_complected(int(item_number))


    #PRINT ALL ITEMS
    elif user_input == "p":
        list_all_item()

    elif user_input == "q":
        # This will end the loop from running forever
        return False

    #CATCH ALL
    else:
        print("Unknown error")

    return True


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
running = True
while running:
    running = user_input()
