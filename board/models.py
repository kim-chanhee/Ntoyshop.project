# Create your models here.
from django.db import models
from ntoy.models import Member,Goods,Admin
from django_summernote.fields import SummernoteTextFormField
from django_summernote.models import Attachment

# Create your models here.
class Qna(models.Model):
    q_num = models.AutoField(db_column='Q_num', primary_key=True)  # Field name made lowercase.
    q_group_no = models.IntegerField(default=0) # 게시글 기본 정렬
    q_order_no = models.IntegerField(default=0) # 답글 작성시 원본글 아래에 위치하기 위한 번호
    q_depth = models.IntegerField(default = 0)  # 답글 장성시 title 앞에 re 이 나오기 위한 장치
    q_goods_num = models.ForeignKey(Goods, models.DO_NOTHING, db_column='Q_goods_num', blank=True, null=True)  # Field name made lowercase.
    q_c_num = models.ForeignKey(Member, models.DO_NOTHING, db_column='Q_C_num')  # Field name made lowercase.
    q_title = models.CharField(db_column='Q_Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    q_text = models.TextField(db_column='Q_Text')  # Field name made lowercase.
    q_w_date = models.DateTimeField(db_column='Q_W_date', auto_now_add=True)  # Field name made lowercase. 뒤의 시간부분을 자동 조정으로 하였음
    q_hits = models.IntegerField(db_column='Q_Hits', blank=True, null=True)  # Field name made lowercase.
    answer = models.IntegerField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qna'





class Review(models.Model):
    rev_no = models.AutoField(primary_key=True)
    rev_product_no = models.ForeignKey(Goods, models.DO_NOTHING, db_column='rev_product_no', blank=True, null=True)
    rev_user_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='rev_user_no')
    rev_title = models.CharField(max_length=20)
    rev_afterword = models.TextField()
    rev_use_date = models.DateField(auto_now_add=True)
    rev_view_count = models.IntegerField()
    rev_hit_use = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'review'


class Notice(models.Model):
    not_num = models.AutoField(primary_key=True)
    not_admin_num = models.ForeignKey(Admin, models.DO_NOTHING, db_column='not_admin_num', blank=True, null=True)
    not_title = models.CharField(max_length=20, blank=True, null=True)
    not_content = models.TextField(blank=True, null=True)
    not_write_date = models.DateField(blank=True, auto_now_add=True)
    not_hits = models.IntegerField(blank=True, null=True)
    not_checks = models.BooleanField(verbose_name='상단고정', default=False)
    not_sort = models.IntegerField(verbose_name='고정정렬', default=0)

    class Meta:
        managed = False
        db_table = 'notice'



class Comment(models.Model):
    no = models.AutoField(primary_key=True)
    board = models.ForeignKey(Review,on_delete=models.CASCADE)
    member_no = models.ForeignKey(Member,on_delete=models.CASCADE)
    content = models.TextField()
    logtime = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return str(self.no) + '\t' + self.title

    class Meta:
        managed = False
        db_table = 'comment'