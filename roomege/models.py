from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    placed = models.BooleanField(default=False)
    age = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=127, null=True, blank=True)
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



class Social(models.Model):
    """
    Social model representing a social and its URL for a church.
    """

    church = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Social Name",
        help_text="The name of the social platform. Ex: Facebook, YouTube, etc.",
    )
    link_address = models.URLField(
        max_length=511, 
        verbose_name="Social URL or Link",
        help_text="The link address or URL of the social for the Church.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the social was created.",
    )


    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"
        ordering = ["CustomUser", "name"]

    def __str__(self):
        return self.name