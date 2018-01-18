from django.views.generic.list import ListView
from django.utils import timezone

from registry.models import Kitty

class KittyListView(ListView):

    model = Kitty

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

