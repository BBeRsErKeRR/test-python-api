
from unittest import TestCase

class TestApi(TestCase):

    def test_hello_world(self, client):
        res = client.get('/')
        assert res.status_code == 200
        assert 'hello world' in str(res.data)
