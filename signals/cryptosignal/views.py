from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import binarysignal
from .forms import SignalForm#SubmitSignals,
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# get user model ( class )
import os
import telegram_Api
import binance_price
User = get_user_model()

# @login_required(login_url='/login/')
def binary_list_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    binaries = binarysignal.objects.all().order_by('-id')
    # p=binance_price.get_price('BTCUSDT')
    # print(p)
    # print(type(binaries))
    # print(binaries)

    p=binance_price.get_Symbol_Price_Ticker()
    # print('p=',p)
    # for s in p:
    #     print(s['symbol'],s['price'])

    for obj in binaries:
        for s in p:
            #print(obj.SymbolTitle.replace("_", ""))
            sym=obj.SymbolTitle.replace("_", "")
            # print(s['sym']['price'])
            if (sym == s['symbol']):
                obj.LivePrice = s['price']
                obj.sym=sym
                # print('symbol=',sym,' AND s.symbol=',s['symbol'],' AND s.price=',s['price'])


    # for obj in binaries:
    #     # print(obj.SymbolTitle)
    #     print(obj.SymbolTitle.replace("_", ""))
    #     # print(binance_price.get_price(obj.SymbolTitle.replace("_", "")))
    #     obj.LivePrice = binance_price.get_price(obj.SymbolTitle.replace("_", ""))
    #     print('---------------------------------')



    context = {
        "object_list": binaries,
        "title": 'Signals List view'
    }
    return render(request, "signal/signal_list.html", context)


def submit_signals(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    form = SignalForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        picpath = form.cleaned_data.get("Images")
        picpath = str(picpath)

        ST = form.cleaned_data.get("SymbolTitle")
        TF = form.cleaned_data.get("TimeFrame")
        NP = form.cleaned_data.get("NowPrice")
        Tr = form.cleaned_data.get("TriggerPrice")
        SL = form.cleaned_data.get("StopLoss")
        TP1 = form.cleaned_data.get("TakeProfit1")
        TP2 = form.cleaned_data.get("TakeProfit2")
        TP3 = form.cleaned_data.get("TakeProfit3")
        TP4 = form.cleaned_data.get("TakeProfit4")
        Pub = form.cleaned_data.get("Publisher")
        message= "💰 : {}\n⏳ TF: {}\n💵 NP: {}\n🔫 Tr : {}\n⛔️ SL : {}\n✅ Tp1 : {}   🧮 {}\n✅ Tp2 : {}   🧮 {}\n✅ Tp3 : {}   🧮 {}\n✅ Tp4 : {}   🧮 {}\nPublisher:@{}".format(ST,TF,NP,Tr,SL,TP1,None,TP2,None,TP3,None,TP4,None,Pub)
        form.save()
        telegram_Api.sendp(chat_id='@crypto_monarch', photo=open('images\images\\' + picpath, 'rb'), caption=message)
        return redirect('/cryptosignal/')

    context = {
        "title": 'Submit Signals',
         "form": form
            }

    return render(request, "signal/submit_signals.html", context)


def binary_detail_view(request, id=None, *args, **kwargs):
    binaries = binarysignal.objects.get(id=id)
    # binaries = get_object_or_404(binarysignal, id=id)
    print(binaries)
    context = {
        "objects": binaries
    }
    print(context)
    return render(request, "signal/signal_detail.html", context)
