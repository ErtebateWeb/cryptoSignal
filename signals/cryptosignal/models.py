from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



# Create your models here.
class binarysignal(models.Model):


    SymbolTitle = models.CharField(max_length=30)
    TimeFrame = models.CharField(max_length=30, default='1D')
    NowPrice = models.CharField(max_length=30)
    TriggerPrice = models.CharField(max_length=30)
    StopLoss = models.CharField(max_length=30)
    TakeProfit1 = models.CharField(max_length=30)
    TakeProfit2 = models.CharField(max_length=30, default='',null=True,blank=True)
    TakeProfit3 = models.CharField(max_length=30, default='',null=True,blank=True)
    TakeProfit4 = models.CharField(max_length=30, default='',null=True,blank=True)
    LivePrice = models.CharField(max_length=30, default='',null=True,blank=True)
    IsActive = models.BooleanField(default=True)

    #DateCreated = models.DateTimeField(default=datetime.now)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    #CreatedDate = models.DateTimeField(default=datetime.now)
    updatedDate = models.DateTimeField(default=datetime.now)

    Publishers = (
        ("Secret_army", "Secret_army"),
        ("mhfateminia", "mhfateminia"),
        ("peyman_gh", "peyman_gh"),
        ("Eslaaamiii", "Eslaaamiii"),
        ("Reza_Esfilar", "Reza_Esfilar"),
    )
    Publisher = models.CharField(max_length=30,choices=Publishers)
    Images = models.ImageField(default='', upload_to='images/', null=True,blank=True)
    #Images = models.FileField(default='', upload_to='/images/', null=True,blank=True)

    def __str__(self):
            return str(self.SymbolTitle)


class FavList(models.Model):


    User =models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    # User =models.CharField(max_length=30, blank=True, null=True, )
    SymbolTitle = models.ForeignKey(binarysignal, blank=True, null=True, on_delete=models.CASCADE)
    # TimeFrame = models.CharField(max_length=30, default='1D')
    # NowPrice = models.CharField(max_length=30)
    # TriggerPrice = models.CharField(max_length=30)
    # StopLoss = models.CharField(max_length=30)
    # TakeProfit1 = models.CharField(max_length=30)
    # TakeProfit2 = models.CharField(max_length=30, default='',null=True,blank=True)
    # TakeProfit3 = models.CharField(max_length=30, default='',null=True,blank=True)
    # TakeProfit4 = models.CharField(max_length=30, default='',null=True,blank=True)
    # LivePrice = models.CharField(max_length=30, default='',null=True,blank=True)
    IsActive = models.BooleanField(default=True)
    IsTriggered = models.BooleanField(default=False)
    IsStopLossed = models.BooleanField(default=False)
    IsTP1 = models.BooleanField(default=False)
    IsTP2 = models.BooleanField(default=False)
    IsTP3 = models.BooleanField(default=False)
    IsTP4 = models.BooleanField(default=False)
    CreatedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.SymbolTitle)