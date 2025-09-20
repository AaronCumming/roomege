from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    placed = models.BooleanField(default=False)
    age = models.IntegerField(null=False, blank=False)
    grade = models.CharField(max_length=127, null=False, blank=False)
    city = models.CharField(max_length=127)
    state = models.CharField(max_length=127)
    religion = models.CharField(max_length=127)
    church = models.CharField(max_length=127)
    bedtime = models.TimeField()
    waketime = models.TimeField()
    room_state = models.IntegerField()
    social_area = models.CharField(max_length=127)
    dishes_scenario = models.TextField()
    late_hw = models.TextField()
    relationship_expectation = models.TextField()

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