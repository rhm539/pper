from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    return render(request, 'dashboard/index.html', {})
>>>>>>> 17de5980e8b95cf1b208ab4cc001fe0235d861a8
