from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,LoginForm



#################### index#######################################
def index(request):
    return render(request, 'homepage.html', {'page_title':'Homepage'})
###################### login ###################################



def user_login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return redirect('index')
        else:
            messages.info(request, f'Please enter correct username or password')
    form = LoginForm()
    return render(request, 'login.html', {'form': form, "page_title":"Login"})


########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')


    else:
        form = UserRegisterForm()
        return render(request, 'signup.html', {'form': form, "page_title":"Sign Up",'errors':form.errors})


@login_required
def chatbot(request):
    return render(request,'chat.html',{"page_title" : "Chat"})

def about(request):
    return render(request,'about.html',{"page_title" : "About"})

################ login forms###################################################
# def login(request):
#     form = Login()
#     # message = ''
#     if request.method == 'POST':

#         form = Login(request.POST)
#         #AuthenticationForm_can_also_be_used__

#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user is not None:
#             form = login(request, user)
#             messages.success(request, f' welcome {username} !!')
#             return redirect('index')
#         else:
#             messages.info(request, f'account done not exit plz sign in')
#     form = AuthenticationForm()
    # return render(request, 'login.html',{'form': form})

# def chat_reply_message(request):
#     from chatbot_application import chatbot
#     run_chatbot = chatbot.ChatBot()
#     msg = {'text' : run_chatbot.reply}
#     return render(request,msg)




