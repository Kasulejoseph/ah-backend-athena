# Generated by Django 2.1.3 on 2019-01-31 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('body', models.TextField(db_index=True)),
                ('description', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favourited', models.BooleanField(default=False)),
                ('favouriteCount', models.IntegerField(default=0)),
                ('likes_count', models.IntegerField(default=0)),
                ('like', models.TextField(default='')),
                ('read_time', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0)),
                ('read_count', models.IntegerField(default=0)),
                ('facebook_shares', models.IntegerField(default=0)),
                ('twitter_shares', models.IntegerField(default=0)),
                ('email_shares', models.IntegerField(default=0)),
                ('avg_rating', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ArticleImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(blank=True, null=True)),
                ('description', models.CharField(db_index=True, max_length=255)),
                ('position_in_body_before', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_slug', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='ComentLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('likes_count', models.IntegerField(default=0)),
            ],
            options={
                'get_latest_by': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Readings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReportArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(db_index=True, max_length=255)),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-reported_at'],
            },
        ),
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=10)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
