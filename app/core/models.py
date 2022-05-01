from django.db import models

# class TopPerformers(models.Model):
#     pass


class MostRuns(models.Model):
    player = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    runs = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Most Runs"

    def __str__(self):
        return f"{self.player} - {self.team} - {self.runs}"


class MostWickets(models.Model):
    player = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    wickets = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Most Wickets"

    def __str__(self):
        return f"{self.player} - {self.team} - {self.wickets}"


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="sponsors")

    def __str__(self):
        return self.name


class WriteUp(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    team1 = models.ImageField(upload_to="writeups_team1")
    team2 = models.ImageField(upload_to="writeups_team2")

    def __str__(self):
        return self.title


class TopPerformersBowler(models.Model):
    player = models.CharField(max_length=100)
    matches = models.IntegerField()
    maidens = models.IntegerField(default=0)
    overs = models.IntegerField()
    runs = models.IntegerField()
    wickets = models.IntegerField()

    class Meta:
        verbose_name_plural = "Top Performers Bowlers"
        ordering = ("-wickets", "runs")

    def __str__(self):
        return f"{self.player} - {self.wickets}"


class TopPerformersBatsman(models.Model):
    player = models.CharField(max_length=100)
    matches = models.IntegerField()
    innings = models.IntegerField()
    runs = models.IntegerField()

    class Meta:
        verbose_name_plural = "Top Performers Batsmen"
        ordering = ("-runs",)

    def __str__(self):
        return f"{self.player} - {self.runs}"


class SemiBatStats(models.Model):
    player = models.CharField(max_length=100)
    matches = models.IntegerField(default=1)
    innings = models.IntegerField(default=1)
    not_out = models.CharField(max_length=100, default=0)
    runs = models.CharField(max_length=100)
    average = models.CharField(max_length=100, default=0)
    top_score = models.CharField(max_length=100)
    fifty = models.IntegerField(default=0)
    strike_rate = models.FloatField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    balls = models.IntegerField(default=0)
    dots = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Semi-Final Batting Stats"
        ordering = ("-runs",)

    def __str__(self):
        return f"{self.player} - {self.runs}"


class SemiBowlStats(models.Model):
    player = models.CharField(max_length=100)
    matches = models.IntegerField(default=1)
    overs = models.IntegerField(default=2)
    maidens = models.IntegerField(default=0)
    runs = models.IntegerField()
    wickets = models.IntegerField(default=1)
    wides = models.IntegerField(default=0)
    no_balls = models.IntegerField(default=0)
    average = models.FloatField(default=0)
    econ = models.FloatField(default=0)
    strike_rate = models.FloatField()
    best = models.CharField(max_length=100)
    strike_rate = models.FloatField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    dots = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Semi-Final Bowling Stats"
        ordering = ("-wickets",)

    def __str__(self):
        return f"{self.player} - {self.wickets}"
