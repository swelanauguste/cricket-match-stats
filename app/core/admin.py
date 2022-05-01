from django.contrib import admin

from .models import MostRuns, MostWickets, Sponsor, WriteUp, TopPerformersBowler, TopPerformersBatsman, SemiBatStats, SemiBowlStats

admin.site.register(MostWickets)
admin.site.register(MostRuns)
admin.site.register(Sponsor)
admin.site.register(WriteUp)
admin.site.register(TopPerformersBowler)
admin.site.register(TopPerformersBatsman)
admin.site.register(SemiBatStats)
admin.site.register(SemiBowlStats)