
from rtl import rtl
from django import forms
import django_jalali.admin as jadmin


from django.contrib.auth import (
    authenticate,
    get_user_model
)
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Melk, Unit, Ostan, City, Rosta
from ckeditor.widgets import CKEditorWidget

User = get_user_model()


class SearchForm( forms.Form ):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-sm rounded bright', 'placeholder': 'جستجو1'} ) )


class UserLoginForm( forms.Form ):
    username = forms.CharField( max_length=100,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد نمایید'} ) )
    password = forms.CharField(
        widget=forms.PasswordInput( attrs={'class': 'form-control', 'placeholder': 'کلمه عبور خود را وارد نمایید'} ) )

    def clean_username(self):
        data = self.cleaned_data['username']
        # password = self.cleaned_data('password')

        if data != User.username():
            user = authenticate( username=data )
            if not user:
                raise ValidationError( _( 'نام کاربری وجود ندارد' ) )
            # if not user.check_password(password):
            #     raise forms.ValidationError('کلمه عبور اشتباه است')
            if not user.is_active:
                raise ValidationError( _( 'کاربر فعال نیست' ) )
            # return super(UserLoginForm, self).clean(*args, **kwargs)
            return data


class UserRegisterForm( forms.ModelForm ):
    username = forms.CharField(
        widget=forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'نام کاربری '} ) )
    email = forms.EmailField(
        widget=forms.EmailInput( attrs={'class': 'form-control', 'placeholder': 'پست الکترونیک'} ) )
    password = forms.CharField(
        widget=forms.PasswordInput( attrs={'class': 'form-control', 'placeholder': 'کلمه عبور'} ) )
    password2 = forms.CharField(
        widget=forms.PasswordInput( attrs={'class': 'form-control', 'placeholder': 'تکرار کلمه عبور'} ) )

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
        return super( UserRegisterForm, self ).clean( *args, **kwargs )


class UnitForm( forms.ModelForm ):
    u_code = forms.CharField( widget=forms.NumberInput( attrs={'class': 'form-control', 'placeholder': 'کد منطقه'} ) )
    u_name = forms.CharField( widget=forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'نام منطقه'} ) )

    class Meta:
        model = Unit
        fields = ['u_code', 'u_name']

    def clean_ucode(self, *args, **kwargs):
        u_code = self.cleaned_data.get( "u_code" )
        if "CFE" in u_code:
            return u_code
        else:
            raise forms.ValidationError( "This is not valid title" )

class MelkForm( forms.ModelForm ):

    class Meta:
        model = Melk
        fields = '__all__'
        widgets = {
                'melk_name': forms.TextInput( attrs={'class':'form-control'} ),
                'khayer_name' : forms.TextInput( attrs={'class':'form-control'} ),
                'sanad_asli' : forms.NumberInput( attrs={'class':'form-control'} ),
                'sanad_farye': forms.NumberInput( attrs={'class':'form-control'} ),
                'sanad_type' : forms.Select( attrs={'class':'form-control'} ),
                'melk_state' : forms.Select( attrs={'class':'form-control'} ),
                'melk_motavali': forms.Select( attrs={'class':'form-control'} ),
                'melk_karbari' : forms.Select( attrs={'class':'form-control'} ),
                'melk_year' : forms.DateInput( format=('%d-%m-%Y'), 
                    attrs={'class':'date-input form-control','type': 'date',
                'data-provide': 'datepicker',
                'data-date-format': 'yyyy-mm-dd',
                } ),
                'melk_arseh': forms.NumberInput( attrs={'class':'form-control'} ),
                'melk_ayan' : forms.NumberInput( attrs={'class':'form-control'} ),
                'melk_price' : forms.TextInput( attrs={'class': 'form-control'} ),
                'melk_comment' : forms.Textarea( attrs={'class':'form-control'} ),
                'melk_pic' : forms.FileInput( attrs={'class':'form-control'} ),
                'ostan': forms.Select( attrs={'class':'form-control'} ),
                'city' : forms.Select( attrs={'class':'form-control'} ),
                'rosta' : forms.Select( attrs={'class':'form-control'} ),
                'post_code': forms.NumberInput( attrs={'class':'form-control'} ),
                'address' : forms.TextInput( attrs={'class':'form-control'} ),
                'melk_gps' : forms.TextInput( attrs={'class':'form-control'} ),
        }


    # def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.fields['ostan'].queryset = Ostan.objects.all()
    #         self.fields['city'].queryset = City.objects.filter(ostan_id = Ostan.id()).order_by('name')
    #         self.fields['rosta'].queryset = Rosta.objects.all()