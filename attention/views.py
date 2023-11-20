from django.shortcuts import render,get_object_or_404
from ntoy.models import Admin,Attendance

# Create your views here.

def attend(request):
    return render(request,'attention/attend.html')
def produce(request):

    return render(request,'attention/produce.html')

def date(request):
    #폼 입력값 가져오기
    date=request.POST['date']
    names=Admin.objects.all()
    context={
        'date':date,
        'names':names
        }

    return render(request,'attention/attention.html',context)

def chk(request):
    #폼 입력값 가져와서 Attendance에 저장
    attendance=Attendance()
    attendance.name=request.POST['name']
    attendance.attendance=request.POST['attendance']
    attendance.date=request.POST['date']
    
    #학생들 이름 전부 가져오기
    names=Admin.objects.all()
    
    #출결 횟수 저장
    name=request.POST['name']
    member_info=get_object_or_404(Admin, admin_name=name)
    if attendance.attendance=="출석":
        member_info.attendance+=1
    
    elif attendance.attendance=="결석":
        member_info.absent+=1
    
    elif attendance.attendance=="지각":
        member_info.tardy+=1

    elif attendance.attendance=="기타":
        member_info.etc+=1

    member_info.save()
    attendance.save()
    msg="출결체크 완료"

    context={
        'date':attendance.date,
        'names':names,
        'msg':msg
        }
    return render(request,'attention/attentionResult.html',context)


def show(request):

    return render(request,'attention/show.html')

def showtable(request):
    date=request.POST.get('date')
    info = Attendance.objects.filter(date__contains='{}'.format(date))

    context={
        'info':info,
        'date':date
        }

    return render(request,'attention/showtable.html',context)

