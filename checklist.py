checklist = list()

# CREATE FUNCTION
def create(item):
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
    index = 0
    for every_item in checklist:
        print(str(index) + every_item)
        index += 1

def mark_complected(index):
    checklist[index] = str("√") + checklist[index]

print("\033[1;34;40m")

def select(function_code):
    #CREATE ITEM
    if function_code.lower() == "c":
        input_item = user_input(" Input item: ")
        create(input_item)

    #READ ITEM
    elif function_code.lower() == "r":
        item_index = user_input("Index number?")

        read(item_index)

    #PRINT ALL ITEMS
    elif function_code.lower() == "p":
        list_all_item()

    elif function_code.lower() == "q":
        #THIS IS WHERE THE LOOP WILL END
        return False

    #CATCH ALL
    else:
        print(" Go get a job")

    return True

#USER INPUT FUNCTION
def user_input():
    user_input = input(prompt)



# TEST FUNCTION
def test():

    create("purple sox")
    create("red clock")
    create("Computer")
    create("Pencil")
    create("Notebook")
    create("Desktop")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    # LET'S TEST CREATE ITEM IN SELECT FUNCTION
    select("C")
    #VIEW ALL THE RESULTS
    list_all_item()
    #CALL FUNCTION WITH NEW VALUE
    select("R")
    #VIEW RESULTS
    list_all_item()

    #USER INPUT test
    user_value = user_input("Please enter a vlue: ")
    print(user_value)

test()
    # list_all_item()
    # mark_complected(2)
    
#WHILE LOOP TO CONTINUE RUNNING THE PROGRAM
running = True
while running:
    selection = user_input(
    "press C to add to list, R to Read from the list and P to display the list and q to quit the program")
    running = select(selection)
