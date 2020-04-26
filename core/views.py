import django.shortcuts
import csv,io, json
import logging
from django.urls import reverse
#from .filters import MelkFilter
from django.http import HttpResponseRedirect,HttpResponse

from django.shortcuts import render
#from .forms import UploadFileForm
# from somewhere import handle_uploaded_file
from django.http import JsonResponse, request
from .models import Melk, Unit, City, Ostan
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UnitForm, MelkForm, UserLoginForm, UserRegisterForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from click import prompt
from django.core import serializers
from jalali_date import datetime2jalali, date2jalali

# def my_view(request):
# 	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

# @login_required
def index_view(request):
    post = Unit.objects.all()
    form = UnitForm()
    return django.shortcuts.render(request, 'core/index.html', {"post":post})

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        if next:
            return django.shortcuts.redirect(next)
        return django.shortcuts.redirect('/core')
    context = {
        'form' : form,
        }
    return django.shortcuts.render(request, 'core/login.html', context)

def Register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, " ثبت نام با موفقیت انجام شد.")
        new_user = authenticate(username=user.username, password=password)
        login(request,new_user)
        if next:
            return django.shortcuts.redirect(next)
        return django.shortcuts.redirect('/core/register')
    context = {
        'form' : form,
        }
    return django.shortcuts.render(request, 'core/signup1.html', context)

def logout_view(request):
    logout(request)
    return django.shortcuts.redirect('/core/login')

def UnitCreateView(request):
    form = UnitForm(request.POST or None)
    post = Unit.objects.all()
    ucode = request.POST.get('u_code')
    
    if ucode !='' or None:
        if post.filter(u_code = ucode):
            messages.success(request,"منطقه مورد نظر قبلا ثبت شده است")
        elif form.is_valid():
            postss= form.save()
            messages.success(request,"ثبت با موفقیت انجام شد...")
            form = UnitForm()
            return django.shortcuts.HttpResponseRedirect(postss.get_absolute_url())
    
   
    # unit_list = Unit.objects.all()
    # page = request.GET.get('page', 1)
    # paginator1 = Paginator(unit_list, 10 ) # Show 5 unit per page  
    
    # try:
    #     posts=paginator1.page(page)
    # except PageNotAnInteger:     
    #     posts=paginator1.page(1)
    # except(EmptyPage):
    #    posts = paginator1.page(paginator1.num_pages)

    context = {
      "post":post,
      "form":form,
    #   "posts":posts, 
    }
    return django.shortcuts.render(request, 'core/unit_edit.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
def UnitUpdateView(request, id):
   
    postt = django.shortcuts.get_object_or_404(Unit, id=id)
    post = Unit.objects.all()
    
    form = UnitForm(request.POST or None, instance=postt)
    if form.is_valid():
        form.save()
        messages.success(request,"ویرایش با موفقیت انجام شد...")
        return django.shortcuts.HttpResponseRedirect(postt.get_absolute_url())
    # unit_list = Unit.objects.all()
    # paginator = Paginator(unit_list, 10 ) # Show 5 unit per page
    # try:
    #     page = int(request.GET.get('page', '1' ))
    # except:
    #     page = 1
    # try:
    #     posts=paginator.page(page)
    # except(EmptyPage):
    #    posts = paginator.page(paginator.num_pages)
    context = {
      "postt":postt,
      "post":post,
      "form":form,
    #   "posts":posts,   
    }
    return django.shortcuts.render(request, 'core/unit_update.html', context)
    

def UnitDeleteView(request, id):
    post = django.shortcuts.get_object_or_404(Unit, id=id)
    if request.method == "POST":
       post.delete()
       return django.shortcuts.HttpResponseRedirect(post.get_absolute_url())
    return django.shortcuts.render (request, "core/confirm_unit.html", {"post":post})

def Upload_view(request):
    #post = get_object_or_404(Melk)
    # if form.is_valid():
    #     form.save()
    #     messages.success(request,"ثبت با موفقیت انجام شد...")
    #     return HttpResponseRedirect(form.get_absolute_url())
    # if request.method == "POST":
    #    post.save()
    #    messages.success(request,"ثبت با موفقیت انجام شد...")
    #    return HttpResponseRedirect(post.get_absolute_url())
    return django.shortcuts.render (request, "core/upload.html")



def MelkCreateView(request):
    # jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
    
    form = MelkForm(request.POST or None, request.FILES or None)
    post = Melk.objects.all()
    sanadasli = request.POST.get('sanad_asli')
    
    if sanadasli !='' or None:
        
        
        if post.filter(sanad_asli = sanadasli):
            messages.success(request,"این سند قبلا ثبت شده است")
        
        elif form.is_valid():
            
            post = form.save()
            messages.success(request, "ثبت با موفقیت انجام شد...")
            return django.shortcuts.HttpResponseRedirect(post.get_absolute_url())
        else :
            messages.error(request, "فرم قانونی نیست")
    # ostan_id = request.GET.get('ostanid')
    # cities = City.objects.filter(ostan_id=ostan_id).order_by('name')
    # city_id = request.GET.get('cityid')
    
    
    context = {
      "form":form,
      "post":post,
    }
    return django.shortcuts.render (request, 'core/melk_insert1.html', context)


def is_valid_queryparam(param):
   return param != '' and param is not None

def MelkUpdateView(request):
    post = Melk.objects.all()

    melksearch1 = request.POST.get('melksearch')
    # post = MelkFilter(request.GET, queryset=Melk.objects.all())
    
    if is_valid_queryparam(melksearch1):
       post = post.filter(melk_name = melksearch1)
   
    # paginator = Paginator(post, 15 ) # Show 5 unit per page
    # try:
    #     page = int(request.GET.get('page', '1' ))
    # except:
    #     page = 1
    # try:
    #     posts=paginator.page(page)
    # except(EmptyPage):
    #    posts = paginator.page(paginator.num_pages)
    ostan_id = request.GET.get('ostan')
    cities = City.objects.filter(ostan_id=ostan_id).order_by('name')
    city_id = request.GET.get('city')
    # rosta = Rosta.objects.filter(city_id=city_id).order_by('name')
    context = {
      "post":post,  
      "cities" :cities,
    #   "rostas":rosta,
    #   "posts":posts,   
    }

    return django.shortcuts.render (request, 'core/melk_update.html', context) 
    
   

def MelkDeleteView(request, id):
    post = django.shortcuts.get_object_or_404(Melk, id=id)
    if request.method == "POST":
       post.delete()
       return django.shortcuts.HttpResponseRedirect(post.get_absolute_url())
    return django.shortcuts.render (request, "core/confirm_melk.html", {"post":post})

def upload_csv(request):
    template = "core\csvupload.html"
    prompt= {'order':'فایل شما دارای کدمنطقه و نام منطقه باشد.'}
    if request.method=="GET":
       return render(request, template, prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'این فایل csv نیست')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',',quotechar="|"):
        _,created = City.objects.update_or_create(
            id=column[0],
            name=column[1],
            ostan_id=column[2],
        )
    context={}
    return render(request,template,context)

def download_csv(request):
    items = Unit.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="unit.csv"'
    writer = csv.writer(response,delimiter=',')
    writer.writerow(['u_code','u_name'])

    for obj in items:
        writer.writerow([obj.u_code,obj.u_name])
    return response
    


def all_json_models(request, id):
    current_brand = Ostan.objects.get(code=id)
    models = City.objects.all().filter(brand=current_brand)
    json_models = serializers.serialize("json", models)
    return HttpResponse(json_models, mimetype="application/javascript")

