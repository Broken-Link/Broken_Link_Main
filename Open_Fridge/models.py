# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    username = models.CharField(db_column='Username', max_length=30)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email Address', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.CharField(db_column='Password', max_length=40)  # Field name made lowercase.
    created_recipes = models.CharField(db_column='Created Recipes', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    friends = models.CharField(db_column='Friends', max_length=500, blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACCOUNT'


class Comments(models.Model):
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING, db_column='Recipe_id')  # Field name made lowercase.
    posterusername = models.CharField(db_column='PosterUsername', max_length=150)  # Field name made lowercase.
    dateposted = models.DateTimeField(db_column='DatePosted')  # Field name made lowercase.
    ucomment = models.TextField(db_column='Ucomment')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMMENTS'


class Following(models.Model):
    username = models.CharField(db_column='username', max_length=150)
    followusername = models.CharField(db_column='followUsername', max_length=150)  # Field name made lowercase.
    datefollowed = models.DateTimeField(db_column='dateFollowed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Following'


class Ingredients(models.Model):
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING, db_column='Recipe_id')  # Field name made lowercase.
    name = models.CharField(max_length=45)
    measurement = models.DecimalField(db_column='Measurement', max_digits=10, decimal_places=2)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    additionalinfo = models.CharField(db_column='AdditionalInfo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'INGREDIENTS'


class OfficialAccountHasRecipe(models.Model):
    u_id = models.IntegerField(db_column='U_id', primary_key=True)  # Field name made lowercase.
    recipe_id = models.IntegerField(db_column='Recipe_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Official Account_has_Recipe'
        unique_together = (('u_id', 'recipe_id'),)


class Recipe(models.Model):
    recipe_id = models.IntegerField(db_column='Recipe_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    steps = models.TextField(db_column='Steps')  # Field name made lowercase.
    username = models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'opt/fridge480/fridge480/static/images/')
    likes = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'RECIPE'


class Tags(models.Model):
    tag = models.CharField(db_column='Tag', max_length=100)  # Field name made lowercase.
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='Recipe_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tags'
        
class UserStats(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=150)
    followers = models.IntegerField()
    following = models.IntegerField()
    recipes = models.IntegerField()
    likes = models.IntegerField()
    accountimage = models.CharField(db_column='accountImage', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User_Stats'
        
class Likes(models.Model):
    idlikes = models.AutoField(db_column='idLikes', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=150)
    recipeid = models.IntegerField(db_column='recipeID')  # Field name made lowercase.
    dateliked = models.DateTimeField(db_column='dateLiked')  # Field name made lowercase.
    recipeowner = models.CharField(db_column='recipeOwner', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Likes'
