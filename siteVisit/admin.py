# -*- coding: utf-8 -*
from django.contrib import admin
from siteVisit.models import SiteName, imageInArticle, ListOfCategories
from django import forms
from .widgets import *
from django.contrib.admin.widgets import AdminFileWidget
from siteVisit.models import Basket, ArrProduct

class ImageInArticle(admin.TabularInline):
    model = imageInArticle
   # list_display = ['imagePath', 'image_img']
    readonly_fields = ['image_img']
   # fields = ['imagePath', 'image_img']
    widgets = {'image':MultiFileInput}
    extra = 1    
    
class SiteAdmin(admin.ModelAdmin):
    fields = ('author', 'articleTitle','articleText','category','visible','price', 'prevRecl')
    widgets = {'image':MultiFileInput}
    inlines = [ImageInArticle]

class ArrProduct(admin.TabularInline):
    model = ArrProduct
    extra = 0
            
class SiteProduct(admin.ModelAdmin):
    fields = ('clientName','Basket_ip_id','time_of_creation')
    inlines = [ArrProduct]
 
           
admin.site.register(SiteName, SiteAdmin)
admin.site.register(Basket,SiteProduct)
admin.site.register(ListOfCategories)

