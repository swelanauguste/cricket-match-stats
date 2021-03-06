"""cf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.MostRunsWicketsListView.as_view(), name="runs-wickets"),
    path("writeups/", views.WriteUpListView.as_view(), name="write-up-list"),
    path(
        "writeups/<int:pk>/", views.WriteUpDetailView.as_view(), name="write-up-detail"
    ),
    path(
        "top-bat/",
        views.TopPerformersBatsmanListView.as_view(),
        name="top-performer-bat-list",
    ),
    path(
        "top-bowl/",
        views.TopPerformersBowlerListView.as_view(),
        name="top-performer-bowl-list",
    ),
    path(
        "semi-top-bat/", views.SemiBatStatsListView.as_view(), name="semi-top-bat-list"
    ),
    path(
        "semi-top-bowl/",
        views.SemiBowlStatsListView.as_view(),
        name="semi-top-bowl-list",
    ),
    path(
        "presentation-ceremony/",
        views.PresentationCeremonyListView.as_view(),
        name="presentation-ceremony-list",
    ),
    path(
        "presentation-ceremony/<int:pk>/",
        views.PresentationCeremonyDetailView.as_view(),
        name="presentation-ceremony-detail",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
