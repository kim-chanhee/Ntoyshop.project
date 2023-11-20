
# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

from ntoy.models import Member

# Create your views here.
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

    return render(request,'login/login.html',context);

def checkLogin(request:HttpRequest):
    id = request.POST.get("id")
    password = request.POST.get("password")

    msg = None
    check = False
    
    try:
        member = Member.objects.get(user_id=id,user_pw=password) # and
        #print(member.query) # 지금 작성한 쿼리문 반환...
    except Exception as e:
        msg = "아이디 혹은 비밀번호가 잘못되었습니다."
    else:
        check = True
        msg = member.user_name + "님이 로그인하셨습니다."

        #로그인 처리
        request.session['login'] = member.user_no

    context = { 'msg' : msg , 'check' : check }
    
    response = redirect('/')

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
    request.session.pop('login') # 세션에 저장된 하나의 키와 밸류 삭제.
    #print(request.session['login'])
    #request.session.flush() # 세션의 저장된 정보 초기화
    return redirect('/')
