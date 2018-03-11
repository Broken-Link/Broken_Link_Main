from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.template import RequestContext
from django.forms.formsets import formset_factory, BaseFormSet
from .forms import RegistrationForms, IngredientForms, BaseIngredientFormSet, RecipeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Recipe, Ingredients, Comments, Following, UserStats, Likes

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
            return render(request, 'results.html', context ={'list_recipes' : list_recipes, 'searched' : q, 'opti$
        else:
            error = "Couldn't find a recipe with that title"
            return render(request, 'index.html', context={ 'error' : error},)
    elif option == 'ingredients':
        pKey = key.split(',')
        print(pKey)
        #DEFAULT the first ingredient filter
        list_recipes = Recipe.objects.all()
        for p in pKey:
            list_recipes = list_recipes.filter(ingredients__name=p)
        if len(list_recipes) > 0:
            q = request.GET['search']
            return render(request, 'results.html', context = {'list_recipes': list_recipes, 'searched' : q, 'opti$
        else:
            error = "Couldn't find a recipe with those ingredients"
            return render(request, 'index.html', context={ 'error' : error},)
    else:
        list_users = User.objects.filter(username__contains = key, is_superuser = 0);        print(list_users)
        return render(request, 'results.html', context = {'list_users': list_users, 'option':option},)

@csrf_exempt
def follow(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        print("worked")
        print("action")
        print("added")
        followEntry = Following.objects.create(username = request.user.username, followusername = username, datefollowed = datetime.now())
        userFollowing = UserStats.objects.get(username = request.user.username)
        userFollowing.following += 1
        userFollowing.save()

        userFollowed = UserStats.objects.get(username = username)
        userFollowed.followers += 1
        userFollowed.save()
        
        print(followEntry)
        return JsonResponse({})
    else:
        print("No")
        return JsonResponse({})
    
@csrf_exempt
def unfollow(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        print("unfollow")
        print("action")
        print("delete")
        Following.objects.filter(username = request.user.username, followusername = username).delete()
        userFollowing = UserStats.objects.get(username = request.user.username)
        userFollowing.following -= 1
        userFollowing.save()

        userFollowed = UserStats.objects.get(username = username)
        userFollowed.followers -= 1
        userFollowed.save()
        return JsonResponse({})
    else:
        print("No")
        return JsonResponse({})

@csrf_exempt
def updateComments(request):
    if(request.method == 'POST'):
        recipeID = request.POST.get('recipeId')
        commenter = request.POST.get('commenter')
        comment = request.POST.get('comment')
        print("comment added")
        Comments.objects.create(recipe_id = recipeID, posterusername = commenter, dateposted = datetime.now(), ucomment = comment)
        return JsonResponse({})
    else:
        print("Comment not added")
        return JsonResponse({})

@csrf_exempt
def deleteComment(request):
    if(request.method == 'POST'):
        commentID = request.POST.get('pk')
        print("comment deleted")
        Comments.objects.filter(id = commentID).delete()
        return JsonResponse({})
    else:
        print("comment wasn't deleted")
        return JsonResponse({})

@csrf_exempt
def updateLike(request):
    if(request.method == 'POST'):
        recipeID = request.POST.get('recipeID')
        recipeOwner = request.POST.get('recipeOwner')
        print("like added" + recipeID)
        recipe = Recipe.objects.get(recipe_id = recipeID)
        print(recipe)
        print(recipe.likes)
        recipe.likes += 1
        recipe.save()
        Likes.objects.create(username = request.user.username, recipeid = recipeID, dateliked= datetime.now(), recipeowner = recipeOwner)
        owner = UserStats.objects.get(username = recipeOwner)
        owner.likes += 1
        owner.save()
        return JsonResponse({})
    else:
        print("Comment not added")
        return JsonResponse({})

@csrf_exempt
def removeLike(request):
    if(request.method == 'POST'):
        print("like removed")
        recipeID = request.POST.get('recipeID')
        recipeOwner = request.POST.get('recipeOwner')
        recipe = Recipe.objects.get(recipe_id = recipeID)
        print(recipe.likes)
        recipe.likes -= 1
        recipe.save()
        Likes.objects.get(username = request.user.username, recipeid = recipeID).delete()
        owner = UserStats.objects.get(username = recipeOwner)
        owner.likes -= 1
        owner.save()
        return JsonResponse({})
    else:
        print("comment wasn't deleted")
        return JsonResponse({})


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
    TagFormSet = formset_factory(TagForms, formset=BaseTagFormSet)
    recipe_form = RecipeForm(request.POST, request.FILES)
    if request.method =='POST':
        ingredient_formset = IngredientFormSet(request.POST)
        tag_formset = TagFormSet(request.POST)
        if recipe_form.is_valid() and ingredient_formset.is_valid() and tag_formset.is_valid():
                new = recipe_form.save(commit=False)
                new.recipe_id = Recipe.objects.all().count()
                new.username  = request.user.username
                new.save()
                new_ingredients = []
                for tag_form in tag_formset:
                    new_tags.append(Tags(tag = tag_form.cleaned_data['tag'], recipe_id = new.recipe_id))
                for ing_form in ingredient_formset:
                    new_ingredients.append(Ingredients(recipe_id = new.recipe_id, name = ing_form.cleaned_data['ingredient'], measurement = ing_form.cleaned_data['measurement'], unit = ing_form.cleaned_data['unit'], additionalinfo = ing_form.cleaned_data['additionalinfo']))
                Ingredients.objects.bulk_create(new_ingredients)
                Tags.objects.bulk_create(tag_form)
                return HttpResponseRedirect('/index/accountPage')
                print("Success in entering a recipe")
        else:
                print("Not Entered")
                return HttpResponseRedirect('/index/recipe_register')
    ingredient_formset = IngredientFormSet()
    recipe_form = RecipeForm()
    tag_form = TagForm()
    context = {
       'ingredient_formset' : ingredient_formset,
       'recipe_form' : recipe_form,
       'tag_form' : tag_form,
    }
    return render(request, 'recipe_register.html', context)



def user_detail(request, pk):
    try:
        userInfo = User.objects.get(pk=pk, is_superuser = 0)
        user_recipes = Recipe.objects.filter(username__exact = userInfo)
        userF = Following.objects.filter(username__exact = userInfo.username)
        user_friends = []
        f = Following.objects.filter(username = request.user.username, followusername = userInfo)
        userStats = UserStats.objects.get(username__exact = userInfo.username)
        print(f)
        following = "false"
        if len(f) > 0:
            following = "true"
                
        for userS in userF:
            user_friends.append(UserStats.objects.get(username__exact = userS.followusername))

        return render(request, 'user_detail.html', context = {'userInfo': userInfo, 'user_recipes': user_recipes, 'user_friends' : user_friends, 'following' : following, 'userStats' : userStats})
    except User.DoesNotExist:
        return render(request, '')

def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
        print(recipe)
        recipe_ingredients = Ingredients.objects.filter(recipe_id__exact = pk)
        recipe_comments = Comments.objects.filter(recipe_id__exact = pk)
        liked = "false"


        if request.user.is_authenticated:
            likedR = Likes.objects.filter(username = request.user.username, recipeid = pk)
            if len(likedR) > 0:
               liked = "true"
           
        return render(request, 'recipe_detail.html', context = {'recipe': recipe, 'recipe_ingredients':recipe_ingredients, 'recipe_comments': recipe_comments, 'liked':liked})
    except recipe.DoesNotExist:
        return render(request, '');
    
@login_required
def accountPage(request):    
    user_recipes = Recipe.objects.filter(username__exact = request.user.username)
    userF = Following.objects.filter(username__exact = request.user.username)
    user_friends = []
    userStats = UserStats.objects.get(username__exact = request.user.username)
    for userS in userF:
        user_friends.append(User.objects.get(username__exact = userS.followusername))
    return render(request, 'accountPage.html', context = {'user_recipes': user_recipes, 'user_friends' : user_friends, 'userStats' : userStats})
