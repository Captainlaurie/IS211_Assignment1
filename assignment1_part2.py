#!/usr/bin/env python
# coding: utf-8

# In[19]:



class Book:
    
    
    def __init__(self, author, title):
        
        """ __init__ constructor that creates object variables with given attributes """
        
        self.author = author
        self.title = title
    
    def display(self):
    
        """Function that prints a book in the form of 'title, written by author' """
    
        print (f"{self.title}, written by {self.author}")


if __name__ == "__main__":
    
    #create class objects with attributes
    
    hPotter4 = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
    ivh = Book("Sir Walter Scott", "Ivanhoe: A Romance")
    
hPotter4.display()
    
ivh.display()
    
    
    


# In[ ]:




