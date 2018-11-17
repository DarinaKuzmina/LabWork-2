from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'res'
urlpatterns = [
	path('', views.logPage, name='logPage'),
    path('registration/', views.registrationPage, name='registrationPage'),
    path('registrationQuery/', views.registrationQuery, name='registrationQuery'),
    path('logPage/', views.logPage, name='logPage'),
    path('loginin/', views.loginin, name='loginin'),
    path('index/', views.index, name='index'),
    path('firstpage/', views.firstpage, name='firstpage'),
    path('add_categorie/', views.add_categorie, name='add_categorie'),
    path('add_rss/', views.add_rss, name='add_rss'),
    path('logout/', views.logoutQuery, name='logout'),
    path('deletee/<int:rss_id>', views.deletee, name='deletee'),
    path('rssPage/<int:rssId>', views.rssPage, name='rssPage'),
    path('search/', views.search, name='search'),
    path('search2/<int:rssId>', views.search2, name='search2'),
]