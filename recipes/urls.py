from .views import MyRecipesView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    RegisterView,
    RecipeListView,
    RecipeDateListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('data/', RecipeDateListView.as_view(), name='recipe-date'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe-edit'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='recipes/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='recipe-list'), name='logout'),
    path('my-recipes/', MyRecipesView.as_view(), name='my-recipes'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
