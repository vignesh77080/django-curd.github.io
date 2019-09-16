from django.shortcuts import render 
from django.http import HttpResponse , HttpResponseRedirect
from curd_app.models import CurdOperations

# Create your views here.
from django.urls import path, reverse

def home(request):
    question = CurdOperations.objects.order_by('-id')[:5]
    return render(request, 'home_page.html',{'question':question})

def submit(request):

    a = request.POST.get('first_name');
    b = request.POST.get('age');
    print(a,b);
    curd_ops = CurdOperations(first_name = a, age = b);
    curd_ops.save();
    get_items = CurdOperations.objects.order_by('-id')

    return render(request, 'home_page.html' ,{'get_items':get_items})

def edit(request , base_id):

    select_by_id = CurdOperations.objects.get(pk=base_id)
    return render(request, 'update.html' , {'select_by_id':select_by_id} )

def update(request , base_id):

    a = request.POST.get('first_name');
    b = request.POST.get('age');
    update_using_id = CurdOperations.objects.get(pk=base_id);

    update_using_id.first_name = a;
    update_using_id.age = b;
    update_using_id.save();

    return HttpResponseRedirect(reverse('curd_app:home'))


def delete_rec(request, base_id):

    delete_using_id = CurdOperations.objects.filter(pk=base_id).delete();
    #delete_using_id.save();

    return HttpResponseRedirect(reverse('curd_app:home'))


