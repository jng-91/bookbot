#def main():
#    book_path = "books/frankenstein.txt"
#    text = get_book_text(book_path)
#    print(text)
    
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

class Book:
    def __init__(self, title, author, book_path):
        self.title = title
        self.author = author
        self.book_path = book_path

    def get_title(self):
        print (self.title)
    
    def get_author(self):
        print (self.author)
    
    def get_book_text(self):
        with open (self.book_path) as f:
            print(f.read())
    
    def count_words(self):
        with open (self.book_path) as f:
            tmp_book_text = f.read()
            print (len(tmp_book_text.split()))




def main():
    frankenstein = Book("Frankenstein", "Mary Shelley", "books/frankenstein.txt")

    frankenstein.count_words()


main()