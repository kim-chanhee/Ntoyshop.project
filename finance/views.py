
from django.shortcuts import render
from ntoy.models import Admin, Salary,Ttable,Payment,Goods
import datetime


# Create your views here.

def flist(request):
    return render(request,'finance/flist.html')

def list(request):

    return render(request,'finance/list.html')

def manage(request):
    s=Salary.objects.all()
    context={
        "s":s
    }
    return render(request,'finance/manage.html',context)


def salary(request):
    a=Admin.objects.all()
    context={
        "a":a
    }
    return render(request,'finance/salary.html',context)

def salaryResult(request,no):
    n=datetime.datetime.now()

    admin = Admin.objects.get(admin_idx=no)
    
    sa=3500000
    ye=334510
    bo=3165490


    
    try:
        Salary.objects.create(s_name=admin.admin_name,s_date=n)
        Ttable.objects.create(t_name="급여",t_money=sa)
        Ttable.objects.create(t_name="예수금",t_money=ye)
        Ttable.objects.create(t_name="보통예금",t_money=bo)
        msg="급여지급 완료"
    except Exception as e:
        print(e)
        msg="실패"

    context={
        "msg":msg
    }
    return render(request,'finance/salaryResult.html',context)

def sDelete(request):
    no=request.GET.get("no")
    sa=3500000
    ye=334510
    bo=3165490

    s=Salary.objects.filter(s_no=no)
    

    try:
        s.delete()
        Ttable.objects.create(t_name="급여",t_money=-sa)
        Ttable.objects.create(t_name="예수금",t_money=-ye)
        Ttable.objects.create(t_name="보통예금",t_money=-bo)
        
        msg="삭제완료"
    except Exception as a:
        msg="실패"
        print(a)
    context={
        "msg":msg
    }

    return render(request,'finance/deleteResult.html',context)

def t(request):
    s="급여"
    f="예수금"
    z="보통예금"
    pp="상품"
    a=Ttable.objects.filter(t_name=s)
    b=0
    for i in a:
        b+=i.t_money

    c=Ttable.objects.filter(t_name=f)
    d=0
    for i in c:
        d+=i.t_money

    o=Ttable.objects.filter(t_name=z)
    q=0
    for i in o:
        q+=i.t_money


    pro=Ttable.objects.filter(t_name=pp)
    aa=0
    for i in pro:
        aa+=i.t_money



    # for i in h:
    #     pp=pp+i
    context={
        "b":b,
        "d":d,
        "q":q,
        "aa":aa
    }



    return render(request,'finance/t.html',context)