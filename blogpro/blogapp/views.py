from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, redirect


def fun1(request):
    return HttpResponse("hello")

def nav(request):
    return render(request,'nav.html')
    

from django.views.generic import ListView
class Tasklistview(ListView):
    model = blogmodel
    template_name = 'list.html'
    context_object_name = 'dict_list'
    ordering = ['-publication_date']


from django.views.generic.detail import DetailView
class Taskdetialview(DetailView):
    model= blogmodel
    template_name = 'blog_detail.html' 
    context_object_name = 'dict_detail'

from django.views.generic.edit import CreateView
class Taskcreateview(CreateView):
    model = blogmodel
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('list')

from django.views.generic.edit import UpdateView
class Taskupdateview(UpdateView):
    model = blogmodel
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('list')
    from django.urls import reverse
from django.views.generic.edit import UpdateView

class Taskupdateview(UpdateView):
    model = blogmodel
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('list')



from django.views.generic.edit import DeleteView
class Taskdeleteview(DeleteView):
    model = blogmodel
    template_name = 'delete.html'
    context_object_name = 'dict_detail'  # Corrected to match your naming preference
    success_url = reverse_lazy('list')

