from django.db import models
from config.settings.base import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from core_apps.common import models as common_models

USER = AUTH_USER_MODEL

class Profile(common_models.TimeStampedUUIDModel):
    """Profile Model"""
    class Gender(models.TextChoices):
        MALE = "male", _("male")
        FEMALE = "female", _("female")
        OTHER = "other", _("other")
    
    username = models.CharField(verbose_name=_("username"), max_length=125, null=True, blank=True)
    country = CountryField(verbose_name=_("country"), default="IR", blank=False, null=False)
    gender = models.CharField(verbose_name=_("gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    about_me = models.TextField(verbose_name=_("about me"), default="Tell Me about yourself ...")
    
    user = models.OneToOneField(USER, on_delete=models.CASCADE, related_name="profile")
    follows = models.ManyToManyField("self", symmetrical=False, related_name="followed_by", blank=True)
    
    def __str__(self) -> str:
        return f"{self.user.phone}'s profile"
    
    def get_following(self):
        return self.follows.all()
    
    def get_followers(self):
        return self.followed_by.all()
    
    async def follow(self, profile):
        await self.follows.aadd(profile)
    
    async def un_follow(self, profile):
        await self.follows.aremove(profile)
        
    async def check_following(self, profile):
        return await self.follows.filter(pkid=profile.pkid).aexists()
    
    async def check_is_followed_by(self, profile):
        return await self.followed_by.filter(pkid=profile.pkid).aexists()