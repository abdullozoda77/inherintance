class Library:
    def __init__(self, title, author, available=True):
         self.title = title
         self.author = author
         self.available = available
    @property
    def title(self):
         return self.__title
    @property
    def author(self):
         return self.__author
    @property
    def available (self):
         return self.__available
    @title.setter
    def title (self, value):
        if not value:
            print("empty")
        else:
            self.__title = value
    @author.setter
    def author(self, value):
        if not value:
            print("empty")
        else:
            self.__author = value
    @available.setter
    def available (self, value):
        if isinstance(value , bool):
            self.__available = value
        else:
            print('no bool !')
    def borrow (self):
        if self.__available:
            self.__available = False
            print("borowed" , self.title)
        else:
            print(self.title , "not available")
    def return_b(self):
        self.__available = True
        print("u return" , self.__title)
b_title = input("enter title --> ")
b_author = input("enter author --> ")
b = Library(b_title, b_author)
print(b.title, b.author, b.available)
b.borrow()
b.return_b()
