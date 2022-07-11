import json

class TestViews():

    def test_catch_all(self,api):
        res = api.get('/')
        assert res.status == "200 OK"

    def test_new_handler(self,api):
        res = api.get('/new')
        assert res.status == "200 OK"

    def test_edit_handler(self,api):
        res = api.get('/edit')
        assert res.status == "200 OK"

    def test_relics_handler(self,api):
        res = api.get('/relics', method="GET")
        assert res.status == "200 OK"
