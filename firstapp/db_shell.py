from firstapp.models import Book
from django.contrib.auth.models import User


# print(Book.objects.filter(name= "dheeraj"))

# a1 = Book.objects.get(id=3).show_details()
# print(a1)

# a = Book.objects.create(name="dheeraj", qty= 40 , price= 450 , author= "Unknown", is_published= True)
# print(a)

###updating existing database values
# for i in range(1,5):
#      obj = Book.objects.filter(id= i).update(price = "100")
# print(obj)

# obj = Book.objects.filter(id= "5").update(id="4")

# or

# obj = Book.objects.get(id= "4")
# obj.name = "Book4"
# obj.save()

#--------------------------------------------------------------------------------------

# obj = Book.objects.filter(id=4).update(author = "N. Tesla")
    # print(obj)

# obj = Book.objects.filter(id= 2).update(price = "200")
# obj = Book.objects.filter(id= 3).update(price = "300")
# obj = Book.objects.filter(id= 4).update(price = "400")
# print(obj)




# obj = Book.objects.filter(id= 6).update(id = "5")
# print(obj)

# book_obj = Book.objects.filter(id= "9").update(id = "8")
# print(book_obj)

# is_published = "False"


# book_obj = Book.objects.create(id=7,name="Book7",qty= 100,price= 700,author= "S.bose",is_published= True)
# print(book_obj)

# obj = Book.objects.get(id = "11")
# obj.delete()
# obj = Book.objects.get(id = "12")
# obj.delete()
# obj = Book.objects.get(id = "13")
# obj.delete()

# obj = Book.objects.get(id= "14")
# obj.delete()

# print(Book.objects.all())
# exec(open(r'S:\django\projects\Library\firstapp\db_shell.py').read())
# exec(open(r'S:\django\projects\Library\firstapp\db_shell.py').read())


# print(Book.objects.get(id= "1"))
# print(Book.objects.get(id = 4).show_details())

# books = Book.objects.all().filter(is_active = False) #for check inactive books csv
# exec(open(r'S:\django\projects\Library\firstapp\db_shell.py').read())
# import openpyxl

# path = "C:/Users/dheeraj/Desktop/books.xlsx"

# wb_obj = openpyxl.load_workbook(path)

# sheet_obj = wb_obj.active

# for i in range(1,51):
#     author_list = sheet_obj.cell(column = 2, row = i).value
#     books = sheet_obj.cell(column = 1, row = i).value
#     Book_lst = str(books)[1:-1]
#     authors = author_list.splitlines()
#     author_list_ = str(authors)[1:-1]

#     obj = Book.objects.create(id = f'{i}', name= Book_lst,qty= 100+i,price= 700+i,author= author_list_ ,is_published= True)
        

# import openpyxl

# path = "C:/Users/dheeraj/Desktop/States.xlsx"

# load = openpyxl.load_workbook(path)

# wb_obj = load.active

# sheet_obj_A = wb_obj["A"]
# sheet_obj_B = wb_obj["B"]

# States_list = []
# for cell in sheet_obj_A:
#     cell1 = (cell.value)
#     States_list.append(cell1)
    
    
# Capital_list = []
# for cell in sheet_obj_B:
#     cell2 = (cell.value)
#     Capital_list.append(cell2)    
    
# States_list = tuple(States_list)



# print(States_list[13])
# for i in range(0,34):
#     obj = Book.objects.create(id = 51+i, name= States_list[i],qty= 150+i,price= 750+i,author= Capital_list[i] ,is_published= True)


# for i in range(82,84):
#     Book.objects.get(id=f'{i}').delete()

# for i in range(85,169):
#     Book.objects.filter(id= i).update(id=(i-84))
# Book.objects.filter(id=2 ).update(id=85) #for update id 

# for i in range(253,421):
#     Book.objects.filter(id= i).update(id=(i-252))
# Book.objects.filter(id=2 ).update(id=85) #for update id 

 #for bulk delete 
# Book.objects.all().delete()







