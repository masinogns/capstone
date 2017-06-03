from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from .forms import UploadForm
from django.contrib.auth.decorators import login_required
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

class IndexView(ListView):
    template_name = 'menza/index.html'
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
    #
    # def get_queryset(self):
    #     return Photo.objects.all().order_by('-upload_date')
