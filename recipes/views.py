from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.models import User

# Pagina principala – lista retetelor sortate alfabetic
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'
    ordering = ['title']

# Pagina separata – lista sortata dupa data
class RecipeDateListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_by_date.html'
    context_object_name = 'recipes'
    ordering = ['-created_at']

# Detalii reteta
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

# Creare reteta
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Editare reteta
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.user

# Stergere reteta
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe-list')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.user

# Inregistrare utilizator
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'recipes/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('recipe-list')
        return render(request, 'recipes/register.html', {'form': form})

# Retetele proprii
class MyRecipesView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/my_recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user).order_by('-created_at')
