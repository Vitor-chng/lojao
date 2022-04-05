from django.contrib import admin
from .models import Venda
from .models import Produto

admin.site.register(Produto)
admin.site.register(Venda)
# Register your models here.
