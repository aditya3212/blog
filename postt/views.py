from django.shortcuts import render, redirect
from django.views import generic
from .models import Post

from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm 
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 
# Create your views here.


class PostList(generic.ListView):
    queryset=Post.objects.order_by('-created_on')
    template_name='index.html'


class PostDetail(generic.DetailView):
    model=Post
    template_name='post_detail.html'




#################### index####################################### 
def index(request): 
    queryset=queryset=Post.objects.order_by('-created_on')
    return render(request, 'user/index.html', {'post_list':queryset}) 
	# return render(request, 'user/index.html', {'title':'index'}) 

########### register here ##################################### 
def register(request): 
	if request.method == 'POST': 
		form = UserRegisterForm(request.POST) 
		if form.is_valid(): 
			form.save() 
			username = form.cleaned_data.get('username') 
			email = form.cleaned_data.get('email') 
			######################### mail system #################################### 
			
			################################################################## 
			messages.success(request, f'Your account has been created ! You are now able to log in') 
			return redirect('login') 
	else: 
		form = UserRegisterForm() 
	return render(request, 'user/register.html', {'form': form, 'title':'reqister here'}) 

################ login forms################################################### 
def Login(request): 
	if request.method == 'POST': 

		# AuthenticationForm_can_also_be_used__ 

		username = request.POST['username'] 
		password = request.POST['password'] 
		user = authenticate(request, username = username, password = password) 
		if user is not None: 
			form = login(request, user) 
			messages.success(request, f' wecome {username} !!') 
			return redirect('index') 
            # return redirect(views.PostList.as_view())
		else: 
			messages.info(request, f'account done not exit plz sign in') 
	form = AuthenticationForm() 
	return render(request, 'user/login.html', {'form':form, 'title':'log in'}) 

