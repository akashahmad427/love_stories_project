from django.test import TestCase

# Create your tests here.
from stories import models

class UsermodelTest(TestCase):
    def test_create_user(self):
        name = 'Ali Hamza'
        moral = 'sad love story'
        story = 'Sad Love Story is a 2005 South Korean television drama series starring Kwon Sang-woo, Kim Hee-sun and Yeon Jung-hoon. It aired on MBC from January 5 to March 17, 2005 on Wednesdays and Thursdays at 21:55 for 20 episodes.'
        user = models.Data(name = name,moral = moral,story = story)
        self.assertEqual(user.name,name)
        self.assertEqual(user.moral,moral)
        self.assertEqual(user.story,story)
        