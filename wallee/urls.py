"""wallee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from website import views
urlpatterns =[
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('signup/',views.signup1),
    path('wallet/',views.wallet1),
    path('logout/',views.logout1),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="website/login.html")),
    path('confirmemail/',views.emailconfirm),
path('resetpass/',views.resetpass),
path('dashboardedit/',views.dashboard1),
path('dashboard/',views.dashboard),
path('addmon/',views.addmoney),
path('cart/',views.conf),
path('shopping/',views.shopping),
    path('card/',views.card),
path('card1/',views.card1),
path('payment/',views.payment),
path('payment1/',views.payment1),
    path('cardpass/',views.cardpass),
path('cardpass1/',views.cardpass1),
    path('payselect/',views.payselect),
    path('netbank/',views.netbankmain),
path('netbank1/',views.netbank),
    path('cardselect/',views.cardselect),
path('cardselect1/',views.cardselect1),
path('cartpay/',views.cartpay),
path('walletpay/',views.walletpay),
path('moviebook/',views.tbook),
path('busbook/',views.btbook),
path('elebill/',views.bpay),
path('promo/',views.promo),


]
