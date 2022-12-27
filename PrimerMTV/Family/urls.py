from django.urls import path

from Family.views import add_member, list_members


urlpatterns = [
    path('añadir/', add_member),
    path('listar/', list_members),
]