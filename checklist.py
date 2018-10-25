checklist = list()

# CREATE FUNCTION
def create(item):
    checklist.append(item)

# READ FUNCTION
def read(index):
    return checklist[index]

# Update Function
def update(index, item):
    checklist[index]= item

# DESTROY FUNCTION
def destroy(index):
    checklist.pop(index)

# TEST FUNCTION
def test():
    create("purple sox")
    create("red clock")

    print(read(0))
    print(read(1))

    update(0, "pruple socks")
    destroy(1)

    print(read(0))
    # print(read(1))

test()
