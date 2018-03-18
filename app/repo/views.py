from django.views.generic import TemplateView, ListView

from .models import Repo, Category


class HomeView(ListView):
    template_name = "home.html"
    context_object_name = 'repo'
    queryset = Repo.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # import ipdb
        # ipdb.set_trace()
        context['categorize_repo'] = Category.objects.all()
        return context
