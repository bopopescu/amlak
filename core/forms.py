
from rtl import rtl
import datetime
import jdatetime
from django import forms
import django_jalali.admin as jadmin
# from django_jalali.db import models as jmodels
#from djmoney.forms import MoneyField
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Melk, Unit, Ostan, City
from ckeditor.widgets import CKEditorWidget
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from location_field.forms.plain import PlainLocationField
# from django.contrib.gis.geos import fromstr
# from django.contrib.gis.db.models.functions import Distance

User = get_user_model()


class SearchForm( forms.Form ):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-sm rounded bright', 'placeholder': 'جستجو1','autocomplete': 'off'} ) )


class UserLoginForm( forms.Form ):
    username = forms.CharField( max_length=100,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد نمایید','autocomplete': 'off'} ) )
    password = forms.CharField(
        widget=forms.PasswordInput( attrs={'class': 'form-control', 'placeholder': 'کلمه عبور خود را وارد نمایید','autocomplete': 'off'} ) )

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
        widget=forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'نام کاربری ','autocomplete': 'off'} ) )
    email = forms.EmailField(
        widget=forms.EmailInput( attrs={'class': 'form-control', 'placeholder': 'پست الکترونیک','autocomplete': 'off'} ) )
    password = forms.CharField(
        widget=forms.PasswordInput( attrs={'class': 'form-control', 'placeholder': 'کلمه عبور','autocomplete': 'off'} ) )
    password2 = forms.CharField(
        widget=forms.PasswordInput( attrs={'class': 'form-control', 'placeholder': 'تکرار کلمه عبور','autocomplete': 'off'} ) )

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
    u_code = forms.CharField( widget=forms.NumberInput( attrs={'class': 'form-control', 'placeholder': 'کد منطقه','autocomplete': 'off'} ) )
    u_name = forms.CharField( widget=forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'نام منطقه','autocomplete': 'off'} ) )

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
                'melk_name': forms.TextInput( attrs={'class':'form-control','autocomplete': 'off'} ),
                'khayer_name' : forms.TextInput( attrs={'class':'form-control','autocomplete': 'off'} ),
                'sanad_asli' : forms.NumberInput( attrs={'class':'form-control','autocomplete': 'off'} ),
                'sanad_farye': forms.NumberInput( attrs={'class':'form-control','autocomplete': 'off'} ),
                'sanad_type' : forms.Select( attrs={'class':'form-control'} ),
                'melk_state' : forms.Select( attrs={'class':'form-control'} ),
                'melk_motavali': forms.Select( attrs={'class':'form-control'} ),
                'melk_karbari' : forms.Select( attrs={'class':'form-control'} ),
                # 'melk_year': forms.TextInput( attrs={'class':'form-control'} ),
                # 'melk_year' : jmodels.jDateField(verbose_name=None, name=None, 
                # #     attrs={'class':' vjDateField hasDatepicker form-control','type': 'date',
                # # 'data-provide': 'datepicker',
                # # 'data-date-format': 'yyyy-mm-dd',
                #  ),
                'melk_arseh': forms.TextInput( attrs={'class':'money form-control','autocomplete': 'off'} ),
                'melk_ayan' : forms.TextInput( attrs={'class':'money form-control','autocomplete': 'off'} ),
                'melk_price' : forms.TextInput( attrs={'class':'money form-control','autocomplete': 'off'} ),
                'melk_comment' : forms.Textarea( attrs={'class':'form-control'} ),
                'melk_pic' : forms.FileInput( attrs={'class':'form-control'} ),
                'ostan': forms.Select( attrs={'class':'form-control'}),
                'city' : forms.Select( attrs={'class':'form-control'}),
                'rosta' : forms.TextInput( attrs={'class':'form-control','autocomplete': 'off'} ),
                'post_code': forms.NumberInput( attrs={'class':'form-control','autocomplete': 'off'} ),
                'address' : forms.TextInput( attrs={'class':'form-control','autocomplete': 'off'} ),
                'melk_gps' : forms.TextInput( attrs={'class':'form-control','autocomplete': 'off'} ),
                'latitude' : forms.TextInput( attrs={'class':'form-control','autocomplete': 'off'} ),
                'longitude' : forms.TextInput( attrs={'class':'form-control','autocomplete': 'off'} ),

                
            }

        # labels = {
        #     'name': 'Full name',
        #     'comment': 'Issue'
        # }
        # help_texts = {
        #     'comment': 'Provide a detailed account of the issue to receive a quick answer'
        # }
        # error_messages = {
        #     'name': {
        #     'max_length': "Name can only be 25 characters in length"
        #     }
        # }
        # field_classes = {
        #     'email': EmailCoffeehouseFormField
        # },
        # localized_fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(MelkForm, self).__init__(*args, **kwargs)
            self.fields['melk_year'] = JalaliDateField(label=_('melk_year'), # date format is  "yyyy-mm-dd"
                widget= AdminJalaliDateWidget # optional, to use default datepicker
            )
            self.fields['melk_year'].widget.attrs.update({'class': 'jalali_date-date form-control','autocomplete': 'off'})

            # you can added a "class" to this field for use your datepicker!
            # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

            # self.fields['date_time'] = SplitJalaliDateTimeField(label=_('date time'), 
            #     widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
            # )
    