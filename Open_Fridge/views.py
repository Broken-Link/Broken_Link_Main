from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import RequestContext
from django.forms.formsets import formset_factory, BaseFormSet
from .forms import RegistrationForms, IngredientForms, BaseIngredientFormSet, RecipeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

# Create your views here.
from .models import Recipe, Ingredients, Comments

def index(request):
    """
    View function for home page of site.
    """   
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={},
    )

def database(request) :
    """
    View function for database of site.
    """
    # Generate counts of some of the main objectss
    list_recipes = Recipe.objects.all()
    num_recipes = Recipe.objects.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'database.html',
        context={'list_recipes' : list_recipes, 'num_recipes' : num_recipes},
    )

def results(request):

    option = request.GET.get('option')
    key = request.GET.get('search')
    if option == 'title':
        list_recipes = Recipe.objects.all().filter(name__icontains = key)
        print(key)
        print(list_recipes)
        if len(list_recipes) > 0:
            q = request.GET['search']
            list_recipes = Recipe.objects.filter(name__icontains= q)
            return render(request, 'results.html', context ={'list_recipes' : list_recipes, 'searched' : q, 'option':option},)
        else:
            error = "Couldn't find a recipe with that title"
            return render(request, 'index.html', context={ 'error' : error},)        
    elif option == 'ingredients':
        include = key.split(",")
        for ing in include:
            list_recipes = Recipe.objects.filter(ingredients__name = ing).distinct();
        return render(request, 'results.html', context = {'list_recipes' : list_recipes, 'option':option, 'include': include},)

    else:
        list_users = User.objects.filter(username__contains = key, is_superuser = 0);        print(list_users)
        return render(request, 'results.html', context = {'list_users': list_users, 'option':option},)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password='password')
    if user is not None:

        login(request, user)
        return redirect('%s?next=%s'%(
            reverse('accountPage'),
            urlquote(request.get_full_path())))
    else:
        error = "Invalid Login Credentials!"
        return render(request, '')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            return HttpResponseRedirect('/')
        
    form = RegistrationForms()
    #variables = RequestContext(request,{'form':form})
    return render(request,
                  'registration/register.html',
                   context={'form':form})

@login_required
def recipe_register(request):
    IngredientFormSet = formset_factory(IngredientForms, formset=BaseIngredientFormSet)
    if request.method =='POST':
        recipe_form = RecipeForm(request.POST)
        ingredient_formset = IngredientFormSet(request.POST)
        if recipe_form.is_valid() and ingredient_formset.is_valid():
            recipe = Recipe.objects.create(recipe_id = Recipe.objects.all().count() + 1, steps = recipe_form.cleaned_data['steps'], name = recipe_form.cleaned_data['name'], username = request.user.username, image = "NA")
            new_ingredients = []
            for ing_form in ingredient_formset:
                new_ingredients.append(Ingredients(recipe_id = recipe.recipe_id, name = ing_form.cleaned_data['ingredient'], measurement = ing_form.cleaned_data['measurement'], unit = ing_form.cleaned_data['unit'], additionalinfo = ing_form.cleaned_data['additionalinfo']))
            Ingredients.objects.bulk_create(new_ingredients)
        return HttpResponseRedirect('/index/accountPage/')
    recipe_form = RecipeForm()
    ingredient_formset = IngredientFormSet()
    context = {
       'ingredient_formset' : ingredient_formset,
       'recipe_form' : recipe_form,
    }
    return render(request, 'recipe_register.html', context)

@login_required
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk, is_superuser = 0)
        print(user)
        user_recipes = Recipe.objects.filter(username__exact = user)
        return render(request, 'user_detail.html', context = {'user': user, 'user_recipes': user_recipes,})
    except User.DoesNotExist:
        return render(request, '');

def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
        print(recipe)
        recipe_ingredients = Ingredients.objects.filter(recipe_id__exact = pk)
        recipe_comments = Comments.objects.filter(recipe_id__exact = pk)
        return render(request, 'recipe_detail.html', context = {'recipe': recipe, 'recipe_ingredients':recipe_ingredients, 'recipe_comments': recipe_comments})
    except recipe.DoesNotExist:
        return render(request, '');
    
@login_required
def accountPage(request):    
    return render(request, 'accountPage.html', context={})
