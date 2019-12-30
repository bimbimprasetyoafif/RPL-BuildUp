from django.contrib import admin
from .models import (
    RAB, 
    Design, 
    DesignImages, 
    MaterialAtap, 
    MaterialCatDalam, 
    MaterialCatLuar, 
    MaterialDinding,
    MaterialLantai,
    MaterialPlafon,
)
# Register your models here.
admin.site.register(RAB)
admin.site.register(Design)
admin.site.register(DesignImages)
admin.site.register(MaterialAtap)
admin.site.register(MaterialCatDalam)
admin.site.register(MaterialCatLuar)
admin.site.register(MaterialDinding)
admin.site.register(MaterialLantai)
admin.site.register(MaterialPlafon)
