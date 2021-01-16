from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class View404(TemplateView):
    template_name = '404.html'