import os 

library_catalog = {}

def clear_terminal():
  os.system("cls" if os.name == "nt" else "clear")

def add_book():
  while True:
    clear_terminal()
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    library_catalog[isbn] = {
      "title" : title,
      "author": author,
      "available" : True,
    }

    print(f"Book {title} by {author} added to the catalog with ISBN {isbn}.")

    choice = input("Do you want to add another book? (y/n): ")
    if choice.lower() != "y":
      break

def check_out_book():
  while True:
    clear_terminal()
    isbn = input("Enter ISBN: ")
    if isbn in library_catalog:
      if library_catalog[isbn]["available"]:
        library_catalog[isbn]["available"] = False
        print(f"Book ''{library_catalog[isbn]['title']}'' checked out successfully")
      else:
        print("Sorry the book currently checked out.")
    else:
        print("Book not found in the catalog.")
    choice = input("Do you want to check out another book? (y/n): ")
    if choice.lower() != "y":
      break

def check_in_book():
  while True:
    clear_terminal()
    isbn = input("Enter ISBN to check in: ")
    if isbn in library_catalog:
      if not library_catalog[isbn]["available"]:
        library_catalog[isbn]["available"] = True
        print("Book '{library_catalog[isbn]['title']}' checked in successfully. ")
      else:
        print("Book is already in the library.")
    else:
      print("Book not found in the library.")

    choice = input("Do you want to check in another book? (y/n): ")
    if choice.lower() != "y":
      break




def list_book():
  clear_terminal()
  print("\nlibrary_catalog:")
  for isbn in library_catalog:
    book_info = library_catalog[isbn]
    print(f" ISBN: {isbn}, Title: {book_info['title']}, Author: {book_info['author']}, available: {book_info['available']}  ")

  choice = input("Do you want to go back to the main page? (y/n): ")
  if choice.lower() == "y":
    break

while True:
  print("\nMenu:")
  print("1. Add Book")
  print("2. Check Out Book")
  print("3. Check In Book")
  print("4. List Books")
  print("5. Exit")

  choice = input("Enter your choice between (1:5): ")

  if choice == "1":
    add_book()
  elif choice == "2":
    check_out_book()
  elif choice == "3": 
    check_in_book()
  elif choice == "4": 
    list_book()
  elif choice == "5": 
    print("Exiting the program...")
    break
  else:
    print("Invalid choice. Please enter a number between 1:5 ")
  


   

