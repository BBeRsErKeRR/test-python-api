class TestApi(object):

    def test_hello_world(self, client):
        res = client.get('/api/hello')
        assert res.status_code == 200
        assert 'hello world' in str(res.data)
