from django.db import models


class Member(models.Model):
    user_no = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=5)
    user_id = models.CharField(max_length=25)
    user_pw = models.CharField(max_length=25)
    join_date = models.DateField()
    addr = models.CharField(max_length=100, blank=True, null=True)
    home_num = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30, blank=True, null=True)
    point = models.IntegerField()
    e_agreement = models.IntegerField(blank=True, null=True)
    n_agreement = models.IntegerField(blank=True, null=True)
    p_agreement = models.IntegerField(blank=True, null=True)


    def __str__(self) -> str:
        return self.user_name

    class meta:
        db_table='member'
        verbose_name = '멤버'
        verbose_name_plural = '멤버'



class Admin(models.Model):
    admin_idx = models.AutoField(primary_key=True)
    admin_id = models.CharField(max_length=25)
    admin_pw = models.CharField(max_length=25)
    admin_name = models.CharField(max_length=20)
    admin_department_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admin'


class CategoryA(models.Model):
    a_idx = models.AutoField(db_column='A_idx', primary_key=True)  # Field name made lowercase.     
    a_name = models.CharField(db_column='A_name', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category_a'


class CategoryB(models.Model):
    b_idx = models.AutoField(db_column='B_idx', primary_key=True)  # Field name made lowercase.     
    b_idx_a = models.ForeignKey(CategoryA, models.DO_NOTHING, db_column='B_idx_A', null=True)  # Field name made lowercase.
    b_name = models.CharField(db_column='B_name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category_b'


class Uploadmodel(models.Model):
    up_no = models.AutoField(primary_key=True)
    up_title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploadmodel'


class Uploadfilesmodel(models.Model):
    upload = models.ForeignKey('Uploadmodel', models.DO_NOTHING, db_column='upload', blank=True, null=True)
    upload_file = models.FileField(blank=True, null=True)
    upload_filename = models.CharField(max_length=64, blank=True, null=True)
    upload_content_type = models.CharField(max_length=128, blank=True, null=True)
    upload_size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploadfilesmodel'


class Goods(models.Model):
    goods_num = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    goods_c_price = models.IntegerField()
    goods_sale_price = models.IntegerField(db_column='goods_Sale_price')  # Field name made lowercase.
    goods_idx_b = models.ForeignKey(CategoryB, models.DO_NOTHING, db_column='goods_idx_B', blank=True, null=True)  # Field name made lowercase.
    goods_idx_a = models.ForeignKey(CategoryA, models.DO_NOTHING, db_column='goods_idx_A', blank=True, null=True)  # Field name made lowercase.
    goods_info = models.FileField(blank=True, null=True)
    goods_image = models.FileField(blank=True, null=True)
    goods_stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'

class Card(models.Model):
    card_idx = models.AutoField(primary_key=True)
    card_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'card'


class Payment(models.Model):
    pay_idx = models.AutoField(primary_key=True)
    pay_user_no = models.ForeignKey(Member, models.DO_NOTHING, db_column='pay_user_no')
    pay_paymethod_no = models.IntegerField(blank=True, null=True)
    pay_card_no = models.ForeignKey(Card, models.DO_NOTHING, db_column='pay_card_no', blank=True, null=True)
    pay_card_num = models.CharField(max_length=30, blank=True, null=True)
    pay_product_no = models.ForeignKey(Goods, models.DO_NOTHING, db_column='pay_product_no')
    pay_amount = models.IntegerField(blank=True, null=True)
    pay_price = models.IntegerField(blank=True, null=True)
    pay_join_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Delivery(models.Model):
    del_idx = models.AutoField(primary_key=True)
    del_user_no = models.ForeignKey('Member', models.DO_NOTHING, db_column='del_user_no', blank=True, null=True)
    del_goods_num = models.ForeignKey('Goods', models.DO_NOTHING, db_column='del_goods_num', blank=True, null=True)
    del_name = models.CharField(max_length=50)
    del_tel1 = models.CharField(max_length=20)
    del_tel2 = models.CharField(max_length=20)
    del_add_no = models.CharField(max_length=6)
    del_addr = models.CharField(max_length=50)
    del_addr_plus = models.CharField(max_length=50)
    del_order_text = models.CharField(max_length=100, blank=True, null=True)
    del_cod = models.IntegerField(blank=True, null=True)
    del_cost = models.IntegerField(blank=True, null=True)
    del_situ = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery'


class Returns(models.Model):
    re_idx = models.AutoField(primary_key=True)
    re_payment_no = models.ForeignKey(Payment, models.DO_NOTHING, db_column='re_payment_no', blank=True, null=True)
    re_return_date = models.DateField(blank=True, null=True)
    re_return_reason = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'returns'


class Basket(models.Model):
    bas_idx = models.AutoField(primary_key=True)
    bas_user_no = models.IntegerField(blank=True, null=True)
    bas_product_no = models.ForeignKey('Goods', models.DO_NOTHING, db_column='bas_product_no', blank=True, null=True)
    bas_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket'




class Salary(models.Model):
    s_no = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=20, blank=True, null=True)
    s_situ = models.CharField(max_length=20, blank=True, null=True)
    s_date = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary'


class Ttable(models.Model):
    t_no = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=20, blank=True, null=True)
    t_money = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ttable'

class Attendance(models.Model): #모델명의 첫글자는 대문자로
    name = models.CharField(max_length = 50) #최대로 넣을 수 있는 글자 수
    attendance = models.CharField(max_length = 50)
    date = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name