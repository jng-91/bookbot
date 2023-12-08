#def main():
#    book_path = "books/frankenstein.txt"
#    text = get_book_text(book_path)
#    print(text)
    
    
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
            return(f.read())
    
    def count_words(self):
        tmp_book_list= self.get_book_text()
        
        return (len(tmp_book_list.split()))
    
    def count_letters(self):
        tmp_text = self.get_book_text()
        
        





def main():
    frankenstein = Book("Frankenstein", "Mary Shelley", "books/frankenstein.txt")

    print(frankenstein.count_words())


main()