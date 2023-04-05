from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    author = models.CharField(max_length=100) 
    is_published = models.BooleanField(default=True) 
    is_active = models.BooleanField(default=True)
   
    
    
    
    # def __str__(self):
    #     return self.name
    
    
    class Meta:
        db_table = "book"
        
    # def show_details(self):
    #     return f" Name is:   {self.name}\n Quantity is:   {self.qty}\n Price is:   {self.price}\n Author is:   {self.author}\n Published:   {self.is_published}"  
    
    #-----------------------------custom model-----------------------------------------------
    
 