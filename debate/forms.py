from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Point
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from multiselectfield import MultiSelectField

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
    )

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #
    #     if commit:
    #         user.save()
    #
    #     return user

class UserProfileRegForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    city = forms.CharField(required=True)
    forms.CharField()
    favorite_topics = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=UserProfile.TOPIC_CHOICES)



    class Meta:
        model = UserProfile
        fields = (
            'image',
            'city',
            'favorite_topics'
        )


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Point
        fields = ('claim',)