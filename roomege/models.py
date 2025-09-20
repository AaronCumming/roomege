from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    placed = models.BooleanField(default=False, null=True, blank=True)
    gender = models.CharField(max_length=127, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=127, null=True, blank=True)
    state = models.CharField(max_length=127, null=True, blank=True)
    religion = models.CharField(max_length=127, null=True, blank=True)
    church = models.CharField(max_length=127, null=True, blank=True)
    bedtime = models.TimeField(null=True, blank=True)
    waketime = models.TimeField(null=True, blank=True)
    room_state = models.IntegerField(null=True, blank=True, verbose_name = "How clean is your room right now? (on a scale of 1-10)")
    social_area = models.CharField(max_length=127, null=True, blank=True, verbose_name = "Do you like your living space to be a social area?")
    dishes_scenario = models.TextField(null=True, blank=True, 
            verbose_name = "Dilemma: It's 1am.  You just finished eating and have several dirty dishes. You also have an 8am class tomorrow. What do you do?")
    late_hw = models.TextField(null=True, blank=True, verbose_name ="How often and how late do you stay up doing home work?")
    relationship_expectation = models.TextField(null=True, blank=True, 
            verbose_name = "What kind of relationship do you expect to have with your roomate? Explain.")
    image = models.ImageField(upload_to="pictures/", null=True, blank=True)
    matches = models.ManyToManyField('self', related_name="match_lists", symmetrical=False, blank=True)

    @property
    def name(self):
        """Displays the name of the user, falls back safely if blank."""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        return "Unnamed User"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["gender", "grade", "last_name", "first_name", "age"]


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