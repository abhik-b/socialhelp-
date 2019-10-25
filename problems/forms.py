from django.forms import ModelForm
from .models import Problem, Solution


class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = ['subject', 'topic', 'content']


class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['content']
