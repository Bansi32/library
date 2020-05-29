class book:
    def __init__(self):
        self.author=''
        self.title=''
        self.price=0
    def read(self):
        self.title=input('Enter the title of the book:')
        self.author=input('Enter the name of the author:')
        self.price=float(input('Enter the price:'))
                          
    def display(self):
        print('Title name:',self.title)
        print('Author name:',self.author)
        print('Price:',self.price)
        print('\n')
books=[]
print("enter \'y\' if you want to select the below option or else enter -1 for exit:")
ch=input("enter the choice:")
while(1):
    if(ch=='y'):
        print('''
1. Add New Books
2. Display Books''')
        choice=int(input("enter the choice:"))
        print('\n')
        if(choice==1):
            a=book()
            a.read()
            books.append(a)
            print('\n')

        elif(choice==2):
            for i in books:
                i.display()
        else:
            print("invalid choice")
    
    else:
        print("you choose to exit")
        break
    ch=input("do you want to continue:")
print("BYE")
