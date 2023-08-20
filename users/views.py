from django.shortcuts import render

from users.forms import UserLoginForm, UserRegistrationForm


# Create your views here.

def login(request):
    if request.method == "POST":
        pass
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, "login.html", context)
