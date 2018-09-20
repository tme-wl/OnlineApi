from django.test import TestCase
from django.test import Client
from interface.models import HostName, HostName

# Create your tests here.


class SubdomainViewTests(TestCase):
    """子域名测试"""
    def test_subdomain_post(self):
        data = {
            "subdomain":""
        }

    def test_no_subdomain_post(self):
        pass
