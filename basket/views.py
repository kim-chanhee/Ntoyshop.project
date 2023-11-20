
from django.shortcuts import render,redirect
from django.http import HttpRequest
from ntoy.models import Goods, Basket

def basketinfo(request):   # 상품 집어 넣는것
    no=int(request.GET.get('no'))
    g=Goods.objects.get(goods_num=no)#상품번호
    bas_user_no=request.session['login']

    point=g.goods_c_price*0.1
    name=g.goods_name
    price=g.goods_c_price
    image=g.goods_image

    try:
        a=Basket.objects.create(bas_user_no=bas_user_no,bas_product_no=g)#회원,상품 번호bas_user_no=request.session['login']
        return redirect('/basket/basket')
    except Exception as e:
        print(e)

    context={
        'image':image,
        'point':point,
        'name':name,
        'price':price
    }

    return render(request,'basket/basket.html',context)


def basket(request):                # 상단 nav바 누르면 장바구니 들어가는 것
  
    b=Basket.objects.filter(bas_user_no=request.session['login'])
    p=0.01
    context={
        'b':b,
        "p":p
    }

    return render(request,'basket/basket.html',context)

def delete(request:HttpRequest):    #삭제
    no = int(request.GET.get("no"))

    try:
        Basket.objects.filter(bas_idx=no).delete()
        msg = "삭제되었습니다."
    except Exception as e:
        print(e)
    
    context={
        'msg' : msg
    }

    return render(request,"basket/delete.html",context)

