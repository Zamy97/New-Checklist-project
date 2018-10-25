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


print("\033[1;34;40m")

# TEST FUNCTION
def test():

    create("purple sox")
    create("red clock")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))


test()
list_all_item()
