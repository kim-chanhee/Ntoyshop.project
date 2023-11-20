from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest
from ntoy.models import Member
from datetime import datetime

# Create your views here.
def join(request):
    return render(request,'member/join.html')


def checkJoin(request:HttpRequest):
    name=request.POST.get("name")
    id=request.POST.get("id")
    pw=request.POST.get("pw")
    phone=str(request.POST.get("tel1"))+str(request.POST.get("tel2"))+str(request.POST.get("tel3"))
    email=request.POST.get("email")

    agree_email=request.POST.get("agree_email")
    if agree_email==None or agree_email=='':
        agree_email=0
    else:
        agree_email=1
    agree_news=request.POST.get("agree_news")
    if agree_news==None or agree_news=='':
        agree_news=0
    else:
        agree_news=1
    agree_push=request.POST.get("agree_push")
    if agree_push==None or agree_push=='':
        agree_push=0
    else:
        agree_push=1
    agree_terms=request.POST.get("agree_terms")

    date=datetime.now()


    try:
        Member.objects.create(user_name=name,user_id=id,user_pw=pw,join_date=date,phone=phone,email=email,point=0,e_agreement=agree_email,n_agreement=agree_news,p_agreement=agree_push)
        msg='성공'

    except Exception as e:
        print(e)
        msg='실패'
        
    context = {
            "msg" : msg
        }

    return render(request,'member/checkJoin.html',context)

def login(request):
    return render(request,'member/login.html')