from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage (request):
    #Homepage = homepage.objects.all()
    return render (request, 'homepage/homepage.html', {'homepage':homepage})
    #'veterinaria/homepage.html',{'homepage': Homepage})
def customerRegistration(request):
    #CustomerRegistration = customerRegistration.objects.all()
    return render (request, 'customerRegistration/customerRegistration.html',{'customerRegistration':customerRegistration})
    #'veterinaria/customerRegistration.html',{'customerRegistration': CustomerRegistration})
def ourProducts(request):
    #OurProducts = ourProducts.objects.all()
    return render (request,'ourProducts/ourProducts.html',{'ourProducts': ourProducts})
    #'veterinaria/ourProducts.html',{'ourProducts': OurProducts})
def ourServices(request):
    #OurServices = ourServices.objects.all()
    return render (request,'ourServices/ourServices.html',{'ourServices': ourServices})
    #'veterinaria/ourServices.html',{'ourServices': OurServices})
def stockRegistration(request):
    #StockRegistration =stockRegistration.objects.all()
    return render (request,'stockRegistration/stockRegistration.html',{'stockRegistration': stockRegistration})
    #'veterinaria/stockRegistration.html',{'stockRegistration': StockRegistration})