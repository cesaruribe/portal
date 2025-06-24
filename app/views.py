from django.shortcuts import render,redirect
from app.models import Actores
from app.forms  import ActoresForm

# Create your views here.
def inicio(request):
    return render(request,'home.html',{})

def menu(request):
    return render(request,'menu.html',{})

def actorShow(request):
    actor = Actores.objects.all()
    return render(request,'actoresShow.html',{'actor':actor})

def actorNew(request):
    if request.method == 'POST':
        form = ActoresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showactor')
    else:
        form = ActoresForm
    return render(request,'actoresNew.html',{'form':form})

def actorEdit(request, actorid):
    actor = Actores.objects.get(actorid=actorid)
    return render(request,'actoresEdit.html',{'actor':actor})

def actorUpdate(request,actorid):
    actor = Actores.objects.get(actorid=actorid)
    form = ActoresForm(request.POST,instance=actor)
    print(form)
    print(form.errors)
    if form.is_valid():
        form.save()
        return redirect("/showactor")
    return render(request,'actorEdit.html',{'actor':actor})

def actorDestroy(request,actorid):
    actor=Actores.objects.get(actorid=actorid)
    actor.delete()
    return redirect("/showactor")
