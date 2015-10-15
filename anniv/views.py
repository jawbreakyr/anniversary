from django.shortcuts import render
from django.views.generic import TemplateView


class AnniversaryView(TemplateView):
    template_name = 'anniv/heart.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AnniversaryView, self).get_context_data(*args, **kwargs)

        return context
