
from django.shortcuts import render
from .models import Goods

def index(request):
    m=Goods.objects.filter(goods_idx_b=6)
    context={
        "m":m,

    }
    return render(request,'index.html',context)