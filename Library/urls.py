"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from firstapp import views
from Users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.home, name="home_page"),
    path('books/', views.show_books, name="all_active_books"),
    path('update/<int:id>/', views.update_book, name="update_book"),
    path('delete/<int:id>/', views.delete_book, name="delete_book"),
    path('soft-delete/<int:id>/', views.soft_delete_book, name="soft_delete_book"),
    path('inactive-books/', views.show_inactive_books, name="all_inactive_book"),
    path('restore-book/<int:id>', views.restore_book, name="restore_book"),
    path('debug__/', include('debug_toolbar.urls')),
    
    # path('book-form/', views.book_form, name="book_form"),
    # path('sibtc-form/', views.sibtc, name="sibtc"),
    
    
    #User url
    path("register/", user_views.register_request, name="register"),
    path("login/", user_views.login_request, name="login_user"),
    path("logout/", user_views.logout_user, name="logout_user"),
    
    path("create-csv/", views.create_csv, name="create_csv"),
    path("Active-books/", views.Active_books, name="Active_books"),
    path("Inactive-books/", views.Inactive_books, name="Inactive_books"),
    path("two-sheets/", views.two_sheets, name="two_sheets"),
    path("upload-csv/", views.upload_csv, name="upload_csv"),
    path('book-list/', views.book_list, name='book_list'), #for raw query not done
 
 
  
]

