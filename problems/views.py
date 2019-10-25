from django.shortcuts import render, redirect
from .models import Problem, Solution
from .forms import ProblemForm, SolutionForm
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from users.models import CustomUser
# Create your views here.


def add_problem(request):
    if request.method == "POST":
        form = ProblemForm(request.POST)
        if form.is_valid:
            form.instance.posted_by = request.user
            form.save()
            return redirect('/problems/')
    form = ProblemForm()
    return render(request, 'addproblem.html', context={
        'form': form
    })


class ProblemListView(ListView):
    model = Problem
    context_object_name = 'problems'
    template_name = "problems_list.html"


def friends_problem(request):
    friends_problems = []
    if request.user.is_authenticated:
        problems = Problem.objects.exclude(posted_by=request.user)
        for p in problems:
            if p.posted_by in request.user.friends.all():
                friends_problems.append(p)
        return render(request, 'home.html', context={
            'friends_problems': friends_problems
        })


def problemdetail(request, id):
    problem = Problem.objects.get(id=id)
    if request.method == "POST":
        soln = SolutionForm(request.POST)
        if soln.is_valid:
            soln.instance.provided_by = request.user
            soln.instance.problem = problem
            soln.save()
            return redirect('/problems/{}'.format(id))
    soln = SolutionForm()

    return render(request, 'problemdetail.html', context={
        'problem': problem,
        'soln': soln,
    })


def verifysolution(request, id):
    sol = Solution.objects.get(id=id)

    sol.verified = 'True'
    sol.save()
    user = CustomUser.objects.get(id=sol.provided_by.id)
    user.verified_solutions_count += 1
    user.save()
    return HttpResponseRedirect('/problems/{}'.format(sol.problem.id))
