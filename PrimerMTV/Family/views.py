from django.shortcuts import render
from django.http import HttpResponse

from Family.models import family

def add_member(request):
    new_member = family.objects.create(name = 'Ines', DNI = 20451898, use_glases = True)
    print(new_member)
    return HttpResponse('Se añadió un familiar a la lista')

def list_members(request):
    all_members = family.objects.all()
    print(all_members)
    context = {
        'family':all_members,
    }
    return render(request, 'list_members.html', context=context)
