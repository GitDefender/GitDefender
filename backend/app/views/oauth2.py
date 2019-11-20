from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def oauth2(request):
    return redirect("https://github.com/login/oauth/authorize?scope=repo:status%20read:repo_hook%20read:org%20read:user%20user:email%20&client_id=d220f1ce704075b77610")