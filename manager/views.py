from calendar import c
from multiprocessing import context
from tkinter import E
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

from ntoy.models import Admin
from ntoy.models import Member
from ntoy.models import CategoryA
from ntoy.models import CategoryB
from ntoy.models import Goods
from ntoy.models import Card

# Create your views here.
def index(request):
    a=Admin.objects.all()
    return render(request,'manager/index.html')

def login(request:HttpRequest):
    id = request.GET.get("id") # ''
    check = False
    if id == '' or id == None:
        id = request.COOKIES.get("ckid")
        if id != None:
            check = True

    context = {
        'id' : id,
        "check" : check,
    }

    return render(request,'manager/login.html',context);

def checkLogin(request:HttpRequest):
    id = request.POST.get("id")
    password = request.POST.get("password")

    msg = None
    check = False
    
    try:
        admin = Admin.objects.get(admin_id=id,admin_pw=password) # and
        #print(member.query) # 지금 작성한 쿼리문 반환...
    except Exception as e:
        msg = "아이디 혹은 비밀번호가 잘못되었습니다."
    else:
        check = True
        msg = admin.admin_name + "님이 로그인하셨습니다."

        #로그인 처리
        request.session['manager'] = admin.admin_idx

    context = { 'msg' : msg , 'check' : check }
    
    response = render(request,'manager/result.html',context)

    if check:
        ckid = request.POST.get("ckid") #파라미터의 ckid

        ck = request.COOKIES.get('ckid') # 쿠키파일중에 파일명이 ckid 찾기

        
        if ckid != None: #아이디 기억하기 체크된 상태
            if ck == None:
                #쿠키파일 생성...
                response.set_cookie("ckid",id,max_age=60*60*10) #생성
                # ckid라는 파일명으로 로그인한 아이디를 컨텐츠에 넣고 유지시간 10시간으로 쿠키파일 설정.
            elif ck != id: #쿠키파일의 아이디와 로그인된 아이디가 다른경우
                response.set_cookie("ckid",id,max_age=60*60*10) # 만들어진 상황이면 쿠키파일 변경
        else: # 아이디 기억하기 체크 해제된 상태
            if ck == id: # 쿠키파일의 아이디와 로그인된 아이디가 같은경우
                response.delete_cookie("ckid") # 쿠키파일 삭제

        # response = HttpResponse()
        # if ckid != None: #아이디 기억하기 체크된 상태
        #     if ck == None:
        #         #쿠키파일 생성...
        #         response = render(request,'login/result.html')
        #         print(type(response))
        #         response.set_cookie("ckid",id,max_age=60*60*10) #생성
        #         # ckid라는 파일명으로 로그인한 아이디를 컨텐츠에 넣고 유지시간 10시간으로 쿠키파일 설정.
        #         return response
        #     elif ck != id: #쿠키파일의 아이디와 로그인된 아이디가 다른경우
        #         response = render(request,'login/result.html')
        #         print(type(response))
        #         response.set_cookie("ckid",id,max_age=60*60*10) # 만들어진 상황이면 쿠키파일 변경
        #         return response
        # else: # 아이디 기억하기 체크 해제된 상태
        #     if ck == id: # 쿠키파일의 아이디와 로그인된 아이디가 같은경우
        #         response = render(request,'login/result.html')
        #         print(type(response))
        #         response.delete_cookie("ckid") # 쿠키파일 삭제
        #         return response    
    return response

def logout(request:HttpRequest):
    request.session.pop('manager') # 세션에 저장된 하나의 키와 밸류 삭제.
    #print(request.session['login'])
    #request.session.flush() # 세션의 저장된 정보 초기화
    return redirect('/manager/')




def hr(request):

    if Admin.objects.get(admin_idx=request.session['manager']).admin_department_no==1 or Admin.objects.get(admin_idx=request.session['manager']).admin_department_no==3:
        return render(request,'manager/hr/hr.html')
    else:
        return render(request,'manager/hr/warning.html')

def join(request):
    return render(request,'manager/hr/adminJoin.html')

def checkjoin(request):
    id=request.POST.get('id')
    pw=request.POST.get('pw')
    name=request.POST.get('name')
    department=int(request.POST.get('department'))

    try:
        admin=Admin.objects.create(admin_id=id,admin_pw=pw,admin_name=name,admin_department_no=department)
        msg="등록되었습니다"
    except Exception as e:
        print(e)
        msg="실패"
    context={
        "msg":msg
    }
    return render(request,'manager/hr/checkJoin.html',context)

def goods(request):
    if Admin.objects.get(admin_idx=request.session['manager']).admin_department_no==1 or Admin.objects.get(admin_idx=request.session['manager']).admin_department_no==2 or Admin.objects.get(admin_idx=request.session['manager']).admin_department_no==4:
        return render(request,'manager/goods/goods.html')
    else:
        return render(request,'manager/hr/warning.html')


def manage(request):
    admin=Admin.objects.all()
    context={
        "admin":admin
    }
    return render(request,'manager/hr/manage.html',context)

def update(request):
    no=int(request.GET.get('no'))

    try:
        a = Admin.objects.get(admin_idx=no)
    except:
        a = None
    

    context={
        "a":a
    }
    return render(request,'manager/hr/adminUpdate.html',context)

def updateResults(request:HttpRequest):
    no= int(request.POST.get("no"))
    id=request.POST.get('id')
    pw=request.POST.get('pw')
    name=request.POST.get('name')
    department=int(request.POST.get('department'))

    try:
        Admin.objects.filter(admin_idx=no).update(admin_id=id,admin_pw=pw,admin_name=name,admin_department_no=department)
        msg="수정성공"
    except Exception as e:
        msg="실패"
        print(e)

    context={
        'msg':msg
    }

    return render(request,'manager/hr/updateResult.html',context)


def delete(request:HttpRequest):
    no = int(request.GET.get("no"))
    
    try:
        Admin.objects.filter(admin_idx=no).delete()
        msg = "삭제되었습니다."
    except:
        msg = "삭제되지 못했습니다."
    
    context = {
        "msg" : msg
    }

    return render(request,"manager/hr/delete.html",context)








#------------------------------------------------------------------------------------------
def cate(request):
    return render(request,'manager/goods/cate/cate.html')


def cateA(request):
    return render(request,'manager/goods/cate/cateA.html')

def cateAresult(request):
    name=request.POST.get('name')
    print(name)
    try:
        CategoryA.objects.create(a_name=name)
        msg="등록완료"
    except Exception as e:
        msg="등록실패"
        print(e)

    context={
        "msg":msg
    }
    return render(request,'manager/goods/cate/cateAresult.html',context)

def cateAmanage(request):
    m=CategoryA.objects.all()

    context={
        "m":m
    }

    return render(request,'manager/goods/cate/cateAmanage.html',context)


def updateCateA(request):
    no=int(request.GET.get('no'))

    try:
        a = CategoryA.objects.get(a_idx=no)
    except:
        a = None
    

    context={
        "a":a
    }
    return render(request,'manager/goods/cate/updateCateA.html',context)

def updateResult(request):
    no=int(request.POST.get('no'))
    name=request.POST.get('name')
    print(type(name))
    try:
        CategoryA.objects.filter(a_idx=no).update(a_name=name)
        msg="수정완료"
    except Exception as a:
        msg="수정실패"
        print(a)
    
    context={
        "msg":msg
    }
    return render(request,'manager/goods/cate/cateAresult.html',context)


def deleteCateA(request):
    no = int(request.GET.get("no"))
    
    try:
        CategoryA.objects.filter(a_idx=no).delete()
        msg = "삭제되었습니다."
    except:
        msg = "삭제되지 못했습니다."
    
    context = {
        "msg" : msg
    }


    return render(request,'manager/goods/cate/cateAresult.html',context)



def cateB(request):
    a=CategoryA.objects.all()
    context={
        "a":a
    }
    return render(request,'manager/goods/cate/cateB.html',context)

def cateBresult(request):
    cate=request.POST.get('cate')
    catea=int(request.POST.get('cateA'))
    c=CategoryA.objects.get(a_idx=catea)
    print(c)
    print(type(catea))


 
    try:
        CategoryB.objects.create(b_name=cate, b_idx_a=c)
        msg="등록완료"
    except Exception as e:
        msg="등록실패"
        print(e)

    context={
        "msg":msg
    }
    return render(request,'manager/goods/cate/cateBresult.html',context)

def cateBmanage(request):
    b=CategoryB.objects.all()
    context={
        "b":b
    }
    return render(request,'manager/goods/cate/cateBmanage.html',context)

def cateBupdate(request):
    no=request.GET.get('no')
    print(no)
    m=CategoryB.objects.get(b_idx=no)
    a=CategoryA.objects.all()
    context={
        "m":m,
        "a":a
    }
    return render(request,'manager/goods/cate/cateBupdate.html',context)


def cateBupResult(request):
    no=int(request.POST.get('no'))
    name=request.POST.get('name')
    catea=int(request.POST.get('cateA'))

    c=CategoryB.objects.filter(b_idx=no)
    try:
        c.update(b_idx_a=catea,b_name=name)
        msg="등록완료"
    except Exception as e:
        msg="등록실패"
        print(e)

    context={
        "msg":msg
    }
    return render(request,'manager/goods/cate/cateBupResult.html',context)








#--------------------------------------------------------------
def customer(request):
    if Admin.objects.get(admin_idx=request.session['manager']).admin_department_no==1 or Admin.objects.get(admin_idx=request.session['manager']).admin_department_no==5:

        m=Member.objects.all()

        context={
            "m":m
        }
        return render(request,'manager/customer/customer.html',context)
    else:
        return render(request,'manager/hr/warning.html')


def customerDelete(request):
    no = int(request.GET.get("no"))
    
    try:
        Member.objects.filter(user_no=no).delete()
        msg = "삭제되었습니다."
    except:
        msg = "삭제되지 못했습니다."
    
    context = {
        "msg" : msg
    }
    return render(request,'manager/customer/customerDelete.html',context)

def customerUpdate(request):
    no=int(request.GET.get('no'))

    try:
        a = Member.objects.get(user_no=no)
    except:
        a = None
    

    context={
        "a":a
    }
    return render(request,'manager/customer/customerupdate.html',context)

def custUpResult(request):
    no= int(request.POST.get("no"))
    id=request.POST.get('id')
    pw=request.POST.get('pw')
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    email=request.POST.get("email")
    point=request.POST.get('point')
    addr=request.POST.get('addr')

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
        Member.objects.filter(user_no=no).update(user_id=id,user_name=name,user_pw=pw,phone=phone,email=email,e_agreement=agree_email,n_agreement=agree_news,p_agreement=agree_push,point=point,addr=addr)
        msg="수정성공"
    except Exception as e:
        msg="실패"
        print(e)

    context={
        'msg':msg
    }
    return render(request,'manager/customer/custUpResult.html',context)




#------------------------------------------------------------------------------------------------





def product(request):
    a=CategoryA.objects.all()
    b=CategoryB.objects.all()
    context={
        "a": a,
        "b": b
    }
    return render(request,'manager/goods/product.html',context)

def productResult(request):
    name=request.POST.get('name')
    cprice=request.POST.get('cprice')
    rprice=request.POST.get('rprice')
    catea=request.POST.get('catea')
    a=CategoryA.objects.get(a_idx=catea)
    cateb=request.POST.get('cateb')
    b=CategoryB.objects.get(b_idx=cateb)
    info=request.FILES.get('info')
    image=request.FILES.get('image')
    point=request.POST.get('point')
    stock=request.POST.get('stock')

    try:
        Goods.objects.create(goods_name=name,goods_c_price=cprice,goods_sale_price=rprice,goods_idx_b=b,goods_idx_a=a,goods_image=image,goods_info=info,goods_stock=stock)
        msg="등록성공"
    except Exception as a:
        print(a)
        msg="실패"

    context={
        "msg":msg
    }
    return render(request,'manager/goods/productResult.html',context)


def productDelete(request):
    no=request.GET.get('no')

    try:
        Goods.objects.filter(goods_num=no).delete()
        msg="삭제되었습니다"
    except Exception as e:
        print(e)
        msg="실패"
    context={
        "msg":msg
    }
    return render(request,'manager/goods/productDelete.html',context)


def productM(request):
    p=Goods.objects.all()

    context={
        "p":p
    }
    return render(request,'manager/goods/productM.html',context)

def productUpdate(request):
    no=request.GET.get('no')
    p=Goods.objects.get(goods_num=no)
    context={
        "p":p
    }
    return render(request,'manager/goods/productUpdate.html',context)

def pUpdateResult(request):
    no=int(request.POST.get('no'))
    name=request.POST.get('name')
    cprice=request.POST.get('cprice')
    rprice=request.POST.get('rprice')
    catea=request.POST.get('catea')
    a=CategoryA.objects.get(a_idx=catea)
    cateb=request.POST.get('cateb')
    b=CategoryB.objects.get(b_idx=cateb)
    info=request.FILES.get('info')
    image=request.FILES.get('image')
    point=request.POST.get('point')
    stock=request.POST.get('stock')

    g=Goods.objects.filter(goods_num=no)

    try:
        g.update(goods_name=name,goods_c_price=cprice,goods_sale_price=rprice,goods_idx_b=b,goods_idx_a=a,goods_image=image,goods_info=info,goods_stock=stock)
        msg="등록성공"
    except Exception as a:
        print(a)
        msg="실패"

    context={
        "msg":msg
    }
    return render(request,'manager/goods/pUpdateResult.html',context)


def plusAccount(request):
    no=request.GET.get("no")
    g=Goods.objects.get(goods_num=no)
    context={
        "g":g
    }
    return render(request,'manager/goods/plusAccount.html',context)

def plusResult(request):
    no=int(request.POST.get("no"))
    print(no)
    stock=int(request.POST.get('plus'))

    rstock=Goods.objects.get(goods_num=no).goods_stock+stock
    g=Goods.objects.filter(goods_num=no)
    try:
        g.update(goods_stock=rstock)
        msg="수정성공"
    except Exception as e:
        print(e)
        msg="실패"

    context={
        "msg":msg,
    }
    return render(request,'manager/goods/plusResult.html',context)

#카테고리 b 등록, 상품등록 문제있음



def card(request):
    return render(request,'manager/goods/card/card.html')

def cardresult(request):
    name=request.POST.get('name')

    try:
        Card.objects.create(card_name=name)
        msg="등록완료"
    except Exception as e:
        msg="등록실패"
        print(e)

    context={
        "msg":msg
    }
    return render(request,'manager/goods/card/cardresult.html',context)


def cardM(request):
    return render(request,'manager/goods/card/cardM.html')


def cardList(request):
    c=Card.objects.all()
    context={
        "c":c
    }
    return render(request,'manager/goods/card/cardList.html',context)

def cardUpdate(request):
    no=request.GET.get("no")
    c=Card.objects.get(card_idx=no)

    context={
        "c":c
    }
    return render(request,'manager/goods/card/cardUpdate.html',context)



def updateResult(request):
    no=request.POST.get("no")
    name=request.POST.get("name")

    c=Card.objects.filter(card_idx=no)
    try:
        c.update(card_name=name)
    except Exception as e:
        print(e)
        redirect('/manager/cardUpdate/')



    return redirect('/manager/cardList/')

def cardDelete(request):
    no=request.GET.get("no")
    c=Card.objects.filter(card_idx=no)
    c.delete()
    return redirect('/manager/cardList')