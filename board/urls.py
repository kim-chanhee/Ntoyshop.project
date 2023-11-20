from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('qnaList/',views.qnaList),
    path('qnaRead/',views.qnaRead),
    path('qnaUpdate/',views.qnaUpdate),
    path('qnaWrite/<int:q_num>',views.qnaWrite),
    path('qnaWriteCheck/',views.qnaWriteCheck),
    path('qnaUpdateCheck/',views.qnaUpdateCheck),
    path('qnaDelete/',views.qnaDelete),


    path('noticeList/',views.noticeList),
    path('noticeRead/',views.noticeRead),
    path('noticeUpdate/',views.noticeUpdate),
    path('noticeWrite/',views.noticeWrite),
    path('noticeWriteCheck/',views.noticeWriteCheck),
    path('noticeUpdateCheck/',views.noticeUpdateCheck),
    path('noticeDelete/',views.noticeDelete),


    path('reviewList/',views.reviewList),
    path('reviewRead/',views.reviewRead),
    path('reviewUpdate/',views.reviewUpdate),
    path('reviewWrite/',views.reviewWrite),
    path('reviewWriteCheck/',views.reviewWriteCheck),
    path('reviewUpdateCheck/',views.reviewUpdateCheck),
    path('reviewDelete/',views.reviewDelete),
    path('<int:no>/reviewComment',views.recommentInsert),
    path('reviewComment/<int:no>',views.recommentDelete),


    path('summernote/', include('django_summernote.urls')),

]
