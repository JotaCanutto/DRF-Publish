from datetime import datetime, timedelta

from django.test import TestCase

from .models import Publish


def test_publish_is_instance():
    publish = Publish(1, 1, datetime.now(), datetime.now() + timedelta(days=10), True)

    assert isinstance(publish, Publish)
    assert hasattr(publish, 'id')
    assert hasattr(publish, 'id_pool')
    assert hasattr(publish, 'id_channel')
    assert hasattr(publish, 'initial_date')
    assert hasattr(publish, 'final_date')
    assert hasattr(publish, 'is_active')
