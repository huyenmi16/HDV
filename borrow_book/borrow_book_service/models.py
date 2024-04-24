from django.db import models


class BorrowBook(models.Model):
    idborrow = models.AutoField(primary_key=True)
    idbook = models.IntegerField()
    name_cust = models.CharField(max_length=200)
    cccd_cust = models.CharField(max_length=12)
    sdt = models.CharField(max_length=15)  
    address_cust = models.TextField()
    quantity = models.IntegerField()
    address_lib = models.TextField()
    date_borrow = models.DateField()
    date_return_expected = models.DateField()
    status = models.TextField()

