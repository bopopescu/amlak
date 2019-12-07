import datetime
import django.db
from django.utils import timezone
from django.urls import reverse



class Ostan(django.db.models.Model):
    name = django.db.models.CharField(max_length=20, verbose_name="استان")

    def __str__(self):
        return self.name

class City(django.db.models.Model):
    ostan = django.db.models.ForeignKey(Ostan, on_delete=django.db.models.CASCADE, verbose_name ='شهرستان')
    name = django.db.models.CharField(max_length=50)
           
    def __str__(self):
        return self.name

class Rosta(django.db.models.Model):
    city = django.db.models.ForeignKey(City, on_delete=django.db.models.CASCADE)
    name = django.db.models.CharField(max_length=50, verbose_name="روستا")

    def __str__(self):
        return self.name


class Unit(django.db.models.Model):
    u_code = django.db.models.CharField(max_length=40, verbose_name="کد منطقه")
    u_name = django.db.models.CharField(max_length=50, verbose_name="نام منطقه")
    def __str__(self):
        return self.u_name
    def get_absolute_url(self):
        return reverse("core:unit_create", kwargs={})
        #return reverse("core:unit_update", kwargs={"id": self.id})

class Melk(django.db.models.Model):
    melk_name = django.db.models.CharField(max_length=100, verbose_name="نام ملک")
    khayer_name = django.db.models.CharField(max_length=100, verbose_name="نام واگذارکننده")
    sanad_asli = django.db.models.CharField(max_length=20, verbose_name="شماره سند اصلی")
    sanad_farye = django.db.models.CharField(max_length=20, verbose_name="شماره سند فرعی")
    CHOICES1 =(
            ('عادی','عادی'),
            ('قطعی دفترچه ای','قطعی دفترچه ای'),
            ('قطعی غیرمنقول','قطعی غیرمنقول'),
            ('صلح نامه','صلح نامه'),
            ('وقف نامه','وقف نامه'),
            ('ابتیاعی','ابتیاعی')
            )
    sanad_type = django.db.models.CharField(choices=CHOICES1, max_length=50, verbose_name="نوع سند واگذاری")
    melk_state = django.db.models.CharField(max_length=50, verbose_name="وضعیت کنونی ملک")
    melk_motavali = django.db.models.CharField(max_length=100, verbose_name="متولی ملک")
    melk_karbari = django.db.models.CharField(max_length=50, verbose_name="نوع کاربری ملک")
    melk_year = django.db.models.DateField(verbose_name="سال واگذاری ملک")
    melk_arseh = django.db.models.CharField(max_length=20, verbose_name="عرصه ملک")
    melk_price = django.db.models.CharField(max_length=50, verbose_name="ارزش ریالی ملک")
    melk_ayan = django.db.models.CharField(max_length=20, verbose_name="اعیان ملک")
    melk_comment = django.db.models.CharField(max_length=1000, verbose_name="توضیحات سند ملک")
    melk_pic = django.db.models.FileField(blank=True, null=True, verbose_name="تصویر سند ملک")
    ostan = django.db.models.ForeignKey(Ostan, on_delete=django.db.models.CASCADE, verbose_name="استان")
    city = django.db.models.ForeignKey(City, on_delete=django.db.models.CASCADE, verbose_name="شهرستان")
    rosta = django.db.models.ForeignKey(Rosta, on_delete=django.db.models.CASCADE, verbose_name="روستا")
    post_code = django.db.models.CharField(max_length=10, verbose_name="کدپستی")
    address = django.db.models.CharField(max_length=200, verbose_name="آدرس ملک")
    melk_gps = django.db.models.CharField(max_length=100, verbose_name="موقعیت جغرافیایی ملک")
    def __str__(self):
        return self.melk_name
    
    def get_absolute_url(self):
        return reverse("core:melk_insert", kwargs={})
    
    
