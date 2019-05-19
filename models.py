# Model karyawan
# Create your models here.
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jurusan (models.Model):
    nama = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return self.nama

class Mahasiswa (models.Model):
    JENIS_KELAMIN_CHOICES = (
        ('pria', 'Pria'),
        ('wanita', 'Wanita'),
    )


    nim = models.CharField (max_length=30, blank=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField(blank=True)
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN_CHOICES)
    no_telepon = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama