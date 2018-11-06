def permutation(string):
    list_of_perm = []
    list_of_char = []

    for char in string:
        list_of_char.append(char)

    for i, char in enumerate("war"):
        for index in [0,1,2]:
            temp_list = list(list_of_char)
            temp_list[i]=list_of_char[index]
            temp_list[index]=char
            temp_string = "".join(temp_list)
            if temp_string not in list_of_perm:
                list_of_perm.append(temp_string)

    print(list_of_perm)

permutation("war")
