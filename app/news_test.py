import unittest
from models import news



class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Setting up method that will run before every Test
        '''
        self.new_source = (1234,'A thrilling drift in kenyan economy','https://techcrunch.com/wp-content/uploads/2020/11/GettyImages-887657568.jpg?w=600',8.5,2000)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source))


if __name__ == '__main__':
    unittest.main()