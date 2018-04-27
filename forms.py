from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User

class CategoryForms(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text = "Please enter category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput, required = False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForms(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text = "Please enter the title of the page")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput())
    first_visit = forms.DateTimeField(widget=forms.HiddenInput())
    last_visit = forms.DateTimeField(widget=forms.HiddenInput())
    class Meta:
        #Meta needs atleast 1 field = META
        # Provide an association between the ModelForm and a model
        model = Page
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if (url and not url.startswith ('http://')):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
