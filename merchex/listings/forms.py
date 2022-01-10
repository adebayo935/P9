from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Ticket,Review,UserFollows
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

User = get_user_model()


class RegisterForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['login']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('login',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('login',)


class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Entrez votre login','required':True}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Entrez votre mot de passe', 'required': True}))


class AskRevForm(forms.ModelForm):

    Titre = forms.CharField(widget=forms.TextInput(attrs={'style':"height:40px",'size':"150",'required':True}))
    Description = forms.CharField(widget=forms.Textarea(attrs={'style': "height:400px;width:1060px;",'rows':'5','cols':'33', 'size': "150"}))
    #user = forms.ModelChoiceField(queryset=User.objects.filter(id=User.id), empty_label=None)

    class Meta:
        model = Ticket
        fields = ('image',)


class MakeRevForm(forms.ModelForm):
    Sujet = forms.CharField(widget=forms.TextInput(attrs={'style':"height:40px",'size':"150",'required':True}))
    Note = forms.ChoiceField(widget=forms.RadioSelect(),choices=(('1','1/5'),('2','2/5'),('3','3/5'),('4','4/5'),('5','5/5')),required=True)
    Commentaire = forms.CharField(widget=forms.Textarea(
        attrs={'style': "height:400px;width:1060px;", 'rows': '5', 'cols': '33', 'size': "150", 'required': True}))

    class Meta:
        model = Review
        fields = ()


class UsersForm(forms.ModelForm):

    Selection = forms.ModelChoiceField(queryset=User.objects, widget=forms.Select(attrs={'style':'height:70px;width:300px;'}))

    class Meta:
        model = UserFollows
        fields = ()
        exclude = ('User',)