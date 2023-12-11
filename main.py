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
    
    # Prints a report about the Book class object that includes some text formatting and the number of words as well as the number of each character of the alphabet in the book
    def get_report(self):
        
        #saves a Dictionary including all letters found in the book as key and the number of how often that letter is included as the keys value
        counted_letters = self.count_letters()
        
        # converts that dictionary to a list of touples while each touple has the following format [(key,value)]
        tmp_list = list(counted_letters.items())

        #uses the python build in sorted function together with the itemgetter function to sort the list of touples by the touples [1] value in ascending order
        tmp_list_sorted = sorted(tmp_list, key=itemgetter(1))

        print(f"--- Begin report of {self.book_path} ---")
        
        print ("")
        
        print (f"{self.count_words()} words found in the document")
        
        print ("")

        #loop through the sorted list of touples to print each pair 
        for pair in tmp_list_sorted:
            print (f"The {pair[0]} character was found {pair[1]} times")
        
        print ("")

        print ("--- End report ---")

        

         

        
        



        
        
        
        





def main():

    frankenstein = Book("Frankenstein", "Mary Shelley", "books/frankenstein.txt")

    frankenstein.get_report()


main()