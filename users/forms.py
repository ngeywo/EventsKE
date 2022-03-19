from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile



class RegisterUserForm(UserCreationForm):

    email= forms.EmailField()
    firstname= forms.CharField(error_messages={'required': 'errror message here'}, max_length=50)
    lastname= forms.CharField(max_length=50)


    class Meta:
        model= User
        fields= ('username','firstname','lastname','email', 'password1', 'password2')

        # def save(self,commit= True):
        #     user= Super(RegisterUserForm,self).save(commit= False)
        #     user.email= self.cleaned_data['email']
        #     if commit:
        #         user.save()
        #         return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']

    def save(self):
        photo = super(ProfileUpdateForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w + x, h + y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo
