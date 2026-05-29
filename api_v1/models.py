from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class BoardGame(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='games')
    min_players = models.PositiveIntegerField()
    max_players = models.PositiveIntegerField()
    play_time = models.PositiveIntegerField(help_text='Play time in minutes')
    difficulty = models.CharField(max_length=50, blank=True)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name='reviews')
    author_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author_name}: {self.game.title}'
