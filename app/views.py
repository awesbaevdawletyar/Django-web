from django.shortcuts import render
from .models import Order
from cms.models import CmsSlider
from .forms import OrderForm
# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    # form=OrderForm()
    return render(request,'./index.html',{'slider_list': slider_list,
                                        })
def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element=Order(order_name=name,order_phone=phone)
    element.save()
    return render(request,'./thanks.html',{'name':name,'phone':phone})

