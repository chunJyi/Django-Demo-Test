from ast import List
from calendar import month
from datetime import date, datetime
from multiprocessing import context
from sqlite3 import Date
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from bakery_shop.models import Customer


items = ['pancakes','cupcakes','cheesecake','cookies_donuts','croissant']


# http://127.0.0.1:8000/
def home(request):
    customers=Customer.objects.all()
    context={
        'items':items,
        'customers':customers
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))


# http://127.0.0.1:8000/item
def item(request,i=None):
    customers=Customer.objects.filter(item=i)

    context={
        'items':items,
        'customers':customers
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

# http://127.0.0.1:8000/promotionSale
def promotionSale(request):
    current_month=date.today().month
    customers=list( Customer.objects.filter(birthDay__month = current_month))
   
    # for c in customers:
    #     nd = c.birthDay
    #     print(type(nd))
    #     print(nd.strftime("%d"))

    customers.sort(key= lambda x : x.birthDay.strftime("%d"))
    
    context={
        'items':items,
        'customers':customers
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))



# http://127.0.0.1:8000/create
def create(request):
    items = ['pancakes','cupcakes','cheesecake','cookies donuts','croissant']
    gender =['male','female']
    context={
        'items':items,
        'gender':gender
    }
    template = loader.get_template('create.html')
    return HttpResponse(template.render(context, request))

# http://127.0.0.1:8000/createCustomer
def createCustomer(request) :
    if request.method == 'POST' :
        customer=Customer(
                name= request.POST['name'],
                phNo= request.POST['phNo'],
                address= request.POST['address'], 
                birthDay= request.POST['birthDay'],   
                gender= request.POST['gender'],
                item= request.POST['item'],
        )
        customer.save()
        messages.info(request,"SUCCESSFULLY! CREATED NEW CUSTOMER")
    else :
        pass
    return redirect('/create')
