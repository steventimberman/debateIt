# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from multiselectfield import MultiSelectField
from django.utils import timezone
from awesome_avatar.fields import AvatarField

#USER
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=60, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    # image = AvatarField(upload_to='avatars', width=100, height=100, blank=True)
    TOPIC_CHOICES = (('Sports', 'Sports'),
                     ('Politics', 'Politics'),
                     ('Entertainment', 'Entertainment'),
                     ('Fashion', 'Fashion'),
                     ('Odd News', 'Odd News'),
                     ('Local', 'Local'),
                     ('International', 'International'),
                     ('Music', 'Music'),
                     ('Trending', 'Trending'),
                     ('Technology', 'Technology'),
                     ('Science', 'Science'),
                     ('Business', 'Business'),
                     ('Finance', 'Finance'),
                     ('Television', 'Television'),
                     ('Movies', 'Movies'),
                     ('Celebrities', 'Celebrities'),
                     ('Social Media', 'Social Media'),
                     ('Food', 'Food'),
                     ('Health', 'Health'),
                     ('Nature', 'Nature'),
                     ('Kids', 'Kids'),
                     ('Breaking News', 'Breaking News'),
                     ('Travel', 'Travel'),
                     ('Substances', 'Substances'),
                     ('United States', 'United States'),
                     ('Andimals', 'Animals'),
                     ('Art', 'Art'),
                     ('Education', 'Education'),
                     ('Employment', 'Employment'),
                     ('Brands', 'Brands')
                     )
    favorite_topics = MultiSelectField(choices=TOPIC_CHOICES, default=(('Odd News', 'Odd News')))


    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)


#DEBATE CLASSES

class Community(models.Model):
    name = models.CharField(max_length=150)
    description = description = models.CharField(max_length=350)
    photo = models.ImageField(blank=True)
    host = models.ForeignKey(User)

class DebateTopic(models.Model):
    topic = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    timestamp = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True)
    article_URL = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User)


    TOPIC_CHOICES = (('Sports', 'Sports'),
                     ('Politics', 'Politics'),
                     ('Entertainment', 'Entertainment'),
                     ('Fashion', 'Fashion'),
                     ('Odd News', 'Odd News'),
                     ('Local', 'Local'),
                     ('International', 'International'),
                     ('Music', 'Music'),
                     ('Trending', 'Trending'),
                     ('Technology', 'Technology'),
                     ('Science', 'Science'),
                     ('Business', 'Business'),
                     ('Finance', 'Finance'),
                     ('Television', 'Television'),
                     ('Movies', 'Movies'),
                     ('Celebrities', 'Celebrities'),
                     ('Social Media', 'Social Media'),
                     ('Food', 'Food'),
                     ('Health', 'Health'),
                     ('Nature', 'Nature'),
                     ('Kids', 'Kids'),
                     ('Breaking News', 'Breaking News'),
                     ('Travel', 'Travel'),
                     ('Substances', 'Substances'),
                     ('United States', 'United States'),
                     ('Andimals', 'Animals'),
                     ('Art', 'Art'),
                     ('Education', 'Education'),
                     ('Employment', 'Employment'),
                     ('Brands', 'Brands')
                     )
    tags = MultiSelectField(choices=TOPIC_CHOICES, default=(('Odd News', 'Odd News')))


    def get_absolute_url(self):
        return reverse('debate:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.topic

class DebateSide(models.Model):
    debate_topic = models.ForeignKey(DebateTopic, on_delete=models.CASCADE)
    side = models.CharField(max_length=250)
    side_points = models.BigIntegerField()

    def __str__(self):
        return self.side


#a point is a claim, or comment, on the debate. It's how other contribute.
class Point(models.Model):
    debate = models.ForeignKey(DebateTopic, on_delete=models.CASCADE, related_name='points', null=True)
    # debate_side = models.ForeignKey(DebateSide)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    claim = models.CharField(max_length=500)
    good_points = models.BigIntegerField(default=0)  #likes
    bad_points = models.BigIntegerField(default=0)   #dislikes

    def __str__(self):
        return self.claim