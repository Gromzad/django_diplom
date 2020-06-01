from django.shortcuts import render
from .models import *
from django.core.paginator import *
from django.db.models import Q
from .models import Item
from django.shortcuts import redirect

# Create your views here.


def directory(request):
    try:
        obj1 = Category.objects.get(id=1)
        obj2 = Category.objects.get(id=2)
        obj3 = Category.objects.get(id=3)
        obj4 = Category.objects.get(id=4)
        obj5 = Category.objects.get(id=5)
        obj6 = Category.objects.get(id=6)
        context = {
            "data1": obj1,
            "data2": obj2,
            "data3": obj3,
            "data4": obj4,
            "data5": obj5,
            "data6": obj6,
        }
        return render(request, 'home.html', context)
    except DoesNotExist:
        raise Http404

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        items = Item.objects.filter(Q(title__icontains=q) | Q(text__icontains=q))
        paginator = Paginator(items, 4)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context = {'query': q, 'items': page_obj.object_list, 'paginator': paginator, 'page_number': int(page_number), }
    else:
        return redirect('directory:home')
    return render(request, 'results.html', context)


def metalproduction(request):
    items = Item.objects.filter(category_id=1)
    paginator = Paginator(items, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "items": page_obj.object_list,
        "paginator": paginator,
        "page_number": int(page_number),
    }
    return render(request, 'metalproduction.html', context)


def machinebuild(request):
    items = Item.objects.filter(category_id=2)
    paginator = Paginator(items, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "items": page_obj.object_list,
        "paginator": paginator,
        "page_number": int(page_number),
    }
    return render(request, 'machinebuild.html', context)


def instrproduction(request):
    items = Item.objects.filter(category_id=3)
    paginator = Paginator(items, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "items": page_obj.object_list,
        "paginator": paginator,
        "page_number": int(page_number),
    }
    return render(request, 'instrproduction.html', context)


def carbuild(request):
    items = Item.objects.filter(category_id=4)
    paginator = Paginator(items, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "items": page_obj.object_list,
        "paginator": paginator,
        "page_number": int(page_number),
    }
    return render(request, 'carbuild.html', context)


def traktorbuild(request):
    items = Item.objects.filter(category_id=5)
    paginator = Paginator(items, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "items": page_obj.object_list,
        "paginator": paginator,
        "page_number": int(page_number),
    }
    return render(request, 'traktorbuild.html', context)


def chembuild(request):
    items = Item.objects.filter(category_id=6)
    paginator = Paginator(items, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "items": page_obj.object_list,
        "paginator": paginator,
        "page_number": int(page_number),
    }
    return render(request, 'chembuild.html', context)


def metalproductionPost(request, slug):
    item = Item.objects.filter(slug=slug).first()
    context = {'item': item}
    return render(request, 'metalproduction_post.html', context)

def machinebuildPost(request, slug):
    item = Item.objects.filter(slug=slug).first()
    context = {'item': item}
    return render(request, 'machinebuild_post.html', context)

def instrproductionPost(request, slug):
    item = Item.objects.filter(slug=slug).first()
    context = {'item': item}
    return render(request, 'instrproduction_post.html', context)

def carbuildPost(request, slug):
    item = Item.objects.filter(slug=slug).first()
    context = {'item': item}
    return render(request, 'carbuild_post.html', context)

def traktorbuildPost(request, slug):
    item = Item.objects.filter(slug=slug).first()
    context = {'item': item}
    return render(request, 'traktorbuild_post.html', context)

def chembuildPost(request, slug):
    item = Item.objects.filter(slug=slug).first()
    context = {'item': item}
    return render(request, 'chembuild_post.html', context)

