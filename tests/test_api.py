
class TestApi(object):
    def test_hello_world(self, client):
        res = client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('hello world', str(res.data))