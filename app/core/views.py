from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import (
    MostRuns,
    MostWickets,
    Sponsor,
    TopPerformersBatsman,
    TopPerformersBowler,
    WriteUp,
)


class TopPerformersBatsmanListView(ListView):
    model = TopPerformersBatsman


class TopPerformersBowlerListView(ListView):
    model = TopPerformersBowler


class WriteUpListView(ListView):
    model = WriteUp


class WriteUpDetailView(DetailView):
    model = WriteUp


class MostRunsWicketsListView(TemplateView):
    template_name = "core/most_runs_wickets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["runs"] = MostRuns.objects.all()
        context["wickets"] = MostWickets.objects.all()
        context["sponsors"] = Sponsor.objects.all()
        return context
