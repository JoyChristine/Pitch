import unittest
from app.models import Pitch,User,Comment
from app import db

class Pitch(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username="Test",password = 'banana')
        self.new_pitch = Pitch(pitch_title = 'Test',content = 'Test',category = 'Test',author = self.new_user)
        self.new_comment = Comment(content = 'Test',category = 'Test',author = self)

    def teardown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_title,'Test')
        self.assertEquals(self.new_pitch.content,'Test')
        self.assertEquals(self.new_pitch.category,'Test')
        self.assertEquals(self.new_pitch.author,self.new_user)
        self.assertEquals(self.new_pitch.comments,self.new_comment)
        self.assertEquals(self.new_pitch.likes,self.new_like)
        self.assertEquals(self.new_pitch.dislikes,self.new_dislike)

    
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch(self):
        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitch(1)
        self.assertTrue(len(got_pitches) == 1)