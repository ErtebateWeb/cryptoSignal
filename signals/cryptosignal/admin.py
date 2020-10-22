from django.contrib import admin
from cryptosignal.models import binarysignal,FavList
# Register your models here.

class AdminMode(admin.ModelAdmin):
    list_display = ['SymbolTitle',
    'NowPrice' ,
    'TimeFrame' ,
    'StopLoss' ,
    'TriggerPrice' ,
    'TakeProfit1' ,
    'TakeProfit2' ,
    'TakeProfit3' ,
    'TakeProfit4',
    'CreatedDate',
    'updatedDate',
    'Publisher',
    'Images']
    search_fields=['SymbolTitle',
    'CreatedDate',
    'updatedDate',
    'Publisher',
    ]
    list_filter = ['CreatedDate']
class FavAdminMode(admin.ModelAdmin):
    list_display = ['id','User','SymbolTitle','IsTriggered','IsStopLossed','IsTP1']
admin.site.register(binarysignal,AdminMode)
admin.site.register(FavList,FavAdminMode)

