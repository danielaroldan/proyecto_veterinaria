from django.contrib import admin
from .models import Cliente
from .models import Venta
from .models import Factura
from .models import Articulo
from .models import StockArticulo

# Register your models here.
admin.site.register (Cliente)
admin.site.register(Venta)
admin.site.register(Factura)
admin.site.register(Articulo)
admin.site.register(StockArticulo)