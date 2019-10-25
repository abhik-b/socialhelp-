from django.db import models
from users.models import CustomUser
from tinymce.models import HTMLField
# Create your models here.


class Problem(models.Model):
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=120, blank=True, null=True)
    topic = models.CharField(max_length=360, blank=True, null=True)
    content = HTMLField()

    def __str__(self):
        return "Problem {} by{}".format(self.id, self.posted_by.username)


class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    provided_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    reply = models.ForeignKey(
        'self', null=True, related_name='replies', on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return "comment id:{}, provided by  :-{}".format(self.id, self.provided_by)
