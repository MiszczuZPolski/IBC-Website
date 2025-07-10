from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth import login,authenticate
from .models import GalleryImage
from .forms import LoginForm, GalleryUploadForm
from datetime import datetime, timedelta
from calendar import monthcalendar
from django.utils import timezone


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
    members = Member.objects.all()
    return render(request, 'guild/members/list.html', {'members': members})

@login_required
def profile(request):
    member = get_object_or_404(Member, user=request.user)
    return render(request, 'guild/members/profile.html', {'member': member})

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

