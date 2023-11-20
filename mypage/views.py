
# Create your views here.
from django.shortcuts import render, redirect
from ntoy.models import Member
from django.http import HttpRequest

# Create your views here.

def mypage(request:HttpRequest):
    member=Member.objects.get(user_no=request.session['login'])
    context={
        'member':member
    }
    return render(request,'mypage/mypage.html',context)


def update(request):
    member=Member.objects.get(user_no=request.session['login'])

    context={
        'member':member
    }
    return render(request,'mypage/update.html',context)

def updateResult(request):
    name=request.POST.get("name")
    id=request.POST.get("id")
    pw=request.POST.get("pw")
    phone=request.POST.get("phone")
    email=request.POST.get("email")
    addr=request.POST.get("addr")
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
    
    try:
        Member.objects.filter(user_id=id).update(user_name=name,user_pw=pw,phone=phone,email=email,e_agreement=agree_email,n_agreement=agree_news,p_agreement=agree_push,addr=addr)
        msg='수정에 성공하였습니다'
    except Exception as e:
        msg='수정에 실패했습니다'
        print(e)
    
    context={
        'msg':msg
    }
    return render(request,'mypage/updateResult.html',context)

def unregister(request):

    return render(request,'mypage/unregister.html')

def unResult(request):

    m=Member.objects.filter(user_no=request.session['login'])

    try:
        m.delete()
        msg="탈퇴가 완료되었습니다"
        request.session.pop('login') # 세션에 저장된 하나의 키와 밸류 삭제.
    #print(request.session['login'])
    #request.session.flush() # 세션의 저장된 정보 초기화
    except Exception as a:
        print(a)
        msg="탈퇴 실패"

    context={
        "msg":msg
    }

    return render(request,'mypage/unResult.html',context)