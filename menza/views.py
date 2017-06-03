from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UploadForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from .models import Photo

@login_required
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            form.save()
            return redirect('menza:list')

    form = UploadForm
    return render(request, 'menza/upload.html', {'form':form})

@login_required
def edit(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            form.save()
            return redirect('menza:list', id=photo.id)
    else:
        form = UploadForm(instance=photo)
    return render(request, 'menza/upload.html', {'form': form})

class ContentCreate(CreateView):
    model = Photo
    fields = ['image' , 'thumnail_image' , 'room_phone' , 'room_name' , 'room_monthly' , 'comment']
    success_url = reverse_lazy('menza:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookCreate, self).form_valid(form)

class MyListView(ListView):
    template_name = 'menza/my_list.html'
    context_object_name = 'user_photo_list'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return user.photo_set.all().order_by('-upload_date')

class ContentList(ListView):
    model = Photo
    template_name = 'menza/list.html'
    paginate_by = 6

class ContentDetail(DetailView):
    model = Photo
    template_name = 'menza/detail.html'


class ContentUpdate(UpdateView):
    template_name = 'menza/upload.html'
    model = Photo
    success_url = reverse_lazy('menza:list')

class ContentDelete(DeleteView):
    model = Photo
    template_name = 'menza/delete.html'
    success_url = reverse_lazy('menza:list')
