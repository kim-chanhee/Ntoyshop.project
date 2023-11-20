from django.shortcuts import render,redirect
from django.http import HttpRequest
from ntoy.models import Goods

def search(request:HttpRequest):

    goods=Goods.objects.filter(goods_name__contains=request.GET.get('search'))
    print(goods)

    context={
        'goods' : goods
    }

    return render(request,'search/search.html',context )
