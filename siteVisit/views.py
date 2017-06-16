# -*- coding: utf-8 -*
from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from siteVisit.models import SiteName, CommentArticle, imageInArticle,ListOfCategories
from siteVisit.models import Basket, ArrProduct
from django.utils import timezone
import time
import os.path
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from .forms import CommentForm, NewArticleForm, EditArticleForm, FindArtikleForm, Feedback, AddImage, AutentificationUser, sendOrder
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError
from ctypes.test.test_errno import threading
import socket
import datetime    
from pip._vendor.requests.models import Response



def article_list(request, pk):
    
#Если первый заход, то создаём корзину, иначе загружаем существующую
#и проверяем, если есть корзины >6 часов, то удаляем их    
    Baskets = Basket.objects.all()
    
    for BaskAdd in Baskets:
        timeDelta = datetime.datetime.strptime(str(datetime.datetime.now()), "%Y-%m-%d %H:%M:%S.%f") - datetime.datetime.strptime(BaskAdd.Basket_ip_id, "%Y-%m-%d %H:%M:%S.%f")
        if timeDelta.seconds / 60  > 360:   #корзина сохраняеться шесть часов
            BaskAdd.delete()
    
    Baskets = Basket.objects.all()    
    client = False
    for BaskAdd in Baskets:
        try:
            if BaskAdd.Basket_ip_id in request.COOKIES.get('1'):
                client = True
                break
        except:
            None   
    if client == False:
        BaskAdd = Basket()
        BaskAdd.Basket_ip_id =  str(datetime.datetime.now())
        BaskAdd.clientName = 'user'
        BaskAdd.save()
        
        response = redirect('/')
        response.set_cookie( '1', BaskAdd.Basket_ip_id)
        return response
    
    Products = ArrProduct.objects.filter(Basket_id = BaskAdd.pk) 
    arrProducts = []
    for Product in Products:
        try:
            arrProducts.append(SiteName.objects.get(pk=int(Product.Product)))
        except:
            None    
    
    articles = SiteName.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    
    products = ArrProduct.objects.filter(Basket_id = BaskAdd.pk)
    countProduct = 0
    for product in products:
        countProduct += 1
    
#Загружаем категории
   #админская часть
    if int(pk) == 999:
        Categories = ListOfCategories.objects.all()
        
          
    filter = '' 
    if int(pk) != 999:
        Categories = ListOfCategories.objects.all()    
        pkCat = int(pk)
        category = ListOfCategories.objects.get(Id_Categories = pkCat)  
        filter = category.Categories
    #Если выбранно "всё", т.е. 0    
        if pkCat == 0:
            filter = ''
   
    #articles.imagePath = []
    args = {}
    args['article'] = []
    autentificatio_form = AutentificationUser
    args['userForm'] = AutentificationUser
    find_form = FindArtikleForm
    args['form'] = find_form
    args['PrevArray'] = []
    args['BaskAdd'] = BaskAdd
    args['countProduct'] = countProduct
    args['arrProducts'] = arrProducts
     
    form = FindArtikleForm(request.POST)
    
    for article in articles:
        article.tryCategory = False
        if (filter == '') or (article.category.lower().find(filter.lower()) > -1):
            article.tryCategory = True
        comments = CommentArticle.objects.filter(article_id = article.id)
        for comment in comments:
            article.countComment += 1 


#Если ставим фильтр    
    if request.method == "POST":
        if form.is_valid():
            findFilter = form.save(commit = False)
            for article in articles:
                article.articleFindText = findFilter.articleFindText
    
        
    for article in articles:
        
        images = imageInArticle.objects.filter(image_id = article.pk)
        if len(images)>0:
            article.imagePathBegin = images[0].imagePath.url
# Проверяем и заполняем превьюшными (рекламными) картинками и текстом масив PrevArray
        if article.prevRecl == True:
            for image in images:
                args['PrevArray'].append(image.imagePath.url)
            
        #article.articleTextPreview = article.articleText[:100]
        if (article.articleText.lower().find(article.articleFindText.lower())>-1) & (article.tryCategory == True):
            args['article'].append(article)    
    if int(pk) != 999:
        return render(request, 'siteVisit/Article_list.html', {'timeDelta':timeDelta, 'form': args['form'],'userForm':args['userForm'], 'articles' : args['article'], 'countProduct':args['countProduct'], 'BaskAdd':args['BaskAdd'], 'arrProducts':args['arrProducts'], 'PrevArray': args['PrevArray'], 'Categories':Categories})
    if int(pk) == 999:
        return render(request, 'siteVisit/Article_list_admin.html', {'timeDelta':timeDelta, 'form': args['form'],'userForm':args['userForm'], 'articles' : args['article'], 'countProduct':args['countProduct'], 'BaskAdd':args['BaskAdd'], 'arrProducts':args['arrProducts'], 'PrevArray': args['PrevArray'], 'Categories':Categories})

# перенаправляем на сайт с фильтром  "на всё" (+ "/0")
def article_list2(request):
    return redirect(article_list, 0)  

def article_list_admin(request):
    return redirect(article_list, 999)  
  
def autentificationUser(request):
    return render_to_response('siteVisit/test.html')

def test(request):
    return render_to_response('siteVisit/test.html')

def article_detail(request, pk ):
    products = ArrProduct.objects.all()
    countProduct = 0
    for product in products:
        countProduct += 1
        
    nomImage = 0
    comment_form = CommentForm
    
#Загружаем категории
    Categories = ListOfCategories.objects.all()    
    
    args = {}
   # args.update(csrf(request))
    args['article'] = SiteName.objects.get(id=pk)
    args['comments'] = CommentArticle.objects.filter(article_id = pk)
    args['form'] = comment_form
    args['images'] = imageInArticle.objects.filter(image_id = pk)
    args['userForm'] = AutentificationUser
    args['countProduct'] = countProduct
    args['Categories'] = Categories
    

    Baskets = Basket.objects.all()
    try:
        for Bask in Baskets:
            if Bask.Basket_ip_id in request.COOKIES.get('1'):
                BaskAdd = Bask
                args['BaskAdd'] = BaskAdd
                break
    except:
        None   
            
    Products = ArrProduct.objects.filter(Basket_id = BaskAdd.pk)
        
    arrProducts = []
    for Product in Products:
        try:
            arrProducts.append(SiteName.objects.get(pk=int(Product.Product)))
        except:
            None
    args['arrProducts'] = arrProducts   
    
   # STATIC_ROOT = os.path.abspath(os.path.dirname(__file__))
    #args['article'].imagePath.append(args['article'].articleTitle+'_'+str(0)+'.jpg')
    #for i in range(10):
        #if os.path.isfile('siteVisit/static/media/'+args['article'].articleTitle+'_'+str(i)+'.jpg'):
        #    args['article'].imagePath.append('media/'+args['article'].articleTitle+'_'+str(i)+'.jpg')
    #    args['article'].imagePath.append('media/'+args['article'].articleTitle+'_'+str(i)+'.jpg')
            
#Для pythonanywhere ------------------           
        #if os.path.isfile(os.path.join(STATIC_ROOT,'../static/media/'+args['article'].articleTitle+'_'+str(i)+'.jpg')):
        #    args['article'].imagePath.append('\\media\\'+args['article'].articleTitle+'_'+str(i)+'.jpg')
#Для pythonanywhere ------------------
                    
   # args['article'].imagePathBegin = 'media/'+args['article'].articleTitle+'_'+str(nomImage)+'.jpg'
    if len(args['images'])>0:
        args['article'].imagePathBegin = args['images'][0].imagePath
        
    return render_to_response('siteVisit/Article_detail.html', args )

def article_detail_admin(request, pk ):
    products = ArrProduct.objects.all()
    countProduct = 0
    for product in products:
        countProduct += 1
        
    nomImage = 0
    comment_form = CommentForm
    
#Загружаем категории
    Categories = ListOfCategories.objects.all()    
    
    args = {}
   # args.update(csrf(request))
    args['article'] = SiteName.objects.get(id=pk)
    args['comments'] = CommentArticle.objects.filter(article_id = pk)
    args['form'] = comment_form
    args['images'] = imageInArticle.objects.filter(image_id = pk)
    args['userForm'] = AutentificationUser
    args['countProduct'] = countProduct
    args['Categories'] = Categories
    

    Baskets = Basket.objects.all()
    try:
        for Bask in Baskets:
            if Bask.Basket_ip_id in request.COOKIES.get('1'):
                BaskAdd = Bask
                args['BaskAdd'] = BaskAdd
                break
    except:
        None   
            
    Products = ArrProduct.objects.filter(Basket_id = BaskAdd.pk)
        
    arrProducts = []
    for Product in Products:
        try:
            arrProducts.append(SiteName.objects.get(pk=int(Product.Product)))
        except:
            None    
    args['arrProducts'] = arrProducts   
    
   # STATIC_ROOT = os.path.abspath(os.path.dirname(__file__))
    #args['article'].imagePath.append(args['article'].articleTitle+'_'+str(0)+'.jpg')
    #for i in range(10):
        #if os.path.isfile('siteVisit/static/media/'+args['article'].articleTitle+'_'+str(i)+'.jpg'):
        #    args['article'].imagePath.append('media/'+args['article'].articleTitle+'_'+str(i)+'.jpg')
    #    args['article'].imagePath.append('media/'+args['article'].articleTitle+'_'+str(i)+'.jpg')
            
#Для pythonanywhere ------------------           
        #if os.path.isfile(os.path.join(STATIC_ROOT,'../static/media/'+args['article'].articleTitle+'_'+str(i)+'.jpg')):
        #    args['article'].imagePath.append('\\media\\'+args['article'].articleTitle+'_'+str(i)+'.jpg')
#Для pythonanywhere ------------------
                    
   # args['article'].imagePathBegin = 'media/'+args['article'].articleTitle+'_'+str(nomImage)+'.jpg'
    if len(args['images'])>0:
        args['article'].imagePathBegin = args['images'][0].imagePath
        
    return render_to_response('siteVisit/Article_detail_admin.html', args )

def addcomment(request, pk):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit = False)
                comment.article_id = SiteName.objects.get(pk=pk)
                form.save()
    else:
        None            
    return redirect('/siteVisit/%s/' % pk)        


def delComment(request, pkCom):
    if request.method == "POST":
        comment = CommentArticle.objects.get(pk=pkCom)
        pkArt = comment.article_id.id
        
        article = SiteName.objects.get(pk=pkArt)
        article.author = request.user
        
        comment.delete()
   # return redirect('/siteVisit/%s/' % pkArt)     
    return redirect(article_detail_admin, pkArt)  

def article_add(request):
    article = SiteName()
   # article.author = request.user
    article.tryCategory = True
    article.prevRecl = False
    article.countComment = 0
    article.price = 0
    article.category = 'Всё'
    article.save(force_insert=True)
    return redirect(article_edit, article.pk)

def addInBasket(request,pk, pk_bask, index):
    ArrProd = ArrProduct.objects.filter(Basket_id = pk_bask)
    truProduct = False 
    for Product in ArrProd:
        if int(Product.Product) == int(pk):
            truProduct = True
    if truProduct == False:
        ArrProducts  = ArrProduct()
        ArrProducts.Product = pk
        ArrProducts.countProduct = 1
        ArrProducts.Basket_id = Basket.objects.get(pk=pk_bask)
        ArrProducts.save(force_insert=True)
    if int(index) == 0:
        return redirect(article_list, 0)
    else:
        return redirect(article_detail, pk)
        
def InBasket(request, pk_bask, pk_del):
    BaskAdd = Basket.objects.get(pk=pk_bask)
    arrProducts = []
    sum = 0
#Загружаем категории
    Categories = ListOfCategories.objects.all()    

    Products = ArrProduct.objects.filter(Basket_id = pk_bask)
    for Product in Products:
        try:
            if int(Product.Product) == int(pk_del):
                Product.delete()
            if int(Product.Product) != int(pk_del):
                arrProducts.append(SiteName.objects.get(pk=int(Product.Product)))
                sum += arrProducts[len(arrProducts)-1].price
        except:
            None        
                
    return render(request, 'siteVisit/basket.html', {'sum':sum, 'arrProducts': arrProducts, 'pk_bask':pk_bask, 'Categories':Categories, 'BaskAdd':BaskAdd})

def order(request, pk_bask):
    
    Categories = ListOfCategories.objects.all() 
    
    BaskAdd = Basket.objects.get(pk=pk_bask)
    arrProducts = []
    sum = 0
    
    Products = ArrProduct.objects.filter(Basket_id = pk_bask)
    for Product in Products:
        try:
            arrProducts.append(SiteName.objects.get(pk=int(Product.Product)))
            sum += arrProducts[len(arrProducts)-1].price
        except:
            None
        
    if request.POST:
        form = sendOrder(request.POST)
        if form.is_valid():
            FIO = form.cleaned_data['FIO']
            City = form.cleaned_data['City']
            Mobile = form.cleaned_data['Mobile']
            email = form.cleaned_data['email']
            arrayOrder = 'Имя покупателя - ' +FIO+ ' , '+ ' Город - '+City+' , '+' Телефон - '+ Mobile + ' , '+' E-Mail - '+email
            arrayOrder = arrayOrder +' , ' 
            for product in arrProducts:
                arrayOrder = arrayOrder + ' , '+ product.articleTitle+' ( '+str(product.price)+' )'
            arrayOrder = arrayOrder +' , '+ 'Общая цена - '+ str(sum) 
            recepients = ['anatoliy.kushka@tns-ua.com','mysiteadmkushka@gmail.com']
            
#Очищаем корзину
            for Product in Products:
                Product.delete()
        
            try:
                send_mail('Покупка!!!', arrayOrder , 'mysiteadmkushka@gmail.com', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            return article_list(request, 0)
    else:
        form = sendOrder()
                
    return render(request, 'siteVisit/order.html', {'form':form,'sum':sum, 'arrProducts': arrProducts, 'pk_bask':pk_bask, 'Categories':Categories, 'BaskAdd':BaskAdd})
    
def article_edit(request, pk):
    if pk != 999:
        article = get_object_or_404(SiteName, pk=pk)
   # article.author = request.user
        arrImage = imageInArticle.objects.filter(image_id = pk)
    if pk == 999:
        form = EditArticleForm(request.POST, instance=article)
        return redirect(article_edit, article.pk)
    
    if request.method == "POST":
        form = EditArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

        formAddImage = AddImage(request.POST, request.FILES)
        if formAddImage.is_valid():
            imageAdd = formAddImage.save(commit = False)
            imageAdd.image_id = SiteName.objects.get(pk=article.id)
            form = EditArticleForm(instance=article)
            #form = EditArticleForm(request.POST, instance=article)
            #if form.is_valid():
            #    article = form.save(commit=False)
            #    article.save()
            
            if imageAdd.imagePath:
                imageAdd.save()
                
            #form = EditArticleForm(instance=article)    
            
    else:
        form = EditArticleForm(instance=article)
        formAddImage = AddImage()
   # form = EditArticleForm(instance=article)    
    Categories = ListOfCategories.objects.all()
    return render(request, 'siteVisit/article_edit.html', {'form': form, 'formAddImage':formAddImage, 'arrImage': arrImage, 'article':article, 'Categories':Categories})

def delArticle(request, pk):
    if request.method == "POST":
        article = SiteName.objects.get(pk=pk)
       # article.author = request.user
        article.delete()
    return redirect(article_list, 999)        

def delPicture(request,pkArt,  pkPic):
    if request.method == "POST":
        delPic = imageInArticle.objects.get(pk=pkPic)
        article = SiteName.objects.get(pk=pkArt)
        article.author = request.user
        delPic.delete()
    return redirect(article_edit, pkArt)    

def feedback(request):
    
    Categories = ListOfCategories.objects.all()
    
    Baskets = Basket.objects.all()
    try:
        for Bask in Baskets:
            if Bask.Basket_ip_id in request.COOKIES.get('1'):
                BaskAdd = Bask
                break
    except:
        None 
        
    Products = ArrProduct.objects.filter(Basket_id = BaskAdd.pk)
        
    arrProducts = []
    for Product in Products:
        try:
            arrProducts.append(SiteName.objects.get(pk=int(Product.Product)))
        except:
            None
            
    if request.POST:
        form = Feedback(request.POST)
        if form.is_valid():
  #          email = form.cleaned_data['email']
            textFeedback = form.cleaned_data['textFeedback']
            recepients = ['anatoliy.kushka@tns-ua.com','mysiteadmkushka@gmail.com']
            try:
                send_mail('', textFeedback, 'mysiteadmkushka@gmail.com', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            return article_list(request, 0)
    else:
        form = Feedback()
    return render(request, 'siteVisit/FeedBack.html', {'form': form, 'Categories':Categories, 'BaskAdd':BaskAdd, 'arrProducts':arrProducts})


    