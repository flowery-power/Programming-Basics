fav_book = input()
counter = 0
book = input()
book_not_found = False

while book != fav_book:

    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        book_not_found = True
        break
    book = input()
    counter += 1

if not book_not_found:
    print(f"You checked {counter} books and found it.")
