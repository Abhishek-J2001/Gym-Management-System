from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.homepage, name= "homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('classpage/', views.classpage, name="classpage"),
    path('contactdata/', views.contactdata, name="contactdata"),
    path('classtimepage/', views.classtimepage, name="classtimepage"),
    path('servicepage/', views.servicepage, name="servicepage"),
    path('teampage/', views.teampage, name="teampage"),
    path('paymentpage/', views.paymentpage, name="paymentpage"),
    path('paymentdata/', views.paymentdata, name="paymentdata"),
    path('blogpage/', views.blogpage, name="blogpage"),
    path('blogdata/', views.blogdata, name="blogdata"),
    path('regpage/', views.regpage, name= "regpage"),
    path('savereg/', views.savereg, name="savereg"),
    path('edit_page/', views.edit_page, name="edit_page"),
    path('updateprofile/<int:dataid>/', views.updateprofile, name="updateprofile"),
    path('login_page/', views.login_page, name= "login_page"),
    path('user_login/', views.user_login, name= "user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('profile_page/', views.profile_page, name= "profile_page"),
]
