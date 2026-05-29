from rest_framework import serializers

from .models import BoardGame, Category, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class BoardGameSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = BoardGame
        fields = [
            'id',
            'title',
            'category',
            'category_id',
            'min_players',
            'max_players',
            'play_time',
            'difficulty',
            'is_available',
            'description',
            'created_at',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    game = serializers.StringRelatedField(read_only=True)
    game_id = serializers.PrimaryKeyRelatedField(
        queryset=BoardGame.objects.all(),
        source='game',
        write_only=True
    )

    class Meta:
        model = Review
        fields = ['id', 'game', 'game_id', 'author_name', 'rating', 'text', 'created_at']
