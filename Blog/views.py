from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from .models import Post, Contact


def index(request):
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'blog/index.html', {'posts': posts})


def read(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    return render(request, 'blog/read.html', {'post': post})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return redirect(reverse('contact') + '?success=1')

    success = request.GET.get('success') == '1'
    if request.user.is_authenticated:
        full_name = f"{request.user.first_name} {request.user.last_name}"
        email = request.user.email
    else:
        full_name = ''
        email = ''
    return render(request, 'blog/contact.html', {'full_name': full_name, 'email': email, 'success': success})


@login_required
def addpost(request):
    if request.method == "POST":
        post_title = request.POST.get('post_title', '')
        category = request.POST.get('category', '')
        content = request.POST.get('content', '')
        image = request.FILES.get('image')

        post = Post(
            post_title=post_title,
            author=request.user,  # Securely assign current user
            category=category,
            content=content,
            image=image
        )
        post.save()

        request.session['can_view_success'] = True
        return redirect('blog_submission_success')

    return render(request, 'blog/addpost.html', {'username': request.user.username})


def submission_success(request):
    if not request.session.get('can_view_success'):
        return redirect('addPost')
    del request.session['can_view_success']
    return render(request, 'blog/message.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'blog/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'blog/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'blog/signup.html')

        try:
            myuser = User.objects.create_user(username=username, email=email, password=pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return render(request, 'blog/signup.html')

    return render(request, 'blog/signup.html')


def loginuser(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            return redirect('blogHome')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

    return render(request, 'blog/login.html')


def logoutuser(request):
    logout(request)
    return redirect('blogHome')


@login_required
def profile(request):
    user = request.user
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'last_login': user.last_login,
    }
    return render(request, 'blog/profile.html', context)


@login_required
def mypost(request):
    posts = Post.objects.filter(author=request.user).order_by('-timestamp')
    return render(request, 'blog/mypost.html', {'posts': posts})


def designedanddeveloped(request):
    return render(request, 'blog/designed-and-developed.html')


@login_required
@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)

    # Security check
    if post.author != request.user and not request.user.is_superuser:
        return JsonResponse({'status': 'error', 'message': 'Unauthorized action'}, status=403)

    post_title = post.post_title
    post.delete()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'message': f'Post "{post_title}" deleted successfully'})

    messages.success(request, f'Post "{post_title}" deleted successfully')
    return redirect('blogHome')


@login_required
@require_POST
def delete_user_with_csrf(request, username):
    user = get_object_or_404(User, username=username)

    if request.user != user:
        return JsonResponse({'status': 'error', 'message': 'You can only delete your own account'}, status=403)

    username = user.username
    user.delete()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'message': f'Account "{username}" deleted successfully'})

    messages.success(request, f'Account "{username}" deleted successfully')
    return redirect('blogHome')
