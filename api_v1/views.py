from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import BoardGame, Category, Review
from .serializers import BoardGameSerializer, CategorySerializer, ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BoardGameViewSet(viewsets.ModelViewSet):
    queryset = BoardGame.objects.all()
    serializer_class = BoardGameSerializer

    def get_queryset(self):
        queryset = BoardGame.objects.all()

        category = self.request.query_params.get('category')
        min_players = self.request.query_params.get('min_players')
        max_players = self.request.query_params.get('max_players')
        is_available = self.request.query_params.get('is_available')

        if category:
            queryset = queryset.filter(category_id=category)
        if min_players:
            queryset = queryset.filter(min_players__lte=min_players)
        if max_players:
            queryset = queryset.filter(max_players__gte=max_players)
        if is_available:
            queryset = queryset.filter(is_available=is_available.lower() == 'true')

        return queryset

    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['patch'])
    def bulk_update(self, request):
        updated_games = []

        for item in request.data:
            game_id = item.get('id')
            try:
                game = BoardGame.objects.get(id=game_id)
            except BoardGame.DoesNotExist:
                continue

            serializer = self.get_serializer(game, data=item, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated_games.append(serializer.data)

        return Response(updated_games)

    @action(detail=False, methods=['delete'])
    def bulk_delete(self, request):
        ids = request.data.get('ids', [])
        deleted_count, _ = BoardGame.objects.filter(id__in=ids).delete()
        return Response({'deleted': deleted_count})


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        game_id = self.request.query_params.get('game_id')
        if game_id:
            queryset = queryset.filter(game_id=game_id)
        return queryset
