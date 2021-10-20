from django.contrib.auth.models import User
from django.db.models.query import RawQuerySet
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from userprofile.form import profileform, signupForm, userForm
from django.utils.translation import templatize
from userprofile.models import profile
from django.contrib import messages

# Create your views here.
# class loginview(LoginView):
#     template_name = "login.html"
#     redirect_authenticated_user = True
#     authentication_form = AuthenticationForm

#     def get_success_url(self):
#         return reverse("home:home")

def viewprofile(request, user_id):
    profileview = User.objects.get(user=user_id)
    context = {"profileview": profileview}
    return render(request, "viewprofile.html", context)

def usersprofile(request):
    allprofile = profile.objects.filter(user=request.user)
    context = {"allprofile": allprofile}
    return render(request, "usersprofile.html", context)

def loginview(request):
    if request.method == "POST":
        loginform = AuthenticationForm(data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse("home:home"))
    else:
        loginform = AuthenticationForm()
        return render(request, "login.html", {"form": loginform})

def signupview(request):
    if request.method == "POST":
        signupForm = UserCreationForm(data=request.POST)

        if signupForm.is_valid():
            signupForm.save()

        username = signupForm.cleaned_data.get('username')
        password = signupForm.cleaned_data.get('password1')

        user = authenticate(username=username, password=password)

        login(request, user)
        return HttpResponseRedirect(reverse("home:home"))
    else:
        signupForm = UserCreationForm()
        return render(request, "signup.html", {'form': signupForm})


# class signupview(CreateView):
#     model = User
#     form_class = signupForm
#     template_name = "signup.html"

#     def form_valid(self, signupForm):
#         super().form_valid(signupForm)
#         user = authenticate(
#             username=signupForm.cleaned_data.get('username'),
#             password=signupForm.cleaned_data.get('password1'))

#         login(self.request, user)
#         return HttpResponseRedirect(reverse("userprofile:userlogin")
#                                     )
#     def get_success_url(self):
#         return reverse("user:login")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home:home"))


def updateprofile(request):
    if request.method == "POST":
        pform = profileform(request.POST, request.FILES,
                            instance=request.user.profile)
        uform = userForm(request.POST, instance=request.user)
        if pform.is_valid() and uform.is_valid():
            pform.save()
            uform.save()
        return HttpResponseRedirect(reverse("userprofile:users"))
    else:
        pform = profileform(instance=request.user.profile)
        uform = userForm(instance=request.user)
    context = {'pform': pform, 'uform': uform}
    return render(request, "profileupdate.html", context)


def updatepass(request):
    if request.method == "POST":
        passchangeform = PasswordChangeForm(request.POST, request.user)
        if passchangeform.is_valid():
            user = passchangeform.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Success")
            return HttpResponseRedirect(reverse("home:home"))
        else:
            messages.error(request, "Re-Try")
    else:
        passchangeform = PasswordChangeForm(request.user)
        return render(request, "changepass.html", {"form": passchangeform})
