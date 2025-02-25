from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from adminlte3.form.auth.login_form import LoginForm
from django.http import JsonResponse

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a homepage or any other page
            else:
                # messages.error(request, "Invalid credentials")
                return redirect('login')  # Redirect back to the login page
        else:
            return JsonResponse({'message': 'Form is not validate!', 'errors': form.errors}, status=400)
    else:
        form = LoginForm()

    return render(request, '../templates/adminlte/login.html', {'form': form})
