from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import Sign_up
# Create your views here.
def signup(request):
    if request.method == "POST":
        fm = Sign_up(request.POST)
        if fm.is_valid():
            fm.save()
    else:

        fm = Sign_up()
    return render(request, 'enroll/signup.html', {'form':fm})