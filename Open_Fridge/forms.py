from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms.formsets import BaseFormSet
from .models import Ingredients, Recipe

class RegistrationForms(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Password(again)",widget=forms.PasswordInput())
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Username is already taken.")

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['recipe_id', 'username']
class TagForm(forms.Form):
    tag = forms.CharField(label='tag', max_length=45)        
        
class IngredientForms(forms.Form):
    # recipe_id = forms.IntegerField(label = 'Recipe_id', initial=0)
    ingredient = forms.CharField(label='ingredient', max_length=30)
    measurement = forms.DecimalField(label='measurement', max_digits=10)
    unit = forms.CharField(max_length=20, widget=forms.TextInput())
    additionalinfo = forms.CharField(max_length=100, widget=forms.TextInput(), initial = "N/A")


class BaseIngredientFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        ingredients = []
        duplicates = False
        for form in self.forms:
            if form.cleaned_data:
                ingredient = form.cleaned_data['ingredient']
                if ingredient in ingredients:
                    duplicates = True
                ingredients.append(ingredient)

            if duplicates:
                raise forms.ValidationError(
                    'Ingredient must have Name',
                    code = 'no_name'
                )
