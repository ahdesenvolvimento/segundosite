from django.urls import path
from .views import index, contato, produto,ops
urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto', produto, name='produto'),
    path('ops', ops, name='ops'),
]