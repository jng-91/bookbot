#def main():
#    book_path = "books/frankenstein.txt"
#    text = get_book_text(book_path)
#    print(text)
from operator import itemgetter  
    
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
        tmp_text = self.get_book_text().lower()
        letters_counted = {}
        for letter in tmp_text:
            if not letter.isalpha():
                pass 
            
            elif letter in letters_counted:
                letters_counted[letter] += 1
            
            else:
                letters_counted[letter] = 1
        return letters_counted
    

    def get_report(self):
        
        counted_letters = self.count_letters()
        tmp_list = list(counted_letters.items())

        tmp_list_sorted = sorted(tmp_list, key=itemgetter(1))

        print(f"--- Begin report of {self.book_path} ---")
        
        print ("")
        
        print (f"{self.count_words()} words found in the document")
        
        print ("")

        for pair in tmp_list_sorted:
            print (f"The {pair[0]} character was found {pair[1]} times")
        
        print ("")

        print ("--- End report ---")

        

         

        
        



        
        
        
        





def main():

    frankenstein = Book("Frankenstein", "Mary Shelley", "books/frankenstein.txt")

    frankenstein.get_report()


main()