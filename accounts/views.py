from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import UserForm

# Create your views here.
def sign_up(request):
    # Generating User Address
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Save in DB
            form.save()
            # Extract user_name, raw_password
            user_name = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('r_password')
            # Log-in
            user = authenticate(username=user_name, password=raw_password)
            login(request, user)
            return redirect('/')
    elif request.method == 'GET':
        form = UserForm()
    return render(request, 'accounts/sign_up.html', {'form':form})