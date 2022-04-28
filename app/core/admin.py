from django.contrib import admin

from .models import MostRuns, MostWickets, Sponsor, WriteUp

admin.site.register(MostWickets)
admin.site.register(MostRuns)
admin.site.register(Sponsor)
admin.site.register(WriteUp)