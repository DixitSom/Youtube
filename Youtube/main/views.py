from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from main.forms import UserLoginForm, UserRegistrationForm
from .models import User

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
            messages.warning(request, 'Invalid Credentials', extra_tags='danger')

            return redirect('/login?next={0}'.format(request.GET.get('next', '')))

    return render(request, 'login.html', {'form': form})



# Sign Up view is here
def signUp(request, *args, **kwargs):
    
    # context
    ctx = {}

    form = UserRegistrationForm(request.POST or None)

    # If form data is valid
    if form.is_valid():

        email = form.cleaned_data.get('email')

        # if email already registered
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already in Use", extra_tags='danger')

        else:
            form.save()

            return redirect('login')

    # add form to context
    ctx['form'] = form

    return render(request, 'register.html', context=ctx)