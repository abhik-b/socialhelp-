from django.urls import path
from .views import add_problem, ProblemListView, friends_problem, problemdetail, verifysolution
app_name = 'problems'
urlpatterns = [

    path('', ProblemListView.as_view(), name='problem-list'),
    path('addproblem/', add_problem, name='addproblem'),
    path('friendsproblems/', friends_problem, name='friendsproblem'),
    path('<int:id>/', problemdetail, name='problemdetail'),
    path('verifysolution/<int:id>/', verifysolution, name='verifysolution')
]
