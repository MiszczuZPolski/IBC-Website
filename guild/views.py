from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import GalleryUploadForm
from .models import GalleryImage


# Create your views here.
def home(request):
    return render(request, 'guild/home.html')

def about(request):
    return render(request, 'guild/about.html')

# Widoki dla kampanii
def campaign_list(request):
    return render(request, 'guild/campaigns/list.html')

def campaign_detail(request, pk):
    return render(request, 'guild/campaigns/detail.html')

# Widoki dla kalendarza
def calendar_view(request):
    return render(request, 'guild/calendar/calendar.html')

# Widoki dla członków
def member_list(request):
    return render(request, 'guild/members/list.html')

@login_required
def profile(request):
    return render(request, 'guild/members/profile.html')

#Widoki dla galerii
def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'guild/gallery/list.html', {'images': images})

@login_required
def gallery_upload(request):
    if request.method == 'POST':
        form = GalleryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = request.user
            image.save()
            return redirect('guild:gallery')
    else:
        form = GalleryUploadForm()
    return render(request, 'guild/gallery/upload.html', {'form': form})

#Widoki dla Easter Egga
def easter_egg(request):
    return render(request, 'guild/easteregg.html')

