import pytest
from django.test import TestCase
from django.urls import reverse

class AboutViewTest(TestCase):
    def test_basic_aboutview(self):
        """
        About view with argument 'frogs' should contain a '...frogs' heading
        """
        url = reverse('main:about', args=("frogs",))
        response = self.client.get(url)
        self.assertContains(response, "<h1>All about frogs</h1>")

    def test_aboutview_commas_and_underscores(self):
        """
        About view with argument 'frogs,_bats,_and_spiders' should contain a
        'frogs, bats, and spiders' heading
        """
        url = reverse('main:about', args=("frogs,_bats,_and_spiders",))
        response = self.client.get(url)
        self.assertContains(response,
            "<h1>All about frogs, bats, and spiders</h1>")

    def test_aboutview_using_bootstrap(self):
        """
        About view should contain a reference to "bootstrap.*".
        """
        url = reverse('main:about', args=("frogs",))
        response = self.client.get(url)
        self.assertContains(response, "bootstrap.")
