lst =['science','maths','english','hindi','sst','sanskrit']

def show_books():
    c =1
    for i in lst:
        print(f'{c}---{i}\n')
        c +=1

books ={'gaurav':['maths']}
def borrow():
    name =input('enter your name\n').strip().lower()
    book= input('enter book name\n')
    if book in lst:
        if name in books:
            books[name].append(book)
            print('book has been issued')
        else:
            books[name]=[book]
    else:
        print('book did not found')

def all_book():
    if books:
        for name,book in books.items():
            print(f'\n"{name.title()}" = ',end=' ')
            for bo in book:
                print(bo,end=',')
    else:
        print('no books issued')



def return_book():
    name=input()
    if name in books:
        for i in books:
            if name==i:
                if len(books[i])==1:
                    bb=input('book name')
                    books.pop(i)
                    return
                else:
                    bb=input('book name')
                    if bb in books[i]:
                        books[i].remove(bb)
    else:
        print('no book has been issued or enter correct name again')
    
    


def main():
    menu="""
    1.List all books
    2.Borrow book
    3.Return books
    4.All books
    5.Exit
    """
    print(menu)
    choose =input(' enter you choice')
    if choose =='1':
        show_books()
        input('enter any key')
        main()
    elif choose =='2':
        show_books()
        borrow()
        input('enter any key')
        main()
    elif choose =='3':
        return_book()
        input('enter any key')
        main()
    elif choose=='4':
        all_book()
        input('enter any key')
        main()
    elif choose =='5':
        exit(0)
    else:
        print('invalid choice')
        main()
main()       
        
