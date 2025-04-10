# 1. Practise question


class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade


    def display(self):
        print(f"the student name is {self.name}, and he is {self.age}, and he got grade {self.grade}")



stu1 = student("Ritu Raj",18,"A")
stu2 = student("Mahi Singh", 19,"B")



stu1.display()
stu2.display()





# 2 Practise Question 2

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed


    def bark(self):
        print(f"woof! I am {self.name} the {self.breed}")



d1 = Dog("Tommy", "Desi")
d2 = Dog("Goldy","German")
d3 = Dog("Silky","American")


#calling
d1.bark()
d2.bark()
d3.bark()


# 3. pratise Question 


class book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        pass

    def summary(self):
        return print (f"The book {self.title} by {self.author} has {self.pages} pages.")


b1 = book ("The kite Runner","Adil",244)
b2 = book ("The girl in room 105","chetan bhagat",222)


b1.summary()
b2.summary()


# 4. Practise Questions

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")

acc1 = BankAccount("Ritu Raj", 1000)
acc1.display_balance()
acc1.deposit(500)
acc1.withdraw(300)
acc1.withdraw(1500)  


# 5. Practise Question 

class Movie:
    def __init__(self,title,genre,rating):
        self.title = title
        self.genre = genre 
        self.rating = rating


    def show_details(self):
        print(f"Title ={self.title}\n Genre = {self.genre}\n Rating =  {self.rating}")


m1 = Movie("Beyonds the Clouds","Satire","5 stars")
m2 = Movie("Joyland","Family Drama","4 Stars")


m1.show_details()
m2.show_details()

