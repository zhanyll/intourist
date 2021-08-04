from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

def homepage(request):
    return render(request, 'core/index.html')

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'core/index.html')

class HomeView(TemplateView):
    template_name = 'core/index.html'

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile_object = user.profile
        return render(request, 'core/profile.html', {'profile': profile_object})
    else:
        return redirect('homepage')