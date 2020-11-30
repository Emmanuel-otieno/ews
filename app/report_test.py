import unittest
from models import  Report

Sources = Report.Sources
class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Setting up method that will run before every Test
        '''
        self.new_source =Report(1234,'Kenyans debts still flactuating','A thrilling drift in kenyan economy','https://techcrunch.com/wp-content/uploads/2020/11/GettyImages-887657568.jpg?w=600',8.5,2000)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Report))


if __name__ == '__main__':
    unittest.main()