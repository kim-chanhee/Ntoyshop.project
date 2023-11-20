from ssl import AlertDescription
from ntoy.models import Member,Admin, Goods
from .models import Qna,Review,Notice,Comment

from types import NoneType
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.core.paginator import Paginator
from .forms import QnAWriteForm, noticeWriteForm, reviewWriteForm

from django.db.models import Max
from django.db.models import F


def qnaList(request:HttpRequest):

    MAX_PAGE_CNT = 10
    MAX_LIST_CNT = 10

    qnalist = Qna.objects.all().order_by('-q_group_no','q_order_no')


    page = request.GET.get('page','1')

    paginator = Paginator(qnalist,MAX_LIST_CNT)

    page_obj = paginator.get_page(page)

    last_page = 0

    for last_page in paginator.page_range:
        last_page += 1

    current_block = ((int(page)-1)//MAX_PAGE_CNT)+1

    start_page = (current_block -1)*MAX_PAGE_CNT + 1

    end_page = start_page + MAX_PAGE_CNT -1

    context = {
        'list' : page_obj,
        'last_page' : last_page,
        'start_page' : start_page,
        'end_page' : end_page,
    }


    return render(request,'board/qna/qnaList.html',context)


def qnaRead(request:HttpRequest):
    q_num = request.GET.get('q_num')

    board = Qna.objects.get(q_num=q_num)

    board.q_hits += 1

    board.save()

    context = {
        'content' : board
    }

    return render(request,'board/qna/qnaRead.html',context)


def qnaWrite(request, q_num = 0):
    forms = QnAWriteForm()

    context = {
        'forms' : forms,
        'q_num' : q_num,
    }

    return render(request,'board/qna/qnaWrite.html',context)

def qnaWriteCheck(request:HttpRequest):
    q_num = request.POST.get('q_num')
    user_no = Member.objects.get(user_no = int(request.session['login']))     
    title = request.POST.get('q_title')
    content = request.POST.get('q_text')
    hits = 0

    url = None
    msg = None
    
    


    try:
        if q_num == '0':
            q_group_no = Qna.objects.aggregate(max_group=Max('q_group_no')).get('max_group') + 1
            # 미리 데이터가 존재해야 작동을 한다.

            # q_group_no = Qna.objects.aggregate(max_group=Max('q_group_no')).get('max_group')
            
            
            qna = Qna.objects.create(q_c_num=user_no,q_title=title,q_text=content,q_group_no=q_group_no,q_hits=hits)
        else:
            qna2 = Qna.objects.get(q_num=q_num)
            Qna.objects.filter(q_order_no__gte=qna2.q_order_no + 1).update(q_order_no=F('q_order_no') + 1)
            qna = Qna.objects.create(q_c_num=user_no,q_title=title,q_text=content,q_group_no = qna2.q_group_no,q_order_no = qna2.q_order_no+1,q_depth = qna2.q_depth + 1,q_hits=hits)

    except Exception as e:
        print(e)
        url = '/board/qnaWrite/' + q_num
        msg = '글작성 실패'
    else:
        url = '/board/qnaList/'
        msg = '글작성 성공'

    context = {
        'url' : url,
        'msg' : msg,
    }
    return render(request,'board/qna/qnaResult.html',context)


def qnaUpdate(request:HttpRequest):
    q_num = request.GET.get('q_num')

    board = Qna.objects.get(q_num=q_num)

    forms = QnAWriteForm(instance=board)

    context = {
        'forms' : forms,
        'q_num' : q_num,
    }

    return render(request,'board/qna/qnaUpdate.html',context)

def qnaUpdateCheck(request:HttpRequest):

    q_num = request.POST.get('q_num')
    title = request.POST.get('q_title')
    content = request.POST.get('q_text')

    content = content.replace('\r\n','<br>')

    url = None
    msg = None

    try:
        board = Qna.objects.filter(q_num=q_num).update(q_title=title,q_text=content)
    except Exception as e:
        print(e)
        url = '/board/qnaUpdate/'     # qna 부분 앱명으로 전환 필요
        msg = '수정 실패'
    else:
        url = '/board/qnaRead/?q_num=' + q_num               # qna 부분 앱명으로 전환 필요
        msg = '수정 성공'

    context = {
        'url' : url,
        'msg' : msg,
    }

    return render(request,'board/qna/qnaResult.html',context)

def qnaDelete(request:HttpRequest):
    q_num = request.GET.get('q_num')

    url = None
    msg = None

    try:
        board = Qna.objects.get(q_num=q_num).delete()
    except Exception as e:
        print(e)
        url = '/board/qnaRead/?q_num=' + q_num
        msg = '글삭제 실패'
    else:
        url = '/board/qnaList/'
        msg = '글삭제 성공'
    
    context = {
        'url' : url,
        'msg' : msg,
    }

    return render(request,'board/qna/qnaResult.html',context)




    # ========================================================
    # 여기는 공지 부분


def noticeList(request:HttpRequest):

    MAX_PAGE_CNT = 10
    MAX_LIST_CNT = 4

    # noticelist = Notice.objects.all().order_by('-not_num')
    noticelist = Notice.objects.all().order_by('-not_sort','-not_num')


    page = request.GET.get('page','1')

    paginator = Paginator(noticelist,MAX_LIST_CNT)

    page_obj = paginator.get_page(page)

    last_page = 0

    for last_page in paginator.page_range:
        last_page += 1

    current_block = ((int(page)-1)//MAX_PAGE_CNT)+1

    start_page = (current_block -1)*MAX_PAGE_CNT + 1

    end_page = start_page + MAX_PAGE_CNT -1

    context = {
        'list' : page_obj,
        'last_page' : last_page,
        'start_page' : start_page,
        'end_page' : end_page,
    }

    return render(request,'board/notice/noticeList.html',context)



def noticeRead(request:HttpRequest):
    notice_num = request.GET.get('not_num')

    board = Notice.objects.get(not_num=notice_num)

    board.not_hits += 1

    board.save()

    context = {
        'content' : board
    }
    return render(request,'board/notice/noticeRead.html',context)


def noticeWrite(request):
    forms = noticeWriteForm()
    context = {
        'forms' : forms
    }

    return render(request,'board/notice/noticeWrite.html',context)

def noticeWriteCheck(request:HttpRequest):
    admin_num = Admin.objects.get(admin_idx = int(request.session['manager']))
    


    title = request.POST.get('not_title')
    content = request.POST.get('not_content')
    hits = 0
    check = request.POST.get('not_checks')      # 이건 그냥 on인지 아닌지를 가져온다.

    nsort = 0

    if check != None:
        checkt = True
        nsort += 1
    else:
        checkt = False



    try:
        # notice = Notice.objects.create(not_admin_num=admin_num,not_title=title,not_content=content,not_hits=hits,not_checks=checkt)
        
        notice = Notice.objects.create(not_admin_num=admin_num,not_title=title,not_content=content,not_hits=hits,not_checks=checkt,not_sort = nsort)
    except Exception as e:
        print(e)
        url = '/board/noticeWrite/'
        msg = '공지 작성 실패'
    else:
        url = '/board/noticeList/'
        msg = '공지 작성 완료'

    context = {
        'url' : url,
        'msg' : msg,
    }
    return render(request,'board/notice/noticeResult.html',context)

def noticeUpdate(request:HttpRequest):
    notice_num = request.GET.get("not_num")

    board = Notice.objects.get(not_num=notice_num)

    forms = noticeWriteForm(instance=board)
    context = {
        'forms' : forms,
        'not_num' : notice_num,
    }
    return render(request,'board/notice/noticeUpdate.html',context)

def noticeUpdateCheck(request:HttpRequest):

    notice_num = request.POST.get('not_num')
    title = request.POST.get('not_title')
    content = request.POST.get('not_content')

    content = content.replace('\r\n','<br>')

    url = None
    msg = None

    try:
        board = Notice.objects.filter(not_num = notice_num).update(not_title=title,not_content=content)
    except Exception as e:
        print(e)
        url = '/board/noticeUpdate/'
        msg = '수정실패'
    else:
        url = '/board/noticeRead/?not_num=' + notice_num
        msg = '수정 성공'
    context = {
        'url' : url,
        'msg' : msg,
    }
    return render(request,'board/notice/noticeResult.html',context)

def noticeDelete(request:HttpRequest):

    notice_num = request.GET.get('not_num')

    url = None
    msg = None

    try:
        board = Notice.objects.get(not_num = notice_num).delete()
    except Exception as e:
        print(e)
        url = '/board/notieRead/?not_num=' + notice_num
        msg = '공지삭제 실패'
    else:
        url = '/board/noticeList/'
        msg = '글삭제 성공'
    
    context = {
        'url' : url,
        'msg' : msg,
    }
    return render(request,'board/notice/noticeResult.html',context)

# ============================================================

#  여기는 이용후기

def reviewList(request:HttpRequest):

    MAX_PAGE_CNT = 10
    MAX_LIST_CNT = 10

    reviewlist = Review.objects.all().order_by('-rev_no')


    page = request.GET.get('page','1')

    paginator = Paginator(reviewlist,MAX_LIST_CNT)

    page_obj = paginator.get_page(page)

    last_page = 0

    for last_page in paginator.page_range:
        last_page += 1

    current_block = ((int(page)-1)//MAX_PAGE_CNT)+1

    start_page = (current_block -1)*MAX_PAGE_CNT + 1

    end_page = start_page + MAX_PAGE_CNT -1



    context = {
        'list' : page_obj,
        'last_page' : last_page,
        'start_page' : start_page,
        'end_page' : end_page,
    }

    return render(request,'board/review/reviewList.html',context)



def reviewRead(request:HttpRequest):
    use_no = request.GET.get('rev_no')

    board = Review.objects.get(rev_no=use_no)

    board.rev_view_count += 1

    board.save()


    comments = Comment.objects.filter(board = use_no)

    print(comments)

    context = {
        'content' : board,
        'comments' : comments,
    }
    
    return render(request,'board/review/reviewRead.html',context)


def reviewWrite(request:HttpRequest):

    n = request.GET.get('no')
    g=Goods.objects.get(goods_num=n)
    print(n)
    print(g)

    forms = reviewWriteForm()

    context = {
        'forms' : forms,
        'g' : g,

    }

    return render(request,'board/review/reviewWrite.html',context)

def reviewWriteCheck(request:HttpRequest):
    user_no = Member.objects.get(user_no = int(request.session['login']))


    title = request.POST.get('rev_title')
    content = request.POST.get('rev_afterword')
    view = 0
    hit = 0

    no = int(request.POST.get('no'))

    g=Goods.objects.get(goods_num=no)
    print(no)



    try:
        review = Review.objects.create(rev_product_no=g,rev_user_no=user_no,rev_title=title,rev_afterword=content,rev_view_count=view,rev_hit_use=hit)
     
    except Exception as e:
        print(e)
        url = '/board/reviewWrite/'
        msg = '후기 작성 실패'
    else:
        url = '/board/reviewList/'
        msg = '후기 작성 완료'

    context = {
        'url' : url,
        'msg' : msg,
    }
    return render(request,'board/review/reviewResult.html',context)

def reviewUpdate(request:HttpRequest):
    rev_no = request.GET.get('rev_no')

    board = Review.objects.get(rev_no = rev_no)
    
    forms = reviewWriteForm(instance=board)
    
    context = {
        'forms' : forms,
        'rev_no' : rev_no,
    }
    return render(request,'board/review/reviewUpdate.html',context)

def reviewUpdateCheck(request:HttpRequest):

    rev_no = request.POST.get('rev_no')
    title = request.POST.get('rev_title')
    content = request.POST.get('rev_afterword')

    content = content.replace('\r\n','<br>')

    url = None
    msg = None

    try:
        board = Review.objects.filter(rev_no=rev_no).update(rev_title=title,rev_afterword=content)
    except Exception as e:
        print(e)
        url = '/board/reviewUpdate/'            
        msg = '수정실패'
    else:                                       
        url = '/board/reviewRead/?rev_no=' + rev_no
        msg = '수정 성공'
    context = {
        'url' : url,
        'msg' : msg,
    }
    return render(request,'board/review/reviewResult.html',context)

def reviewDelete(request:HttpRequest):

    rev_no = request.GET.get('rev_no')
    print(rev_no)

    url = None
    msg = None

    try:
        board = Review.objects.get(rev_no = rev_no).delete()
    except Exception as e:
        print(e)
        url = '/board/reviewRead/?rev_no=' + rev_no
        msg = '공지삭제 실패'
    else:
        url = '/board/reviewList/'
        msg = '글삭제 성공'
    
    context = {
        'url' : url,
        'msg' : msg,
    }
    return render(request,'board/review/reviewResult.html',context)


# 이용후기 댓글 기능

def recommentInsert(request:HttpRequest,no):
    member_no = Member.objects.get(user_no = int(request.session['login']))
    board = Review.objects.get(rev_no=no)
    content = request.POST.get('content')

    content = content.replace('\r\n','<br>')

    try:
        comment = Comment.objects.create(member_no = member_no,board = board,content = content)
    except Exception as e:
        print(e)


    return redirect('/board/reviewRead/?rev_no=' + str(no))
    # 왜 번호를 문자열 형식으로 전달?????



def recommentDelete(request:HttpRequest,no):

    try:
        comment = Comment.objects.get(no=no)
        url = '/board/reviewRead/?rev_no=' + str(comment.board.rev_no)
        comment.delete()
    except Exception as e:
        print(e)


    return redirect(url)
