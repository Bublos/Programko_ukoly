from classes.book import Book
from os.path import realpath,join,dirname
class Library(Book):
    def __init__(self,path_to_file:str) -> None:
        self.path = path_to_file
        self.books=[]
        with open(self.path,"r", 
                  ) as file:
            for line in file:
                book = Book(line.strip())
                self.books.append(book)
        self.books.sort(key=lambda book : book.author)

    def add_book(self,other:str):
        for book in self.books:
            if book.id == other.id:
                return print("Kniha nemá unikátní ID")
        self.books.append(other)
        self.books.sort(key=lambda book: book.author)
        print(f"Kniha s id {other.id} byla přidána")

    def get_unique_id(self)->int:
        ids = [int(book.id) for book in self.books]
        ids.sort()
        for i in range(len(ids)):
            if ids[i] != i + 1:
                return i + 1
        return len(ids) + 1
    
    def show_available_books(self):
        for book in self.books:
            if book.available == "Available":
                print(book)

    def find_book_and_borrow_it(self, name):
        i=0
        for book in self.books:
            if name in book.name:
                if book.available =="Available":
                    temp = book
                    i+=1
                    print(book)
        if i==1:
            if input("Přejete si knihu vypújčit?: a/n: ") == "a":
                temp.available = "Unavailable"

        if i==0:
            print("Neexistuje žádná dostupná kniha s tímto jménem")
            
    
    def repr(self):
        return "\n".join([str(book) for book in self.books]) 
    def __str__(self):
        return self.repr()
            
