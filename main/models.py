from tkinter import CASCADE
from django.db import models

class klub(models.Model):
    kode_klub = models.AutoField(primary_key=True)
    nama_klub = models.CharField(max_length=100)
    base = models.CharField(max_length=255)
    logo_klub = models.CharField(max_length=255)
    status_klub = models.CharField(max_length=255)

class player(models.Model):
    kode_pemain = models.AutoField(primary_key=True)
    nama_pemain = models.CharField(max_length=70)
    tgl_lahir = models.DateField()
    foto = models.CharField(max_length=255)
    no_punggung = models.CharField(max_length=2)
    posisi = models.CharField(max_length=30)
    kode_klub = models.ForeignKey(klub, on_delete=models.CASCADE, related_name="kode_klub+")

class liga(models.Model):
    kode_liga = models.AutoField(primary_key=True)
    nama_liga = models.CharField(max_length=100)
    negara = models.CharField(max_length=50)

class matchday(models.Model):
    kode_match = models.AutoField(primary_key=True)
    home_team = models.ForeignKey(klub, on_delete=models.CASCADE, related_name="kode_klub+")
    away_team = models.ForeignKey(klub, on_delete=models.CASCADE, related_name="kode_klub+")
    home_score = models.SmallIntegerField()
    away_score = models.SmallIntegerField()
    winner = models.ForeignKey(klub, on_delete=models.CASCADE, related_name="kode_klub+")
    tgl_pertandingan = models.DateField()
    status = models.CharField(max_length=255)
    kode_liga = models.ForeignKey(liga, on_delete=models.CASCADE, related_name="kode_liga+")

