from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe

class RecipeTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='pass1234')
        self.user2 = User.objects.create_user(username='user2', password='pass1234')

        self.recipe = Recipe.objects.create(
            user=self.user1,
            title='Ciorbă de legume',
            ingredients='O rețetă delicioasă.',
            cook_time='45'
        )

    def test_login_success(self):
        # Login corect – redirect (302)
        response = self.client.post(reverse('login'), {
            'username': 'user1',
            'password': 'pass1234'
        })
        self.assertEqual(response.status_code, 302)

    def test_login_failure(self):
        # Login incorect – ramanem pe pagina de login (200)
        response = self.client.post(reverse('login'), {
            'username': 'user1',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Autentificare')  # verifica titlul paginii

    def test_create_recipe_authenticated(self):
        # Utilizatorul autentificat poate adauga o reteta
        self.client.login(username='user1', password='pass1234')
        response = self.client.post(reverse('recipe-add'), {
            'title': 'Omletă',
            'ingredients': 'Ouă cu brânză',
            'cook_time': '10'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Recipe.objects.count(), 2)

    def test_delete_recipe_by_non_author(self):
        # Alt user nu are voie sa stearga o reteta care nu ii apartine
        self.client.login(username='user2', password='pass1234')
        response = self.client.post(reverse('recipe-delete', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 403)

    def test_sorting_by_title(self):
        # Retetele trebuie sa fie sortate alfabetic in recipe-list
        Recipe.objects.create(
            user=self.user1,
            title='Ardei umpluți',
            ingredients='clasic',
            cook_time='60'
        )
        response = self.client.get(reverse('recipe-list'))
        titles = [r.title for r in response.context['recipes']]
        self.assertEqual(titles, sorted(titles))
