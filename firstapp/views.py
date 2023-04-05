import csv
import logging

import openpyxl
import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import HttpResponse, redirect, render
from django.views.decorators.csrf import csrf_exempt
from openpyxl import *

from .forms import AddressForm, BookForm
from .models import Book

# from django.middleware.csrf import get_token

# Create your views here.


@csrf_exempt
@login_required
def home(request):  # http request
    # csrf_token = get_token(request)
    # print(csrf_token)
    # return render(request, 'my_template.html', {'csrf_token': csrf_token})
    # Creating, Updating ---
    if request.method == "POST":
        data = request.POST
        bid = data.get("book_id")
        name = data.get("book_name")
        qty = data.get("book_qty")
        price = data.get("book_price")
        author = data.get("book_author")
        is_pub = data.get("book_is_pub")
        print(request.POST)
        if is_pub == "Yes":
            is_pub = True
        else:
            is_pub = False

        if not bid:
            Book.objects.create(name=name, qty=qty, price=price,
                                author=author, is_published=is_pub)
        else:
            book_obj = Book.objects.get(id=bid)
            book_obj.name = name
            book_obj.qty = qty
            book_obj.price = price
            book_obj.author = author
            book_obj.is_published = is_pub
            book_obj.save()

        return redirect('home_page')
        # return HttpResponse ("Success...!")
    elif request.method == "GET":
        # print(request.GET) #get query params = parameters
        return render(request, "old_home.html", context={"person_name": "Dheeraj"})


@login_required
def show_books(request):
    return render(request, "show_books.html", {"books": Book.objects.filter(is_active=True), "active": True})


@login_required
def update_book(request, id):
    book_obj = Book.objects.get(id=id)
    return render(request, "home.html", context={"single_book": book_obj})


@login_required
def delete_book(request, id):
    book_obj = Book.objects.get(id=id).delete()
    return redirect("all_active_books")


@login_required
def soft_delete_book(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_active = False
    book_obj.save()
    return redirect("all_active_books")


@login_required
def show_inactive_books(request):
    return render(request, "show_books.html", {"books": Book.objects.filter(is_active=False), "inactive": True})


@login_required
def restore_book(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_active = True
    book_obj.save()
    return redirect("all_active_books")


# def book_form(request):
#     return render(request, "book_form.html", {"form": UserCreationForm()})

# simpleisbetterthancomplex - refer this website for django crispy forms

@login_required
def sibtc(request):
    return render(request, "sibtc.html", {"form": AddressForm()})


@login_required
def book_form(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponse("Successfully Registered!!!")

    else:
        context = {"form": form}
        return render(request, "book_form.html", context=context)


# csv file read write


def create_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="test.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'qty', 'price', 'author',
                    'is_published', 'is_active'])

    books = Book.objects.all().values_list('name', 'qty', 'price',
                                           'author', 'is_published', 'is_active')
    for book in books:
        writer.writerow(book)

    return response


def Active_books(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ActiveBooks.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'qty', 'price', 'author',
                    'is_published', 'is_active'])

    book1 = Book.objects.all().filter(is_active=True)
    books = book1.values_list('name', 'qty', 'price',
                              'author', 'is_published', 'is_active')
    for book in books:
        writer.writerow(book)

    return response


def Inactive_books(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="InActiveBooks.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'qty', 'price', 'author',
                    'is_published', 'is_active'])

    book1 = Book.objects.all().filter(is_active=False)
    books = book1.values_list('name', 'qty', 'price',
                              'author', 'is_published', 'is_active')
    for book in books:
        writer.writerow(book)

    return response

# def two_sheets(request):
#     #Fetching books from database
#     books = Book.objects.all()
#     active_books = books.filter(is_active=True)
#     inactive_books = books.filter(is_active=False)

#     # Create CSV file
#     response = HttpResponse(content_type='text/csv')
#     response['content-Disposition'] = 'attachment; filename=twosheet.csv'

#     writer = csv.writer(response)

#     # Write the active books to the first sheet
#     writer.writerow(['name', 'qty', 'price', 'author', 'is_published', 'is_active'])
#     for book in active_books:
#         writer.writerow([book.name, book.qty, book.price, book.author, book.is_published, book.is_active])
#     response.write('\n')

#     # Write the inactive books to the second sheet
#     writer.writerow(['name', 'qty', 'price', 'author', 'is_published', 'is_active'])
#     for book in inactive_books:
#         writer.writerow([book.name, book.qty, book.price, book.author, book.is_published, book.is_active])

#     return response

# def two_sheets(request):
#     #Fetching books from database
#     books = Book.objects.all()
#     Active_books = books.filter(is_active= True)
#     Inactive_books = books.filter(is_active= False)

#     #Create Excel file
#     response = HttpResponse(content_type='text/csv')
#     response['content-Disposition'] = 'attachment; filename= twosheet.xlsx'


#     writer = pd.ExcelWriter(response,engine='xlsxwriter')


#     df_active = pd.DataFrame(list(Active_books.values_list('name', 'qty', 'price','author', 'is_published','is_active')))
#     df_active.columns = ['name', 'qty', 'price','author', 'is_published','is_active']
#     df_active.to_excel(writer,sheet_name='Active Books', index=False)

#     df_inactive = pd.DataFrame(list(Inactive_books.values_list('name', 'qty', 'price','author', 'is_published','is_active')))
#     df_inactive.columns = ['name', 'qty', 'price','author', 'is_published','is_active']
#     df_inactive.to_excel(writer,sheet_name='Inactive Books', index= False)

#     writer.save()
#     return response

# two_sheets = csrf_exempt(two_sheets)

# you can define headers in to_excel line also


def upload_csv(request):
    file = request.FILES["csv_file"]
    data = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(data)
    lst = []
    for element in reader:  # True string mein aata isliye isko karna pada
        is_pub = element.get("is_published")
        if is_pub == "TRUE":
            is_pub = True

        # same as is_published , is_active ke liye bhi
        is_act = element.get("is_active")
        if is_act == "TRUE":
            is_act = True

        lst.append(Book(name=element.get("name"), qty=element.get("qty"), price=element.get(
            "price"), author=element.get("author"), is_published=is_pub, is_active=is_act))

    Book.objects.bulk_create(lst)
    return HttpResponse("Success")


# """Optimize version of upload csv"""
# import io
# def upload_csv(request):
#     file = request.FILES["csv_file"]
#     file_data = io.StringIO(file.read().decode())
#     reader = csv.DictReader(file_data)
#     books = [Book(name=row["name"], qty=row["qty"], price=row["price"], author=row["author"], is_published=row["is_published"]=="TRUE", is_active=row["is_active"]=="TRUE") for row in reader]
#     Book.objects.bulk_create(books)
#     return HttpResponse("Success")


"""With pandas"""
import pandas as pd
from django.http import HttpResponse


    



def two_sheets(request):
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=books.xlsx'
    wb = openpyxl.Workbook()

    # create active books worksheet
    active_ws = wb.active
    active_ws.title = "Active Books"
    active_books = Book.objects.filter(is_active=True)

    # add header row
    active_ws.append(['name', 'qty', 'price', 'author',
                     'is_published', 'is_active'])

    # add data rows
    for book in active_books:
        active_ws.append([book.name, book.qty, book.price,
                         book.author, book.is_published, book.is_active])

    # create inactive books worksheet
    inactive_ws = wb.create_sheet("Inactive Books")

    # add header row
    inactive_ws.append(['name', 'qty', 'price', 'author',
                       'is_published', 'is_active'])

    # add data rows
    inactive_books = Book.objects.filter(is_active=False)
    for book in inactive_books:
        inactive_ws.append([book.name, book.qty, book.price,
                           book.author, book.is_published, book.is_active])

    wb.save(response)
    return response



# def book_list(request):
    
    # book_list = Book.objects.all()
    # with connection.cursor() as cursor:
    #  cursor.execute("SELECT * FROM library_project.book")
    #  book_list = cursor.fetchall()
    # return render(request, 'book_list.html', {'book_list': book_list})
  
#book list raw query not done   
from .models import Book


def book_list(request):
    book_list = Book.objects.all()
    return render(request, 'book_list.html', {'book_list': book_list})

