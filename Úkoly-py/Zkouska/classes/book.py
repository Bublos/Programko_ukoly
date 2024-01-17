class Book:
    def __init__(self,book:str) -> None:
        self.id,self.name,self.author,self.available= book.split(";")
    def lt(self,other)->bool:
        return self.author<other
    def eq(self,other)->bool:
        return self.id==other
    def set_id(self, id):
        self.id = id
    def repr(self) ->str:
        return (f"{self.id};{self.name};{self.author};{self.available}")
    def __str__(self) -> str:
        return self.repr()