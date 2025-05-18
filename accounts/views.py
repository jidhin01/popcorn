from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def sign_in(request):
    if request.method == 'POST':
        if 'signup' in request.POST:  # If Sign Up form is submitted
            sign_up_name = request.POST.get('sign_up_name', '')  # Use .get() to avoid KeyError
            sign_up_email = request.POST.get('sign_up_email', '')
            sign_up_passwd = request.POST.get('sign_up_passwd', '')

            if User.objects.filter(username=sign_up_name).exists():
                messages.error(request, ' ')
            else:
                user = User.objects.create_user(username=sign_up_name, email=sign_up_email, password=sign_up_passwd)
                user.save()
                messages.success(request, ' ')

        elif 'signin' in request.POST:  # If Sign In form is submitted
            sign_in_username = request.POST.get('sign_in_username', '')  # Use .get()
            sign_in_passwd = request.POST.get('sign_in_passwd', '')

            user = auth.authenticate(username=sign_in_username, password=sign_in_passwd)

            if user is not None:
                # Log the user in
                auth.login(request, user)

                # Check if the user is an admin (superuser)
                if user.is_superuser:
                    return redirect('adminindex')  # Redirect to adminindex page for admin users
                else:
                    return redirect('/')  # Redirect to home page for regular users
            else:
                # If authentication fails, show an error message
                messages.error(request, ' ')

    return render(request, 'sign_in.html')


def logout_view(request):
    auth.logout(request)
    return redirect('/')
