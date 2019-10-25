from django.db import models
from django.contrib.auth.models import AbstractUser


class Achievements(models.Model):
    title = models.CharField(max_length=120)
    contribution_count = models.IntegerField()

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    friends = models.ManyToManyField('CustomUser', blank=True)
    verified_solutions_count = models.IntegerField(default=0)
    achievements = models.ManyToManyField(
        Achievements, blank=True, null=True)

    def achievementscompleted(self):
        for achievement in Achievements.objects.all():
            if self.verified_solutions_count == achievement.contribution_count:
                self.achievements.add(achievement)
        return self.achievements.all()

    # def __str__(self):
    #     return self.user.username


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        CustomUser, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        CustomUser, related_name='to_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "from {}, to {}".format(self.from_user, self.to_user)
