# -*- coding: utf-8 -*
from django.conf.urls import url
from . import views
from django.conf.urls import * 
from django.contrib import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^superadmin/$', views.article_list_admin, name='article_list_admin'),
    url(r'^$', views.article_list2, name='article_list2'),
    url(r'^(?P<pk>[0-9]+)/$', views.article_list, name='article_list'),
    url(r'^siteVisit/autentificationUser/$', views.autentificationUser, name='autentificationUser'),
    url(r'^siteVisit/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^siteVisit/superadmin/(?P<pk>[0-9]+)/$', views.article_detail_admin, name='article_detail_admin'),
    url(r'^siteVisit/edit/(?P<pk>[0-9]+)/$', views.article_edit, name='article_edit'),
    url(r'^siteVisit/addcomment/(?P<pk>[0-9]+)/$', views.addcomment, name='addcomment'),
    url(r'^siteVisit/delComment/(?P<pkCom>[0-9]+)/$', views.delComment, name='delComment'),
    url(r'^siteVisit/delArticle/(?P<pk>[0-9]+)/$', views.delArticle, name='delArticle'),
    url(r'^siteVisit/delPicture/(?P<pkArt>[0-9]+)/(?P<pkPic>[0-9]+)/$', views.delPicture, name='delPicture'),
    url(r'^siteVisit/article_add/$', views.article_add, name='article_add'),
    url(r'^siteVisit/test/$', views.test, name='test'),
    url(r'^siteVisit/FeedBack/$', views.feedback, name='feedback'),
    url(r'^siteVisit/addInBasket/(?P<pk>[0-9]+)/(?P<pk_bask>[0-9]+)/(?P<index>[0-9]+)/$', views.addInBasket, name='addInBasket'),
    url(r'^siteVisit/InBasket/(?P<pk_bask>[0-9]+)/(?P<pk_del>[0-9]+)/$', views.InBasket, name='InBasket'),
    url(r'^siteVisit/order/(?P<pk_bask>[0-9]+)/$', views.order, name='order'),
    url(r'^siteVisit/statik/$', views.CreateStatik, name='CreateStatik'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
