from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import telegram_Api



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
    TelegramMessageId = models.CharField(max_length=30, default='',null=True,blank=True)



    def save(self , *args , **kwargs):
        # self.timestamp = datetime.fromtimestamp(self.date)
        print('send Telegram')


        picpath = self.Images
        picpath = str(picpath)

        TF =self.TimeFrame
        NP =self.NowPrice
        Tr =self.TriggerPrice
        SL =self.StopLoss
        ST =self.SymbolTitle
        TP1 =self.TakeProfit1
        TP2 =self.TakeProfit2
        TP3 =self.TakeProfit3
        TP4 =self.TakeProfit4
        # Pub =self.Publisher
        message = "💰 : {}\n\n⏳ TF: {}\n\n💵 NP: {}\n\n🔫 Tr : {}\n\n⛔️ SL : {}\n\n✅ Tp1 : {}   🧮 {}\n\n✅ Tp2 : {}   🧮 {}\n\n✅ Tp3 : {}   🧮 {}\n\n✅ Tp4 : {}   🧮 {}".format(
            ST, TF, NP, Tr, SL, TP1, None, TP2, None, TP3, None, TP4, None)

        res = telegram_Api.sendp(chat_id='@crypto_monarch', photo=open('images\images\\' + picpath, 'rb'),
                                 caption=message)
                                 # caption=message,rep='81')
        print('Telegram result=', res.message_id)
        self.TelegramMessageId = res.message_id











        # ts=int(datetime.timestamp(self.date)*1000)
        # print('ts =',ts)
        # print('ts type=',type(ts))
        # self.timestamp = ts
        # # self.text = ts
        # # ts=int(datetime.datetime.timestamp(self.date))
        # # print('ts=',ts)
        # print(self.timestamp)
        print ('SAVE!!!')

        super(binarysignal,self).save(*args,**kwargs)
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