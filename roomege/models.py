from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    placed = models.BooleanField(default=False)
    age = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=127)
    city = models.CharField(max_length=127)
    state = models.CharField(max_length=127)
    religion = models.CharField(max_length=127, null=True, blank=True)
    church = models.CharField(max_length=127, null=True, blank=True)
    bedtime = models.TimeField(null=True, blank=True)
    waketime = models.TimeField(null=True, blank=True)
    room_state = models.IntegerField(null=True, blank=True)
    social_area = models.CharField(max_length=127, null=True, blank=True)
    dishes_scenario = models.TextField(null=True, blank=True)
    late_hw = models.TextField(null=True, blank=True)
    relationship_expectation = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="pictures/")

    @property
    def name(self):
        """ Displays the name of the user. """
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["grade", "last_name", "first_name", "age"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"



class Social(models.Model):
    """
    Social model representing a social and its URL for a user.
    """

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="socials",
        verbose_name="User",
        help_text="The user this social belongs to.",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Social Name",
        help_text="The name of the social platform. Ex: Facebook, YouTube, etc.",
    )
    link_address = models.URLField(
        max_length=511, 
        verbose_name="Social URL or Link",
        help_text="The link address or URL of the social for the user.",
    )

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"
        ordering = ["user", "name"]

    def __str__(self):
        return self.name