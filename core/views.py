import django.shortcuts
from .models import Melk, Unit, City, Ostan, Rosta
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
    
    if form.is_valid():
        postss= form.save()
        messages.success(request,"ثبت با موفقیت انجام شد...")
        form = UnitForm()
        return django.shortcuts.HttpResponseRedirect(postss.get_absolute_url())
   
    unit_list = Unit.objects.all()
    page = request.GET.get('page', 1)
    paginator1 = Paginator(unit_list, 5 ) # Show 5 unit per page  
    
    try:
        posts=paginator1.page(page)
    except PageNotAnInteger:     
        posts=paginator1.page(1)
    except(EmptyPage):
       posts = paginator1.page(paginator1.num_pages)

    context = {
      "post":post,
      "form":form,
      "posts":posts, 
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
    unit_list = Unit.objects.all()
    paginator = Paginator(unit_list, 5 ) # Show 5 unit per page
    try:
        page = int(request.GET.get('page', '1' ))
    except:
        page = 1
    try:
        posts=paginator.page(page)
    except(EmptyPage):
       posts = paginator.page(paginator.num_pages)
    context = {
      "postt":postt,
      "post":post,
      "form":form,
      "posts":posts,   
    }
    return django.shortcuts.render(request, 'core/unit_update.html', context)
    

def UnitDeleteView(request, id):
    post = django.shortcuts.get_object_or_404(Unit, id=id)
    if request.method == "POST":
       post.delete()
       return django.shortcuts.HttpResponseRedirect(post.get_absolute_url())
    return django.shortcuts.render (request, "core/confirm.html", {"post":post})

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
    # if not request.user.is_authenticated :
    #     return django.shortcuts.render (request, 'core/404err.html')
    #postt = get_object_or_404(Ostan,id=id)

    form = MelkForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save()
        messages.success(request, "ثبت با موفقیت انجام شد...")
        return django.shortcuts.HttpResponseRedirect(post.get_absolute_url())
        # else :
        #     messages.error(request, "فرم قانونی نیست")

    context = {
      "form":form,
        }
    return django.shortcuts.render (request, 'core/melk_insert1.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def MelkUpdateView(request):
   # postt = get_object_or_404(Melk, id=id)
    post = Melk.objects.all()

    # form = MelkForm(request.POST or None, instance=postt)
    # if form.is_valid():
    #     form.save()
    #     messages.success(request,"ویرایش با موفقیت انجام شد...")
    #     return HttpResponseRedirect(postt.get_absolute_url())
    #unit_list = Unit.objects.all()
    paginator = Paginator(post, 5 ) # Show 5 unit per page
    try:
        page = int(request.GET.get('page', '1' ))
    except:
        page = 1
    try:
        posts=paginator.page(page)
    except(EmptyPage):
       posts = paginator.page(paginator.num_pages)
    context = {
      #"postt":postt,
      "post":post,
      #"form":form,
      "posts":posts,   
    }

    return django.shortcuts.render (request, 'core/melk_update.html', context)


def MelkDeleteView(request, id):
    post = django.shortcuts.get_object_or_404(Unit, id=id)
    if request.method == "POST":
       post.delete()
       return django.shortcuts.HttpResponseRedirect(post.get_absolute_url())
    return django.shortcuts.render (request, "core/confirm.html", {"post":post})