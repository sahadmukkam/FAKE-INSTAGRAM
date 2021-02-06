from django.shortcuts import render,HttpResponse,redirect
from .forms import Sign_up
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage


def reg(request):
    if request.method=='POST':
        email= request.POST['email']
        password= request.POST['password']
        user=authenticate(email=email,password=password)
        if user:
            if user.is_verified:
                login(request, user)
                return redirect('posts:home')
            else:
                return render(request, "accounts/register.html", {'error': True,
                 'error_msg': 'please verify your email address'})
        else:
            return render(request, "accounts/register.html", {'error': True,
            'error_msg': 'username or password is incorrect'})

    return render(request,'accounts/register.html')

def sign(request):
    if request.method=='POST':
        form = Sign_up(request.POST)
        user = form.save()
        generate_verification_email(user, request)
        return redirect('posts:home')
    form=Sign_up()
    return render(request,'accounts/signup.html',{'form':form})

def generate_verification_email(user, request):
    # token generation
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    current_site = get_current_site(request)

    message = f"verify email http://{current_site}/accounts/activate/{uid}/{token}/"

    email = EmailMessage('Insta verify email', message, to=[user.email])
    email.send()

    print(message)



# class Sign_up(FormView):
#     template_name = "accounts/signup.html"
#     form_class = Sign_up

#     def form_valid(self, form):
#         user = form.save()
#         generate_verification_email(user, self.request)
#         return redirect("/")

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_verified = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')




# class RegisterView(FormView):
#     template_name = "accounts/register.html"
#     form_class = RegisterForm

#     def form_valid(self, form):
#         form.save()
#         return redirect("/")

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

# Create your views here.
