from django.shortcuts import render,redirect
from.models import *
from.forms import  *
# Create your views here.
def index(request):
    tas=task.objects.all()
    form=taskform()
    if request.POST:
        form=taskform(request.POST)
        if form.is_valid():
            form.save()
        # return redirect('/')

    context={'tas':tas,'form':form}
    return render(request,'index.html',context)



def updatetask(request,pk):
    t=task.objects.get(id=pk)
    form=taskform(instance=t)
    if request.POST:
        form=taskform(request.POST,instance=t)
        form.is_valid()
        form.save()
        return redirect('/')
    context={'form':form}
    return render (request,'update.html',context)


def deletetask(request,pk):
    item=task.objects.get(id=pk)
    if request.POST:
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request,'delete.html',context)