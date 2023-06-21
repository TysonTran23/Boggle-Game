import json
from unittest import TestCase

from app import app
from flask import session

app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

class BoggleTestCase(TestCase):
    def test_form(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)

    def test_valid_word(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
            response = client.get('/guess?guess=cat')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['result'], 'ok')
    
    def test_non_on_board(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
            response = client.get('/guess?guess=dog')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['result'], 'not-on-board')
    
    def test_not_valid_word(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]] 
            response = client.get('/guess?guess=xyz')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['result'], 'not-word')
    
    def test_not_valid_word(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['highscore'] = 80
                sess['played_times'] = 6
            
            response = client.post('/game-over', json={'score': 100})
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['highscore'], 100)
            self.assertEqual(data['score'], 100)
            self.assertEqual(data['played'], 6)
    
    

    

