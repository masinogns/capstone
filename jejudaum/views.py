from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Room_info

class IndexView(TemplateView):
    template_name = 'jejudaum/index.html'

class RoomList(ListView):
    model = Room_info
    paginate_by = 10
    template_name = 'jejudaum/room_list.html'

class RoomDetail(DetailView):
    model = Room_info
    template_name = 'jejudaum/room_detail.html'

class RoomCreate(CreateView):
    template_name = 'jejudaum/room_new.html'
    model = Room_info
    fields = ['title', 'content']
    success_url = reverse_lazy('jejudaum:room_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(RoomCreate, self).form_valid(form)

class RoomChangeList(ListView):
    template_name = 'jejudaum/room_change_list.html'

    def get_queryset(self):
        return Room_info.objects.filter(owner = self.request.user)

class RoomUpdate(UpdateView):
    template_name = 'jejudaum/room_new.html'
    model = Room_info
    fields = ['title', 'content']
    success_url = reverse_lazy('jejudaum:room_list')

class RoomDelete(DeleteView):
    model = Room_info
    template_name = 'jejudaum/room_delete.html'
    success_url = reverse_lazy('jejudaum:room_list')
