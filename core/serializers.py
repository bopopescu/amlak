
from rest_framework import serializers


class MelkSerializer(serializers.Serializer):
    melk_name = serializers.CharField(max_length=100, verbose_name="نام ملک")
    khayer_name = serializers.CharField(max_length=100, verbose_name="نام واگذارکننده")
    sanad_asli = serializers.CharField(max_length=20, verbose_name="شماره سند اصلی")
    sanad_farye = serializers.CharField(max_length=20, verbose_name="شماره سند فرعی")
    # class Meta:
    #     model = Melk
    #     fields = ['url', 'username', 'email', 'groups']


