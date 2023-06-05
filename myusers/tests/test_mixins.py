from django.test import TestCase
import pytest
from django.contrib.auth import get_user_model
from myusers.models import NewUser
from django.test import RequestFactory


User = get_user_model()
from myusers.permissions import IsStaffEditorPermission

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from rest_framework.views import APIView
from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from pytest import mark
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db
