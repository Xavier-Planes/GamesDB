from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


class Developer(models.Model):
    id = models.TextField(unique=True, primary_key=True)
    developer_name = models.TextField()
    fundation_year = models.TextField(blank=True, null=True)
    founder = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    province_or_state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)    
    videogame_genere_preferences = models.TextField(blank=True, null=True)
    average_videogames_rating = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    ins_creator = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('gamesdb:developers_detail', kwargs={'pk': self.pk})


class Platform(models.Model):
    id = models.TextField(unique=True, primary_key=True)
    console_name = models.TextField()
    controller = models.TextField(blank=True, null=True)
    generation = models.TextField(blank=True, null=True)
    developer = models.ForeignKey(Developer, default=1)
    manufacturer = models.TextField(blank=True, null=True)
    cpu = models.TextField(blank=True, null=True)
    memory = models.TextField(blank=True, null=True)
    graphics = models.TextField(blank=True, null=True)
    sound = models.TextField(blank=True, null=True)
    display = models.TextField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    ins_creator = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('gamesdb:platforms_detail', kwargs={'pk': self.pk})


class Game(models.Model):
    id = models.TextField(unique=True, primary_key=True)
    game_title = models.TextField()
    platform = models.ForeignKey(Platform, default=1)
    release_date = models.TextField(blank=True, null=True)
    ESRB = models.TextField(blank=True, null=True)
    generes = models.TextField(blank=True, null=True)
    trailer = models.URLField(blank=True, null=True)
    developer = models.ForeignKey(Developer, default=1)
    rating = models.TextField(blank=True, null=True)
    updates = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="media", blank=True, null=True)
    ins_creator = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('gamesdb:games_detail', kwargs={'pk': self.pk})

    def average_rating(self):
        ratingSum = sum([float(review.rating) for review in self.gamereview_set.all()])
        reviewCount = self.gamereview_set.count()
        return ratingSum / reviewCount


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)


class GameReview(Review):
    game = models.ForeignKey(Game)
