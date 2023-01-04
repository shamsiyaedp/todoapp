from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Task
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class TaskListview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='b'

class TaskDetailview(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='a'

class TaskUpdateview(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='a'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy('cbvhome')



def home(request):
    b=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        a=Task(name=name,priority=priority,date=date)
        a.save();  
    return render (request,'home.html',{'b':b})

def delete(request,id):
    if request.method=='POST':
        c=Task.objects.get(id=id)
        c.delete();
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    m=Task.objects.get(id=id)
    form=TodoForm(request.POST or None,request.FILES,instance=m)
    if form.is_valid():
        form.save();
        return redirect('/')
    return render(request,'update.html',{'m':m,'form':form})

