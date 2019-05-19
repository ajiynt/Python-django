# Admin Karyawan
# Register your models here.
from django.contrib import admin
from mahasiswa.models import *

# Register your models here.
class JurusanAdmin (admin.ModelAdmin):
    list_display = ['nama', 'keterangan']
    list_filter = ()
    search_fields = ['nama', 'keterangan']
    list_per_page = 25

admin.site.register(Jurusan, JurusanAdmin)


class MahasiswaAdmin (admin.ModelAdmin):
    list_display = ['nim','nama', 'alamat', 'jenis_kelamin', 'jurusan', 'email', 'no_telepon']
    list_filter = ('jenis_kelamin','jurusan')
    search_fields = ['nama', 'alamat', 'email', 'no_telepon']
    list_per_page = 25

admin.site.register(Mahasiswa, MahasiswaAdmin)
