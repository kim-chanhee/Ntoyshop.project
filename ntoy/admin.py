from django.contrib import admin
from .models import Member
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'user_no',
        'user_name',
        'user_id',
        'user_pw',
        "join_date",
        "addr",
        'home_num',
        "phone",
        "email",
        "point",
        "e_agreement",
        "n_agreement",
        "p_agreement",
    )


    list_display_links = (
        'user_no',
        'user_name',
        'user_id',
        'user_pw',
        #"join_date",
        #"addr",
        #'home_num',
        #"phone",
        #"email",
        #"point"
        #"e_agreement",
        #"n_agreement",
        #"p_agreement",
    )