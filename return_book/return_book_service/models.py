from django.db import models


class ReturnBook(models.Model):
    idreturn = models.AutoField(primary_key=True)
    idborrow = models.IntegerField()
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
    date_return = models.DateField()
    total_money = models.DecimalField(max_digits=10, decimal_places=2)

   

