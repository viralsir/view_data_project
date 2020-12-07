from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            messages.success(request,f" {username} account is created you can log in now")
            return redirect('login');
        else :
            return render(request,"users/register.html",{
                    "form":form
            })

    form=UserRegisterForm()
    return render(request,"users/register.html",{
        "form":form
    })


@login_required(login_url='login')
def profileview(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"your profile is updated")
            return redirect('profile')
        else :
            return render(request, "users/account.html", {
                "u_form": u_form,
                "p_form": p_form
            })


    u_form=UserUpdateForm(instance=request.user)
    p_form=ProfileUpdateForm(instance=request.user.profile)
    return render(request,"users/account.html",{
        "u_form":u_form,
        "p_form":p_form
    })