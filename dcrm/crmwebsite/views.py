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
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        record = Record.objects.get(id=pk)
        record.first_name = first_name
        record.last_name = last_name
        record.email = email
        record.phone = phone
        record.address = address
        record.city = city
        record.state = state
        record.save()
        messages.success(request, "Record updated")
        return redirect("home")
    else:
        record = Record.objects.get(id=pk)
        return render(request, "update_record.html", {"record": record})


def add_record(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        record = Record.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
        )
        record.save()
        messages.success(request, "Record added")
        return redirect("home")
    return render(request, "add_record.html")
