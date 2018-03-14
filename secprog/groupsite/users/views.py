from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from users.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.contact_num = form.cleaned_data.get('contact_num')
            user.profile.shippingAdd = form.cleaned_data.get('shippingAdd')
            user.profile.billingAdd = form.cleaned_data.get('billingAdd')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


