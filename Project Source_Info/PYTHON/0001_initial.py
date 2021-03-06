# Generated by Django 2.0.2 on 2018-03-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('username', models.CharField(db_column='Username', max_length=30)),
                ('email_address', models.CharField(db_column='Email Address', max_length=45)),
                ('password', models.CharField(db_column='Password', max_length=40)),
                ('created_recipes', models.CharField(blank=True, db_column='Created Recipes', max_length=500, null=True)),
                ('friends', models.CharField(blank=True, db_column='Friends', max_length=500, null=True)),
                ('user_id', models.IntegerField(db_column='User_id', primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'ACCOUNT',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posterusername', models.CharField(db_column='PosterUsername', max_length=150)),
                ('dateposted', models.DateTimeField(db_column='DatePosted')),
                ('ucomment', models.TextField(db_column='Ucomment')),
            ],
            options={
                'managed': False,
                'db_table': 'COMMENTS',
            },
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_column='username', max_length=150)),
                ('followusername', models.CharField(db_column='followUsername', max_length=150)),
                ('datefollowed', models.DateTimeField(db_column='dateFollowed')),
            ],
            options={
                'managed': False,
                'db_table': 'Following',
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('name', models.CharField(max_length=45)),
                ('measurement', models.DecimalField(db_column='Measurement', decimal_places=2, max_digits=10)),
                ('unit', models.CharField(blank=True, db_column='Unit', max_length=20, null=True)),
                ('additionalinfo', models.CharField(blank=True, db_column='AdditionalInfo', max_length=100, null=True)),
                ('id', models.CharField(blank=True, db_column='id', max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'INGREDIENTS',
            },
        ),
        migrations.CreateModel(
            name='OfficialAccountHasRecipe',
            fields=[
                ('u_id', models.IntegerField(db_column='U_id', primary_key=True, serialize=False)),
                ('recipe_id', models.IntegerField(db_column='Recipe_Id')),
            ],
            options={
                'managed': False,
                'db_table': 'Official Account_has_Recipe',
            },
        ),
        migrations.CreateModel(
            name='RECIPE',
            fields=[
                ('recipe_id', models.IntegerField(db_column='recipe_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('steps', models.CharField(db_column='Steps', max_length=500)),
                ('username', models.CharField(max_length=150)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'RECIPE',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_column='Tag', max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'Tags',
            },
        ),
    ]
