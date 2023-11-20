from ast import Return
from tkinter import E
from django.shortcuts import render, redirect
from ntoy.models import Delivery, Payment, Goods,Admin,Returns
from datetime import datetime

# Create your views here.
def order(request):    
   
    p=Payment.objects.filter(pay_user_no=request.session['login'])
    g=Goods.objects.all()
    d=Delivery.objects.filter(del_user_no=request.session['login'])
    n=datetime.now()

    context={
        "p":p,
        "g":g,
        'd':d
    }
    return render(request,'order/order.html',context)


def delete(request):
    no=request.GET.get('no')
    p=Payment.objects.filter(pay_idx=no)

    try:
        p.delete()
        msg="삭제되었습니다"

    except Exception as e:
        print(e)
        msg='실패'
    
    context={
        "msg":msg
    }

    return redirect('/order/')

def manage(request):
    if Admin.objects.get(admin_idx=request.session['manager']).admin_department_no==1 or Admin.objects.get(admin_idx=request.session['manager']).admin_department_no==4 or Admin.objects.get(admin_idx=request.session['manager']).admin_department_no==5:
        d=Delivery.objects.all()
        r=Returns.objects.all()
        context={
            'd':d,
            'r':r
        }
        return render(request,'order/manage.html',context)
    else:
        return render(request,'manager/hr/warning.html')

def delUpdate(request):
    no=request.GET.get('no')

    d=Delivery.objects.filter(del_idx=no)

    try:
        d.update(del_situ=1)
        return redirect('/order/manage')
    except Exception as a:
        print(a)
        return redirect('/order/manage')


def delDelete(request):
    no=request.GET.get('no')

    d=Delivery.objects.filter(del_idx=no)

    try:
        d.delete()
        return redirect('/order/manage')
    except Exception as a:
        print(a)
        return redirect('/order/manage')


def returns(request):
    no=request.GET.get('no')
    p=Payment.objects.get(pay_idx=no)
    n=datetime.now()
    context={
        "p":p,
        "n":n
    }
    return render(request,'order/returns.html',context)


def returnsResult(request):

    no=int(request.POST.get('no'))
    print(no)
    p=Payment.objects.get(pay_idx=no)
    d=datetime.now()
    t=request.POST.get('message')

    try:
        r=Returns.objects.create(re_payment_no=p,re_return_date=d,re_return_reason=t)
        msg="반품등록완료"
    except Exception as a:
        print(a)
        msg="실패"
    context={
        "msg":msg
    }

    return render(request,'order/returnsResult.html',context)

def reDelete(request):
    no=request.GET.get('no')
    print(no)
    r=Returns.objects.filter(re_idx=no)

    try:
        r.delete()
        return redirect('/order/manage/')
    except Exception as a:
        print(a)
        return redirect('/order/manage/')