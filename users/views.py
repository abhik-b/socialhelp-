from django.shortcuts import render
from .models import CustomUser, FriendRequest
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    users = CustomUser.objects.exclude(id=request.user.id)
    return render(request, 'home.html', {
        'users': users
    })


def send_friend_request(request, id):
    if request.user.is_authenticated:
        # id of the user to whom send friend request
        to_user = CustomUser.objects.get(id=id)
        friendrequest, created = FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=to_user
        )
        return HttpResponseRedirect('/users/profile/{}'.format(request.user.id))


def cancel_friend_request(request, id):
    if request.user.is_authenticated:
        to_user = CustomUser.objects.get(id=id)
        friendrequest = FriendRequest.objects.get(
            from_user=request.user,
            to_user=to_user
        )
        friendrequest.delete()
        return HttpResponseRedirect('/users/profile/{}'.format(request.user.id))


def delete_friend_request(request, id):
    if request.user.is_authenticated:
        from_user = CustomUser.objects.get(id=id)
        friendrequest = FriendRequest.objects.get(
            from_user=from_user,
            to_user=request.user
        )
        friendrequest.delete()
        return HttpResponseRedirect('/users/profile/{}'.format(request.user.id))


def accept_friend_request(request, id):
    if request.user.is_authenticated:
        # id of the user who sent friend request
        from_user = CustomUser.objects.get(id=id)
        friendrequest = FriendRequest.objects.get(
            from_user=from_user, to_user=request.user)
        user1 = friendrequest.from_user
        user2 = friendrequest.to_user
        user1.friends.add(user2)
        user2.friends.add(user1)
        friendrequest.delete()
        return HttpResponseRedirect('/users/profile/{}'.format(request.user.id))


def profile_view(request, id):
    user = CustomUser.objects.get(id=id)
    sent = FriendRequest.objects.filter(from_user=user)
    recieved = FriendRequest.objects.filter(to_user=user)
    recieved_from_requestuser = FriendRequest.objects.filter(
        to_user=user, from_user=request.user)
    recieved_from_requestuser_bool = False
    if len(recieved_from_requestuser) == 1:
        recieved_from_requestuser_bool = True
    sent_to_requestuser = FriendRequest.objects.filter(
        to_user=request.user, from_user=user)
    sent_to_requestuser_bool = False
    if len(sent_to_requestuser) == 1:
        sent_to_requestuser_bool = True

    friends = user.friends.all()
    context = {
        'user': user,
        'sent': sent,
        'recieved': recieved,
        'friends': friends,
        'recieved_from_requestuser_bool': recieved_from_requestuser_bool,
        'sent_to_requestuser_bool': sent_to_requestuser_bool
    }
    return render(request, 'profile.html', context)


def search(request):
    search_query = request.GET.get('q')
    # users = CustomUser.objects.exclude(id=request.user.id)
    users = CustomUser.objects.filter(username=search_query)
    return render(request, 'searchresults.html', context={
        "users": users
    })


def remove_friend(request, id):
    user1 = request.user
    user2 = CustomUser.objects.get(id=id)
    user1.friends.remove(user2)
    user2.friends.remove(user1)
    return HttpResponseRedirect('/users/profile/{}'.format(request.user.id))
