from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.template import Context

def welcome_email(data):
	subject = 'Bienvenido'
	to = [data['email']]
	print(to)
	from_email = 'facilvendelo@gmail.com'
	data_for_render = data
	messages = get_template('emails/welcome-email.html').render(Context(data_for_render))
	msg = EmailMessage(
		subject,
		messages,
		from_email=from_email,
		to=to
	)
	msg.content_subtype = 'html'
	msg.send()


class Dashboard(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name="accounts/perfil.html"
		userform = UserEditForm(instance=request.user)
		profileform = ProfileEditForm(instance=request.user.profile)
		context = {
		'userform':userform,
		'profileform':profileform,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name="accounts/perfil.html"
		userform = UserEditForm(instance=request.user,data=request.POST)
		profileform = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
		if userform.is_valid() and profileform.is_valid():
			userform.save()
			profileform.save()
			messages.success(request,"Los cambios se realizaron exitosamente.")
			return redirect('profile')
		else:
			context={
			'userform':userform,
			'profileform':profileform,
			}
			return render(request,template_name,context)


class Registration(View):
	def get(self, request):
		template_name = "accounts/registration.html"
		form = UserRegistrationForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "accounts/registration.html"
		new_user_form = UserRegistrationForm(request.POST)
		data_user = request.POST
		print(data_user)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			new_user.save()
			perfil = Profile()
			perfil.user = new_user
			perfil.save()
			welcome_email(data_user)
			messages.success(request,"Su registro fue exitoso.")
			return redirect('profile')
		else:
			context = {
			'form':new_user_form
			}
			return render(request,template_name,context)
