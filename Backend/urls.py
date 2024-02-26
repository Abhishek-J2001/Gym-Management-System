from django.urls import path
from Backend import views
urlpatterns = [
    path('indexpage/', views.indexpage, name= "indexpage"),
    path('managepackage/', views.managepackage, name= "managepackage"),
    path('savedata/', views.savedata, name="savedata"),
    path('catdisplay/', views.catdisplay, name="catdisplay"),
    path('editpage/<int:dataid>/', views.editpage, name="editpage"),
    path('updatedata/<int:dataid>/', views.updatedata, name="updatedata"),
    path('deletecat/<int:dataid>/', views.deletecat, name="deletecat"),


    path('managepackagetype/', views.managepackagetype, name= "managepackagetype"),
    path('savedat/', views.savedat, name="savedat"),
    path('packdisplay/', views.packdisplay, name="packdisplay"),
    path('editpack/<int:dataid>/', views.editpack, name="editpack"),
    path('updatepack/<int:dataid>/', views.updatepack, name="updatepack"),
    path('deletepack/<int:dataid>/', views.deletepack, name="deletepack"),

    path('addpackage/', views.addpackage, name="addpackage"),
    path('addpack/', views.addpack, name="addpack"),
    path('addpackdisplay/', views.addpackdisplay, name="addpackdisplay"),
    path('editpackage/<int:dataid>/', views.editpackage, name="editpackage"),
    path('deletepackage/<int:dataid>/', views.deletepackage, name="deletepackage"),
    path('updatepackage/<int:dataid>/', views.updatepackage, name="updatepackage"),

    path('admin_login/', views.admin_login, name="admin_login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecon/<int:dataid>/', views.deletecon, name="deletecon"),

    path('displaypayment/', views.displaypayment, name="displaypayment"),

    path('displayblog/', views.displayblog, name="displayblog"),
    path('deleteblog/<int:dataid>/', views.deleteblog, name="deleteblog"),

    path('displayreg/', views.displayreg, name="displayreg"),
]