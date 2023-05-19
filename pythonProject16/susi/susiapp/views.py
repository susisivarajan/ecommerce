from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import movieform
from .models import ecommerce


def index(request):
    A=ecommerce.objects.all()

    return render(request,"new.html",{'name':A})
def detail(request,susi_id):
    a=ecommerce.objects.get(id=susi_id)
    return render(request,'view.html',{'name':a})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get("item",)
        price=request.POST.get('price',)
        size=request.POST.get('size',)
        brand=request.POST.get('Brand',)
        details=request.POST.get('details',)
        image=request.FILES['image']
        A=ecommerce(name=name,price=price,size=size,brand=brand,details=details,image=image)
        A.save()
        return redirect("/")
    return render(request, 'newapp.html')
def update_detail(request,new_id):
    A=ecommerce.objects.get(id=new_id)
    B=movieform(request.POST or None,request.FILES,instance=A)
    if B.is_valid():
        B.save()
        return redirect("/")
    else:
        form=movieform(instance=A)
    return render(request,"update.html",{'name1':form})
def delete_detail(request,delete_id):
     if request.method=="POST":
         D=ecommerce.objects.get(id=delete_id)
         D.delete()
         return redirect("/")
     return render(request,"delete.html",)
class list_view(ListView):
    model=ecommerce
    template_name ="new.html"
    context_object_name = "name"
class detail_view(DetailView):
    model=ecommerce
    template_name = "view.html"
    context_object_name = "name"
class update_view(UpdateView):
    model=ecommerce
    template_name = "edit.html"
    context_object_name = "form"
    fields=["name","price","brand","size","details","image"]
    def get_success_url(self):
        return reverse_lazy("detail",kwargs={"pk":self.object.id})
class delete_view(DeleteView):
    model = ecommerce
    template_name = "delete.html"
    success_url = reverse_lazy("list")


