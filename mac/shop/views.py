from django.shortcuts import render

from django.http import HttpResponse
from .models import Product,Contact
from math import ceil


# Create your views here.

def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def instagram(request):
    return HttpResponse("@zenny_esh")


def phone(request):
    return HttpResponse("Ph No: 9818248492")


def email(request):
    return HttpResponse("dare3462@gmail.com")


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("We are at contact page")


def tracker(request):
    return render(request, 'shop/tracker.html')


def productview(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(Product)
    return render(request, 'shop/Prodview.html', {'product':product[0]})


def feedback(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/feedback.html")


