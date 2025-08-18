from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def sign_in(request):
    if request.method == 'POST':
        # ------------------- SIGN UP -------------------
        if 'signup' in request.POST:
            sign_up_name = request.POST.get('sign_up_name', '').strip()
            sign_up_email = request.POST.get('sign_up_email', '').strip()
            sign_up_passwd = request.POST.get('sign_up_passwd', '')

            if not sign_up_name or not sign_up_email or not sign_up_passwd:
                messages.error(request, "All fields are required.")
            elif User.objects.filter(username=sign_up_name).exists():
                messages.error(request, "Username already exists.")
            else:
                user = User.objects.create_user(
                    username=sign_up_name,
                    email=sign_up_email,
                    password=sign_up_passwd
                )
                user.save()
                messages.success(request, "Account created successfully. Please sign in.")
                return redirect('accounts:sign_in')   # Redirect to signin after signup

        # ------------------- SIGN IN -------------------
        elif 'signin' in request.POST:
            sign_in_username = request.POST.get('sign_in_username', '').strip()
            sign_in_passwd = request.POST.get('sign_in_passwd', '')

            user = auth.authenticate(username=sign_in_username, password=sign_in_passwd)

            if user is not None:
                auth.login(request, user)

                # Superuser → adminindex page
                if user.is_superuser:
                    return redirect('adminindex')

                # Normal user → home page
                return redirect('index')   # safer than "/"
            else:
                messages.error(request, "Invalid username or password.")

    return render(request, 'sign_in.html')


def logout_view(request):
    auth.logout(request)
    return redirect('index')