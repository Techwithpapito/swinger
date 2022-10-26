from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

# Create your views here.

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm




@login_required
def dashboard(request):
    return render(request, 
                    "account/dashboard.html",
                    {"section":"dashboard"})

                    
# def user_login(request):
#     print("inuser login")
#     if request.method == 'POST':
#         print("posting")
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             print("cleaned", cd)
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponse("Authenticate sucessfully")
#                 else:
#                     return HttpResponse("Disabled account")

#             else:
#                 return HttpResponse("Invalid login")
#     else:
#         form = LoginForm()
#     return render(request,"account/login.html",{'form':form})
