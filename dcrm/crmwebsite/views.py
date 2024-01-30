from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username, password)

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("home")
        else:
            messages.success(request, "There was an error logging you in")
            return redirect("home")
    else:
        return render(request, "home.html", {"records": records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        print("post request")
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            print("form is valid")
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})
    return render(request, "register.html", {"form": form})


def user_record(request, pk):
    if request.user.is_authenticated:
        user_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"user_record": user_record})
    else:
        messages.success(request, "You need to login first")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        user_record = Record.objects.get(id=pk)
        user_record.delete()
        messages.success(request, "Record deleted")
        return redirect("home")
    else:
        messages.success(request, "You need to login first")
        return redirect("home")


def update_record(request, pk):
    pass


def add_record(request):
    pass
