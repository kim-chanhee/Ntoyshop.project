# from django.shortcuts import render
# from ntoy.models import Goods
# # Create your views here.

# def browse(request):
#     m=Goods.objects.all()


#     context={
#         "m":m
#     }
#     return render(request,'browse/browse.html',context)

# def show(request):
#     no=request.GET.get("no")
#     m=Goods.objects.get(goods_num=no)
#     price=Goods.objects.get(goods_num=no).goods_sale_price
#     point=price*0.01
#     context={
#         "m":m,
#         "point":int(point)
#     }

#     return render(request,'browse/show.html',context)

from django.shortcuts import render
from ntoy.models import Goods
from board.models import Review,Qna
from django.http import HttpRequest
from django.core.paginator import Paginator
# Create your views here.
# Create your views here.

def browse(request):
    m=Goods.objects.all()


    context={
        "m":m
    }
    return render(request,'browse/browse.html',context)

def show(request:HttpRequest):
    no=request.GET.get("no")
    m=Goods.objects.get(goods_num=no)
    price=Goods.objects.get(goods_num=no).goods_sale_price
    point=price*0.01

 # ===============================================

    MAX_PAGE_CNT = 10
    MAX_LIST_CNT = 10

    reviewlist = Review.objects.all().order_by('-rev_no')

    
    rpage = request.GET.get('page','1')

    rpaginator = Paginator(reviewlist,MAX_LIST_CNT)

    rpage_obj = rpaginator.get_page(rpage)

    rlast_page = 0

    for rlast_page in rpaginator.page_range:
        rlast_page += 1

    rcurrent_block = ((int(rpage)-1)//MAX_PAGE_CNT)+1

    rstart_page = (rcurrent_block -1)*MAX_PAGE_CNT + 1

    rend_page = rstart_page + MAX_PAGE_CNT -1



    # =========================================

    qnalist = Qna.objects.all().order_by('-q_group_no','q_order_no')


    qpage = request.GET.get('page','1')

    qpaginator = Paginator(qnalist,MAX_LIST_CNT)

    qpage_obj = qpaginator.get_page(qpage)

    qlast_page = 0

    for qlast_page in qpaginator.page_range:
        qlast_page += 1

    qcurrent_block = ((int(qpage)-1)//MAX_PAGE_CNT)+1

    qstart_page = (qcurrent_block -1)*MAX_PAGE_CNT + 1

    qend_page = qstart_page + MAX_PAGE_CNT -1




    context={
        "m":m,
        "point":int(point),
        'rlist' : rpage_obj,
        'rlast_page' : rlast_page,
        'rstart_page' : rstart_page,
        'rend_page' : rend_page,
        'qlist' : qpage_obj,
        'qlast_page' : qlast_page,
        'qstart_page' : qstart_page,
        'qend_page' : qend_page,
    }

    return render(request,'browse/show.html',context)


def page(request):
    no=request.GET.get("no")
    m=Goods.objects.filter(goods_idx_b=no)


    context={
        "m":m
    }
    return render(request,'browse/page.html',context)


