from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

from main.forms import UserLoginForm, UserRegistrationForm, ChannelForm, ContentForm, CommentForm
from .models import Channel, Comment, Content, Interaction, User

# Create your views here.
# this is Home View
def index(request, *args, **kwargs):

    # Get all videos
    videos = Content.objects.all()

    ctx = {'videos': videos}

    return render(request, 'index.html', context=ctx)


# This is view for single videos
def video(request, *args, **kwargs):

    # get Video ID from arguments
    video_id = kwargs['video_id']
    
    # Get the content
    video = Content.objects.get(pk=video_id)

    # get all Videos for side view
    videos = Content.objects.exclude(pk = video_id)


    # Here is the code to handle comments on tha page
    form = CommentForm(request.POST or None)

    if form.is_valid():

        user = request.user
        comment_text = request.POST['info']

        video = Content.objects.get(pk = video_id)

        comment = Comment(content = video, user = user, info=comment_text)

        if 'comment_id' in request.POST:
                comment.reply_ref = Comment(id = request.POST['comment_id'])
        
        comment.save()

        form = CommentForm()

    # set the context variable
    ctx = {'form': form, 'video': video, 'videos':videos}

    return render(request, 'video.html', context=ctx)


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

            # messages.success(request, "Logged In", extra_tags='success')
            return redirect('/'+request.GET.get('next', ''))
        else:

            # Add message for failure
            messages.warning(request, 'Invalid Credentials', extra_tags='danger')

            return redirect('/login?next={0}'.format(request.GET.get('next', '')))

    return render(request, 'login.html', {'form': form})


# Logout View
def signout(request, *args, **kwargs):

    # Log out
    if request.user.is_authenticated:
        logout(request)

    return redirect('login')


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

    
    # Set the context Manager
    ctx = {'form': form}

    return render(request, 'createChannel.html', context=ctx)


# This is Channel View
@login_required(login_url='login')
def channel_view(request, *args, **kwargs):
    pass


# Upload Content View is here
@login_required(login_url='login')
def uploadContent(request, *args, **kwargs):

    # If user doesn't have a channel return Then first Create One
    if request.user.channel_set.count() < 1:
        messages.warning(request, "Create A Channel First", extra_tags='warning')

        return redirect('createChannel')


    form = ContentForm(request.POST or None, request.FILES or None)

    # check if form is a valid form
    if form.is_valid():

        user = request.user                  # Get the active user
        channel = user.channel_set.first()   # Get its channel

        # If user has no channel then Go and create a channel first
        if not channel:
            return redirect('createChannel')
        else:
            title = form.cleaned_data['title']
            media = form.cleaned_data['media']
            description = form.cleaned_data['description']
            

            Content.objects.create(title=title, media=media, description=description, channel=channel)

            # add a success message
            messages.success(request, 'Video uploaded', extra_tags='success')

            return redirect('upload')


    ctx = {'form': form}
    
    return render(request, 'upload.html', context=ctx)


# View to Store interaction in databse
@login_required(login_url='login')
def feed_interaction(request, *args, **kwargs):

    if request.method == 'GET':

        print(request.GET)

        video_id = request.GET.get('video')
        type_interaction = request.GET.get('type')

        video = Content.objects.get(pk=video_id)
        
            
        interaction, created = Interaction.objects.get_or_create(user = request.user, content = video)
        interaction.type = type_interaction
        interaction.save()


    return JsonResponse('Success', safe=False)


def interaction_status(request, *args, **kwargs):
    
    # if request.method == 'GET':

    video_id = int(request.GET['video_id'])
    
    like = Content.objects.get(pk = video_id).interaction_set.filter(type='like').count()
    dislike = Content.objects.get(pk = video_id).interaction_set.filter(type='dislike').count()
    watch = Content.objects.get(pk = video_id).interaction_set.filter(type='watch').count()
    

    return JsonResponse({'like': like, 'dislike': dislike, 'watch':watch})


# View to handle comments
# @login_required(login_url='login')
# def comments(request, *args, **kwargs):

#     form = CommentForm(request.POST or None)

#     if form.is_valid():

#         video_id = request.POST['video_id']
#         user = request.user
#         comment_text = request.POST['info']

#         video = Content.objects.get(pk = video_id)

#         comment = Comment(content = video, user = user, info=comment_text)

#         if 'comment_id' in request.POST:
#                 comment.reply_ref = request.POST['comment_id']
        
#         comment.save()
    
#     # all_comments = [{
#     #                 'comment': comment,
#     #                 'replyies': [{
#     #                                 'comment': nested_comment
#     #                              } for nested_comment in comment.comment_set.all()
#     #                             ]
#     #                  } for comment in Comment.objects.all()
#     #                 ]

#     ctx = {'form': form}

#     return render()