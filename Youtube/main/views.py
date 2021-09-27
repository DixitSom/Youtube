from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

from main.forms import UserLoginForm, UserRegistrationForm, ChannelForm
from .models import Channel, User

# Create your views here.
def index(request, *args, **kwargs):

    return render(request, 'index.html', {})


# Login Vies is here
def login_view(request, *args, **kwargs):

    # Custome Authentication Function

    def custom_authenticate(**kwargs):

        email = kwargs['email']
        password = kwargs['password']

        user_inner = User.objects.filter(email = email).first()

        # If password matches
        if user_inner is not None and check_password(password, user_inner.password):
            return user_inner
        
        return None
    

    form = UserLoginForm(request.POST or None)

    # If form is Valid
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = custom_authenticate(email = email, password = password)

        if user is not None:
            login(request, user)

            messages.success(request, "Logged In", extra_tags='success')
            return redirect('/'+request.GET.get('next', ''))
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

            # Create User in database
            user = User(**form.cleaned_data)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            messages.success(request, 'Account Created Succesfully', extra_tags='success')

            return redirect('login')

    # add form to context
    ctx['form'] = form

    return render(request, 'register.html', context=ctx)


# Create Channel View is here
@login_required(login_url='login')
def createChannel(request, *args, **kwargs):

    form = ChannelForm(request.POST or None)

    # If form is valid
    if form.is_valid():

        channel_name = form.cleaned_data['name']          # get the name of channel
        description = form.cleaned_data['description']    # Description of the chanel
        user = request.user                               # user of Channel

        # Create Channel and save it
        Channel.objects.create(name= channel_name, description=description, user=user)

        messages.success(request, "Channel Created", 'success')
    else:
        messages.warning(request, 'Something is wrong here', 'warning')

    ctx = {'form': form}

    return render(request, 'createChannel.html', context=ctx)


@login_required(login_url='login')
def channel_view(request, *args, **kwargs):
    pass
