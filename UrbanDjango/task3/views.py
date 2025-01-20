from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def platform(request):
    return render(request, 'second_task/platform.html')

def games(request):
    games_title = 'Игры'
    games_list = ['Atomic Heard', 'Cyberpunk 2077', 'PayDay2']
    context = {'games_title': games_title, 'games_list': games_list}
    return render(request, 'second_task/games.html', context)


class cart(TemplateView):
    template_name = 'second_task/cart.html'

