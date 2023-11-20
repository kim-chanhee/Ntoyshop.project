from urllib import response
from django.shortcuts import render
from django.http import HttpRequest
from ntoy.models import Delivery,Payment,Card,Member,Goods,Ttable
import datetime

# Create your views here.

def payment(request):
    c=Card.objects.all()
    no=int(request.POST.get('no'))
    print(type(no))
    # price=Goods.objects.goods_sale_price(goods_num=no)
    # point=price*0.01

    m=Goods.objects.get(goods_num=no)
    price=Goods.objects.get(goods_num=no).goods_sale_price
    count=int(request.POST.get('count'))
    point=int(price*0.01)*count

    p=m.goods_sale_price*(count)+2500
    print(count)
    print(point)
    context={
        "c":c,
        "m":m,
        "p":p,
        "count":count,
        "point":point
       
        # "point":point
    }
    return render(request,'pay/pay.html',context)

def checkpay(request:HttpRequest):
     
    a=Member.objects.get(user_no=request.session['login'])
    pay_paymethod_no=request.POST.get("method")
    b=int(request.POST.get("cardcompany"))
    pay_card_no=Card.objects.get(card_idx=b)
    pay_card_num=request.POST.get("cardNum")
    no=int(request.POST.get('no'))
    c=Goods.objects.get(goods_num=no)
    count=int(request.POST.get('count'))
    
    d=Member.objects.get(user_no=request.session['login'])
    e=Goods.objects.get(goods_num=no)
    del_name=request.POST.get("del_name")
    del_tel1=request.POST.get("del_tel1")
    del_tel2=request.POST.get("del_tel2")
    del_add_no=request.POST.get("postcode")
    del_addr=request.POST.get("addr")
    del_addr_plus=request.POST.get("detailAddr")
    del_order_text=request.POST.get("message")
    del_cod=request.POST.get("del_chlice")
    choice=request.POST.get("del_choice")
    stock=int(request.POST.get("stock"))
    rstock=Goods.objects.get(goods_num=no).goods_stock-stock
    f=Goods.objects.filter(goods_num=no)
    sale_price=e.goods_sale_price
    print(sale_price)
    n=datetime.datetime.now()


    point=int(request.POST.get("point"))
    rpoint=Member.objects.get(user_no=request.session['login']).point+point
    g=Member.objects.filter(user_no=no)
    msg = None
    check = False
    
    print(type(count))
    try:
        Payment.objects.create(pay_user_no=a,pay_card_no=pay_card_no,pay_card_num=pay_card_num,pay_paymethod_no=pay_paymethod_no,pay_product_no=c,pay_amount=count,pay_price=sale_price,pay_join_date=n)
        Delivery.objects.create(del_user_no=d,del_goods_num=e,del_name=del_name,del_tel1=del_tel1,del_tel2=del_tel2,del_add_no=del_add_no,del_addr=del_addr,del_addr_plus=del_addr_plus,del_order_text=del_order_text,del_cod=del_cod,del_cost=2500,del_situ=0)
        f.update(goods_stock=rstock)
        g.update(point=rpoint)
        Ttable.objects.create(t_name="상품",t_money=int(c.goods_sale_price*count))

        
        
        msg="결제가 완료되었습니다"
    except Exception as e:
        msg="다시해보자!"
        print(e)
    
    
    context = {
        'msg' : msg,
        'check' : check,
       
    }
    
    return render(request,'pay/checkpay.html',context)

def payresult(request:HttpRequest):
    payment=Payment.objects.filter(pay_user_no=request.session['login'])
    context={
        'payment':payment
    }
    return render(request,'pay/payresult.html',context)
    