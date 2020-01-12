from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
    

def home(request):
    return render(request, 'home.html')


def end(request):
    return render(request, "end.html")

addprice  =  []
total = None
objlist = []

def bill(request):
    productid=None
    number=None
    name=None
    price=int(0)
    newdata=None
 
    if request.GET.get('productid'):
        productid = request.GET.get('productid')
     
        
    if request.GET.get('number'):
        number = request.GET.get('number')
        
    if request.GET.get('name'):
        name = request.GET.get('name')
    
    if request.GET.get('price'):
        price = request.GET.get('price')        
    
    if(productid != None and name != None and number !=None and price != 0):
        newdata= [productid, name, number, price ]
    

    addprice.append(int(price))
    print(addprice)
    total = sum(addprice)
    print(total)
    
    

    objlist.append(newdata)

    print(addprice)
    
    return render(request, 'bill.html',{"objlist": objlist , "total" :  total}    
    )



def payment(request):
    return render(request, "payment.html")


def testform(request):
    return render(request, "testform.html")
