from main.forms import UserLoginForm
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request, *args, **kwargs):

    return render(request, 'index.html', {})


# Login Vies is here
def login_view(request, *args, **kwargs):

    form = UserLoginForm(request.POST or None)

    # If form is Valid
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', ''))
        else:

            # Add message for failure
            messages.success(request, 'Invalid Credentials', extra_tags='danger')

            return redirect('/login?next={0}'.format(request.GET.get('next', '')))

    return render(request, 'login.html', {'form': form})
        


