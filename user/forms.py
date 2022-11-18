
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField


 
 
class UserRegisterForm(UserCreationForm):
    # first_name = forms.CharField(max_length = 20)
    # last_name = forms.CharField(max_length = 20)
    email = forms.EmailField()
    # phone_no = forms.CharField(max_length = 20)


    


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def __init__(self,*args,**kwargs):
        super(UserRegisterForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control form-control-lg'})



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))
    class Meta:
        model = User

        fields = ['username','password']

        
    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control form-control-lg'})
