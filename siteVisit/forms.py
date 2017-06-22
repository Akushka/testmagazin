# -*- coding: utf-8 -*

_autor_ ='macpro'

from django.forms import ModelForm
from .models import CommentArticle, SiteName, imageInArticle
from django import forms
from django.forms import CharField, Form, PasswordInput

class AutentificationUser(forms.Form):
    userName = CharField(widget=forms.TextInput())  
    password = CharField(widget=PasswordInput())
    fields = ['userName','passw']
        
class CommentForm(ModelForm):
    class Meta:
        model = CommentArticle
        fields = "__all__" 
        fields = ['articleAuthor','articleComment']
        
class NewArticleForm(ModelForm):
    class Meta:
        model = SiteName
        fields = ['id','author','articleTitle','articleText','category','price']
        
class AddImage(ModelForm):
    class Meta:
        model = imageInArticle
        fields = ['imagePath']
                

class EditArticleForm(ModelForm):
    class Meta:
        model = SiteName
      #  fields = "__all__" 
        fields = ['id','author','articleTitle','articleText','category','price','prevRecl','articleTextPreview','visible','viewed']
        

class FindArtikleForm(ModelForm):
    class Meta:
        model = SiteName
        fields = ['articleFindText']

class Feedback(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))  
    textFeedback = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control'})) 
    fields = ['email','textFeedback']
                
class sendOrder(forms.Form):
    FIO = forms.CharField(widget=forms.TextInput(attrs={'size':'20','class': 'form-control'}))
    City = forms.CharField(widget=forms.TextInput(attrs={'size':'20','class': 'form-control'}))
    Mobile = forms.CharField(widget=forms.TextInput(attrs={'size':'20','class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'size':'20','class': 'form-control'}))  
 #   commentInOrder = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control'}))
    fields = ['FIO','City','Mobile','email','commentInOrder']                
                