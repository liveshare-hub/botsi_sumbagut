from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from .models import Profile


def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='staff')
        instance.groups.add(group)
        for x in dir(instance):
            print(x)
        Profile.objects.create(
            user=instance,
            nama=instance.username,
        )

        print('Profile created!')


post_save.connect(user_profile, sender=User)
