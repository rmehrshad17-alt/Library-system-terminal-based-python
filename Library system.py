import msvcrt





counter = 0
# ---------Unique ID ----------
def idcheck(id):
    global counter
    if id in data:
        if len(id)>4:
            counter+=1
            id = id[:-1]
            return idcheck(id + str(counter))
        else:
            counter+=1
            return idcheck(id + str(counter))
    else:
        counter = 0
        return id

def book_id(name,release_date):
    global counter
    id = name[:2] + release_date[-2:]
    return idcheck(id)    


    




def show_list():
    global data
    print()
    for j in data:
        print(f" ({data[j]['name']}) book from ({data[j]['writer']}) that released ({data[j]['release_date']}) | count : ({data[j]['count']}) \n ")
def add_book():
    global data
    print()
    print("======================================")
    print()
    print("adding book...")
    print()
    name = input("enter name of the book : ")
    name = name.lower()
    print()
    writer = input(f"enter writer of {name} : ")
    print()
    release_date = input(f"enter realse date of {name} : (format : 1404,10,21) ")
    print()
    id = book_id(name,release_date)
    print(f"your book id : {id}")
    print()
    bookcount = int(input("how many book you have : "))
    

    data[id] = {"name" : name.lower(),"writer" : writer,"release_date" : release_date,"count" : bookcount}

    show_list()


def search_by_name():
    global data
    print()
    found = False
    search_data = {}
    # variable c is a counter
    c = 0
    while True:
        srch = input("enter your book full name (capital and small letter does matter !) : \n (if you want to quit searching enter 0)\n\n")
        for i in data:
            if srch == data[i]['name']:
                # if there is just one result :
                id = i
                # else
                search_data[i] = {"name" : data[i]['name'],"writer" : data[i]['writer'],"release_date" : data[id]['release_date'],"count" : data[i]['count']}
                found = True
                c+=1
        if srch == "0":
            print("\n going back to the main menu...\n")
            menu()
        elif found:
            if c ==1:
                print()
                print(f"your book found !")
                print()
                book = f" ({data[id]['name']}) book from ({data[id]['writer']}) that released ({data[id]['release_date']}) | count : ({data[id]['count']}) \n "
                print(book)
                input("press ENTER to go back to the previous menu...\n")
                return book,id
            else :
                print()
                print(f"there is more than one book with this name ({data[i]['name']})")
                print()
                print("which one of this is the book you want ? ")
                print()
                #variable j is a counter
                j = 1
                for i in search_data:
                    print(f" {j}.{search_data[i]['name']} by {search_data[i]['writer']} that released {search_data[i]['release_date']} | count : {search_data[i]['count']}")
                    j +=1
                try:
                    print()
                    sel = int(input("Enter a number : "))
                    #variable t is a counter
                    t = 0
                    for i in search_data :
                        t+=1
                        if t == sel:
                            id = i
                    print()
                    print(f"your book found !")
                    print()
                    book = f" ({data[id]['name']}) book from ({data[id]['writer']}) that released ({data[id]['release_date']}) | count : ({data[id]['count']}) \n "
                    print(book)
                    input("press ENTER to go back to the previous menu...\n")
                    return book,id
                except:
                    print()
                    print("wrong input ! try again...")
                    print()
                    
                    

        elif not found :
            print()
            print("there is not any book with that name ! Try again...\n ")



def search_by_id():
    global data
    print()
    found = False
    while True :
        srch = input("enter your book ID that given to you when you were adding your book (capital and small letter doesnt matter) : \n (if you want to quit searching enter 0)\n\n")
        for i in data:
            if i == srch:
                found = True
                id = srch
        if srch == "0":
            print("\n going back to the main menu...\n")
            break
        elif found:
            print()
            print(f"your book found !")
            print()
            book = f" ({data[id]['name']}) book from ({data[id]['writer']}) that released ({data[id]['release_date']}) | count : ({data[id]['count']}) \n "
            print(book)
            input("press ENTER to go back to the previous menu...\n")
            return book,srch
        elif not found :
            print()
            print("there is not any book with that Id ! Try again...\n ")





def search_menu():
    while True :
        print()
        print("======================================")
        print("you want to search in your library by the name of book or ID of book")
        print("! this menu is not like the main menu ! ")
        print("! just press 1 or 2 or 3 !")
        print("! do not need to press [enter] !")
        print("================menu==================")
        print("1.name")
        print("2.ID")
        print("3.quit")
        print("======================================")
        print()
        sel = msvcrt.getch()
        if sel == b"1":
            print("===================================")
            book,id = search_by_name()
            return book,id
        elif sel == b"2":
            print("===================================")
            book,id = search_by_id()
            return book,id
        elif sel == b"3":
            print()
            print("go back to the main menu !")
            menu()    
        else:
                print("Wrong input ! Try again...")
                print()

def change_info(sel,book,id):
    global data
    while True:
        if sel == b'1':
            print()
            print(book)
            print()
            print(" ! changing name ! ")
            newname = input("enter new name for this book : ")
            data[id]['name'] = newname
            book = f" ({data[id]['name']}) book from ({data[id]['writer']}) that released ({data[id]['release_date']}) | count : ({data[id]['count']}) \n "
            change_info_menu(book,id)

        elif sel == b'2' :
            print()
            print(book)
            print()
            print(" ! changing writer ! ")
            newwriter = input("enter new writer name for this book : ")
            data[id]['writer'] = newwriter
            book = f" ({data[id]['name']}) book from ({data[id]['writer']}) that released ({data[id]['release_date']}) | count : ({data[id]['count']}) \n "
            change_info_menu(book,id)
            
        elif sel == b'3' :
            print()
            print(book)
            print()
            print(" ! changing release date ! ")
            newrelease_date = input("enter new release date for this book : ")
            data[id]['release_date'] = newrelease_date
            book = f" ({data[id]['name']}) book from ({data[id]['writer']}) that released ({data[id]['release_date']}) | count : ({data[id]['count']}) \n "
            change_info_menu(book,id)
            change_info_menu(book,id)
        elif sel == b'4' :
            print()
            print(book)
            print()
            print(" ! changing count of book ! ")
            newcount = int(input("enter new count for this book : "))
            data[id]['count'] = newcount
            book = f" ({data[id]['name']}) book from ({data[id]['writer']}) that released ({data[id]['release_date']}) | count : ({data[id]['count']}) \n "
            change_info_menu(book,id)
        elif sel == b'5':
            print()
            print(book)
            change_info_menu(book,id)
        elif sel == b'6' :
            print()
            print("going back to the main menu...")
            menu()
        else :
            print()
            print("wrong key ! ")
            change_info_menu(book,id)
            



def change_info_menu(book,id):
    print()
    print("======================================")
    print("what part of the information you want to change ? ")
    print("================menu==================")
    print("1.name")
    print("2.writer")
    print("3.release date")
    print("4.book count")
    print("5.show the current book info")
    print("6.go back to the main menu")
    print("======================================")
    print()
    sel = msvcrt.getch()
    change_info(sel,book,id)


def remove(sel,id):
    global data
    if sel == b'1':
        print()
        print(f'removing ({data[id]["name"]}) book with ({id}) ID...')
        del data[id]
        print()
        print("done...the book removed from your list...\n")
        input("press ENTER to go back to the main menu")
        menu()
    elif sel == b'2':
        print()
        print("going back to the main menu...")
        menu()
    else :
        print()
        print("wrong input !")
    

def removemenu(book,id):
    global data
    print()
    print("===========================================================")
    print("! this menu is not like the main menu ! ")
    print("! just press 1 or 2 or 3 !")
    print("! do not need to press [enter] !")
    print("===========================================================")
    print(f"\n{book}\n")
    print(f"you are removing ({data[id]["name"]}) with ({id}) ID...\n")
    print("are you sure about it ? \n")
    print("1.yes\n2.no")
    while True:
        sel = msvcrt.getch()
        remove(sel,id)





def menu():
    while True :
        print()
        print("======================================")
        print("welcome to the library system")
        print("================menu==================")
        print("1.add book")
        print("2.show list of book")
        print("3.search book ( name / ID )")
        print("4.change information of books")
        print("5.remove books")
        print("6.exit")
        print("======================================")
        print()
        select = int(input("enter your choice : "))
        while True :
            if select == 1:
                add_book()
                break
            elif select ==2:
                show_list()
                break
            elif select ==3:
                search_menu()
                break
            elif select ==4:
                book,id = search_menu()
                change_info_menu(book,id)
                break
            elif select ==5:
                book,id = search_menu()
                removemenu(book,id)
                break
            elif select ==6:
                quit()


menu()