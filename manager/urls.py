from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('checkLogin/',views.checkLogin),
    path('hr/',views.hr),
    path('join/',views.join),
    path('checkJoin/',views.checkjoin),
    path('goods/',views.goods),
    path('logout/',views.logout),
    path('manage/',views.manage),
    path('update/',views.update),
    path('updateResults/',views.updateResults),
    path('delete/',views.delete),
    path('customer/',views.customer),
    path('customerDelete/',views.customerDelete),
    path('cate/',views.cate),
    path('cateA/',views.cateA),
    path('cateAresult/',views.cateAresult),
    path('updateCateA/',views.updateCateA),
    path('deleteCateA/',views.deleteCateA),
    path('cateAmanage/',views.cateAmanage),
    path('cateBmanage/',views.cateBmanage),
    path('customerUpdate/',views.customerUpdate),
    path('custUpResult/',views.custUpResult),
    path('cateB/',views.cateB),
    path('cateBresult/',views.cateBresult),
    path('cateBupdate/',views.cateBupdate),
    path('cateBupResult/',views.cateBupResult),
    path('insertProduct/',views.product),
    path('productResult/',views.productResult),
    path('productM/',views.productM),
    path('productUpdate/',views.productUpdate),
    path('pUpdateResult/',views.pUpdateResult),
    path('productDelete/',views.productDelete),
    path('plusAccount/',views.plusAccount),
    path('plusResult/',views.plusResult),
    path('card/',views.card),
    path('cardresult/',views.cardresult),
    path('cardM/',views.cardM),
    path('cardList/',views.cardList),
    path('cardUpdate/',views.cardUpdate),
    path('updateResult/',views.updateResult),
    path('cardDelete/',views.cardDelete)

]


