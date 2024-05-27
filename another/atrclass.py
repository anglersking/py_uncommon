import attr
@attr.s
class Book:
    title=attr.ib(type=str)
    author =attr.ib(type=str)
    @title.validator
    def check(self,attribute,value):
        if not "a" in value:
            raise ValueError("title mast habe a")

# @attr.s
# class Books:
#     books=attr.ib(factory=list,type=List[Book])
    
#     def add_book(self,book:Book):
#         pass 


book=Book(title="asd",author="马")
print(book.title)
b2=Book(title="asd",author="马")
print(book==b2)

