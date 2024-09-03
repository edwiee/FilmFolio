from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import*

class RegistrationForm(UserCreationForm):
    # fname = forms.CharField(max_length=30)
    # lname = forms.CharField(max_length=30)
    # username = models.CharField(max_length=200, null=True)
    # password = models.CharField(max_length=200, null=True)
    # cpassword = models.CharField(max_length=200, null=True)
    # email = forms.EmailField()
    class Meta:
        model = UserManage
        fields = '__all__'

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']
