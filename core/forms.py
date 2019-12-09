from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Melk, Unit, Ostan, City, Rosta


User = get_user_model()

class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm rounded bright', 'placeholder': 'جستجو1'}))


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد نمایید'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'کلمه عبور خود را وارد نمایید'}))

    def clean_username(self):
        data = self.cleaned_data['username']
        #password = self.cleaned_data('password')

        if data != User.username():
            user = authenticate(username=data)
            if not user:
                raise ValidationError(_('نام کاربری وجود ندارد'))
            # if not user.check_password(password):
            #     raise forms.ValidationError('کلمه عبور اشتباه است')
            if not user.is_active:
                raise ValidationError(_('کاربر فعال نیست'))
            #return super(UserLoginForm, self).clean(*args, **kwargs)
            return data

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری '}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'پست الکترونیک'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'کلمه عبور'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار کلمه عبور'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]

    def clean_password(self, *args, **kwargs):
        # password = self.cleaned_data.get('password')
        # password2 = self.cleaned_data.get('password2')
        # if password != password2 :
        #     raise forms.ValidationError("  کلمه عبور را عینا تکرار نمایید")
        # password = User.objects.filter(password=password)
        # if password_qs.exists():
        #     raise forms.ValidationError(" این ایمیل وجود دارد")
        return super(UserRegisterForm, self).clean(*args, **kwargs)


class UnitForm(forms.ModelForm):
    u_code = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'کد منطقه'}))
    u_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام منطقه'}))

    class Meta:
        model = Unit
        fields = ['u_code', 'u_name']

    def clean_ucode(self, *args, **kwargs):
        u_code = self.cleaned_data.get("u_code")
        if "CFE" in u_code:
            return u_code
        else:
            raise forms.ValidationError("This is not valid title")


# class MelkFormAsli(forms.ModelForm):


#     melk_name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام ملک'}))
#     khayer_name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام واگذار کننده'}))
#     sanad_asli = forms.CharField(widget= forms.NumberInput(attrs={'class':'form-control', 'placeholder':'سند اصلی'}))
#     sanad_farye = forms.CharField(widget= forms.NumberInput(attrs={'class':'form-control', 'placeholder':'سند فرعی'}))
#     CHOICES1 =(
#             ('1','عادی'),
#             ('2','قطعی دفترچه ای'),
#             ('3','قطعی غیرمنقول'),
#             ('4','صلح نامه'),
#             ('5','وقف نامه'),
#             ('6','ابتیاعی')
#             )
#     sanad_type = forms.ChoiceField(widget= forms.Select(attrs={'class':'form-control', 'placeholder':'نوع سند'}), choices=CHOICES1)
#     CHOICES2 =(
#             ('1','آموزشی'),
#             ('2','اداری'),
#             ('3','مسکونی'),
#             ('4','غیره')

#             )   

#     melk_karbari = forms.ChoiceField(widget= forms.Select(attrs={'class':'form-control', 'placeholder':'نوع کاربری ملک'}), choices=CHOICES2)
#     CHOICES3 =(
#             ('1',' آموزش و پرورش'),
#             ('2','اوقاف'),
#             ('3','دولت'),
#             ('4','آستانه'),
#             ('5','غیره'),

#             )
#     melk_motavali = forms.ChoiceField(widget= forms.Select(attrs={'class':'form-control', 'placeholder':'متولی ملک'}), choices=CHOICES3)
#     CHOICES4 =(
#             ('1','درحال بهره برداری'),
#             ('2','کشاورزی'),
#             ('3','زمین')

#             )
#     melk_state = forms.ChoiceField(widget= forms.Select(attrs={'class':'form-control', 'placeholder':'وضعیت ملک'}), choices=CHOICES4)

#     class Meta:
#         model = Melk
#         fields = ['melk_name', 'khayer_name','sanad_asli','sanad_farye','sanad_type','melk_karbari','melk_state','melk_motavali'
#                     ]
# class MelkFormOmomi(forms.ModelForm):

#     melk_year = forms.DateField(widget= forms.DateInput(attrs={'class':'form-control', 'placeholder':'تاریخ سند'}))
#     melk_price = forms.CharField(widget= forms.NumberInput(attrs={'class':'form-control', 'placeholder':'قیمت ملک'}))
#     melk_arseh = forms.CharField(widget= forms.NumberInput(attrs={'class':'form-control', 'placeholder':'عرصه ملک'}))
#     melk_ayan = forms.CharField(widget= forms.NumberInput(attrs={'class':'form-control', 'placeholder':'اعیان ملک'}))
#     melk_comment = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control', 'placeholder':'توضیحات سند'}))
#     melk_pic = forms.ImageField(widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'تصویر سند'}))
#     class Meta:
#         model = Melk
#         fields = ['melk_year','melk_price','melk_arseh','melk_ayan','melk_comment','melk_pic']

# class MelkFormAddress(forms.ModelForm):

#     Ostan =(
#         ('1','خراسان رضوی'),
#         ('2','خراسان شمالی'),
#         ('3','خراسان جنوبی'),
#         ('4','غیره')
#         )

#     ostan = forms.ChoiceField(widget= forms.Select(attrs={'class':'form-control', 'placeholder':'استان'}), choices=Ostan)
#     City =(
#         ('1','مشهد'),
#         ('2','تربت حیدریه'),
#         ('3','تربت جام'),
#         ('4','کاشمر'),
#         ('5','قوچان')

#         )
#     city = forms.ChoiceField(widget= forms.Select(attrs={'class':'form-control', 'placeholder':'شهرستان'}), choices=City)
#     rosta = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام روستا یا دهستان'}))
#     post_code = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'کدپستی'}))
#     address = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس'}))
#     melk_gps = forms.ImageField(widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'موقعیت جغرافیایی'}))
#     class Meta:
#         model = Melk

#         fields = ['ostan','city','rosta','post_code','address','melk_gps']


class MelkForm(forms.ModelForm):
    melk_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام ملک'}))
    khayer_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام واگذار کننده'}))
    sanad_asli = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سند اصلی'}))
    sanad_farye = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سند فرعی'}))
    CHOICES1 = (
        ('عادی', 'عادی'),
        ('قطعی دفترچه ای', 'قطعی دفترچه ای'),
        ('قطعی غیرمنقول', 'قطعی غیرمنقول'),
        ('صلح نامه', 'صلح نامه'),
        ('وقف نامه', 'وقف نامه'),
        ('ابتیاعی', 'ابتیاعی')
    )
    sanad_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'نوع سند'}),
                                   choices=CHOICES1)
    CHOICES2 = (
        ('آموزشی', 'آموزشی'),
        ('اداری', 'اداری'),
        ('مسکونی', 'مسکونی'),
        ('غیره', 'غیره')

    )

    melk_karbari = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'نوع کاربری ملک'}), choices=CHOICES2)
    CHOICES3 = (
        ('آموزش و پرورش', ' آموزش و پرورش'),
        ('اوقاف', 'اوقاف'),
        ('دولت', 'دولت'),
        ('آستانه', 'آستانه'),
        ('غیره', 'غیره'),

    )
    melk_motavali = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'متولی ملک'}),
                                      choices=CHOICES3)
    CHOICES4 = (
        ('در حال بهره برداری', 'درحال بهره برداری'),
        ('کشاورزی', 'کشاورزی'),
        ('زمین', 'زمین')

    )
    melk_state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'وضعیت ملک'}),
                                   choices=CHOICES4)

    melk_year = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'single-daterange form-control', 'placeholder': 'تاریخ سند'}))
    melk_price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'قیمت ملک'}))
    melk_arseh = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'عرصه ملک'}))
    melk_ayan = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'اعیان ملک'}))
    melk_comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '1', 'placeholder': 'توضیحات سند'}))
    # melk_pic = forms.CharField(widget= forms.FileField(attrs={'class':'form-control', 'placeholder':'تصویر سند'}))
    # Ostan =(
    #     ('خراسان رضوی'),
    #     ('خراسان شمالی'),
    #     ('خراسان جنوبی'),
    #     ('غیره'),

    #     )

    ostan = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'استان'}))
    # City =(
    #     ('1','مشهد'),
    #     ('2','تربت حیدریه'),
    #     ('3','تربت جام'),
    #     ('4','کاشمر'),
    #     ('5','قوچان')

    #     )
    city = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'شهرستان'}))
    rosta = forms.CharField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'نام روستا یا دهستان'}))
    post_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کدپستی'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس'}))
    melk_gps = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موقعیت جغرافیایی'}))

    class Meta:
        model = Melk
        fields = ['melk_name', 'khayer_name', 'sanad_asli', 'sanad_farye', 'sanad_type', 'melk_karbari',
                  'melk_motavali', 'melk_state',
                  'melk_year', 'melk_price', 'melk_arseh', 'melk_ayan', 'melk_comment', 'melk_pic', 'ostan', 'city',
                  'rosta', 'post_code', 'address', 'melk_gps']

# class ItemForm(forms.Form):

#     # here we use a dummy `queryset`, because ModelChoiceField
#     # requires some queryset
#     item_field = forms.ModelChoiceField(queryset=Ostan.objects.none())

#     def __init__(self, item_id):
#         super(ItemForm, self).__init__()
#         self.fields['item_field'].queryset = Ostan.objects.filter(id=item_id)    
# def __init__(self, world, *args, **kwargs):
#     super(MelkForm, self).__init__(*args, **kwargs)
#     query = Ostan.objects.filter(controller=world).exclude(sector="hangar").exclude(sector="warping")
#     choices = []
#     for sfleet in query:
#         choices.append((sfleet.pk, sfleet.name + " - " + sfleet.sector))
#     choices = tuple(choices)
#     self.fields['fleet'] = forms.ChoiceField(choices=choices, label="Select fleet to warp")

# def __init__(self,*args,**kwargs):
#     super().__init__(*args,**kwargs,)
# 	self.fields['city'].queryset=City.object.none()

# 	if 'ostan' in self.data:
# 		try:
# 			ostan=int(self.data.get('Ostan'))
# 			self.fields['city'].queryset=City.objects.filter(ostan=ostan).order_by('ostan')
# 		except(ValueError,TypeError):
# 			pass
# 	elif self.instance.pk:
# 		self.fields['city'].queryset=self.instance.city_set.order_by('city')


# def clean_sanad_asli(self, *args, **kwargs):
#     sanad_asli = self.cleaned_data.get("sanad_asli")
#     if "CFE" in sanad_asli:
#         return sanad_asli
#     else:
#         raise forms.ValidationError("This is not valid title")


# widgets= {
#     'melk_name': forms.TextInput ,
#     'khayer_name' : forms.TextInput,
#     'sanad_asli' : forms.TextInput,
#     'sanad_farye': forms.TextInput ,
#     'sanad_type' : forms.TextInput,
#     'melk_state' : forms.TextInput,
#     'melk_motavali': forms.TextInput ,
#     'melk_karbari' : forms.TextInput,
#     'melk_year' : forms.TextInput,
#     'melk_arseh': forms.TextInput ,
#     'melk_ayan' : forms.TextInput,
#     'melk_pic' : forms.TextInput,
#     'ostan': forms.TextInput ,
#     'city' : forms.TextInput,
#     'rosta' : forms.TextInput,
#     'post_code': forms.TextInput ,
#     'address' : forms.TextInput,
#     'melk_gps' : forms.TextInput,
# }

# class TestForm(forms.ModelForm):
#     class Meta:
#         model = TestModel
#         fields = ('name', 'date', 'date_time')

#     def __init__(self, *args, **kwargs):
#         super(TestForm, self).__init__(*args, **kwargs)
#         self.fields['date'] = JalaliDateField(label=_('date'), # date format is  "yyyy-mm-dd"
#             widget=AdminJalaliDateWidget # optional, to use default datepicker
#         )

#         # you can added a "class" to this field for use your datepicker!
#         # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

#         self.fields['date_time'] = SplitJalaliDateTimeField(label=_('date time'), 
#             widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
#         )
