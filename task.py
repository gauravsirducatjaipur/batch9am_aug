list1 = []

def createList():
    try:
        global list1
        list1 = []
        listSize = int(input("How many elements do you want to add in list: "))

        for i in range(listSize):
            element = input("Enter element which you want to add in list: ")
            list1.append(element)
    except:
        print("Some error in list creation")
    else:
        print("List created successfully")
        print("List is:", list1)
    finally:
        print("function called successfully")

def editList():
    try:
        global list1
        element = input("Enter element which you want to edit: ")

        if len(list1) == 0:
            print("List is empty")
        elif element not in list1:
            print("Element is not present in list")
        else:
            print("Current List:", list1)
            # index = int(input("Enter index of element which you want to edit: "))
            index = list1.index(element)

            if index >= 0 and index < len(list1):
                newElement = input("Enter new element: ")
                list1[index] = newElement
                print("Element updated successfully")
                print("Updated List:", list1)
    except:
        print("Some error in list editing")
    else:
        print("program executed successfully without an exception")
    finally:
        print("function called successfully")


def deleteList():
    global list1
    if len(list1) == 0:
        print("List is already empty")
    else:
        list1.clear()
        print("List deleted successfully")

def viewList():
    if len(list1) == 0:
        print("List is empty")
    else:
        print("Your List is:")
        for i in range(len(list1)):
            print(i, ":", list1[i])

def searchList():
    if len(list1) == 0:
        print("List is empty")
    else:
        element = input("Enter element which you want to search: ")
        if element in list1:
            print("Element is present in list")
            print("Index:", list1.index(element))
        else:
            print("Element is not present in list")

while True:
    choice = int(input(
        "\nEnter your choice\n"
        "Press 1. Create New List\n"
        "Press 2. Edit List\n"
        "Press 3. Delete List\n"
        "Press 4. View List\n"
        "Press 5. Search Element\n"
        "Press 6. Exit\n"
    ))

    print("Choice is:", choice)

    if choice == 1:
        createList()
    elif choice == 2:
        editList()
    elif choice == 3:
        deleteList()
    elif choice == 4:
        viewList()
    elif choice == 5:
        searchList()
    elif choice == 6:
        print("Thank you")
        break
    else:
        print("Invalid Choice")