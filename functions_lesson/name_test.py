import unittest
from check_functions import get_full_name 
class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('alijon', 'valiyev')
        self.assertEqual(name,'Alijon Valiyev')
         
    def test_otasining_ismi(self):
        name = get_full_name('alijon', 'valiyev', 'olimovich')
        self.assertEqual(name,'Alijon Olimovich Valiyev' )
unittest.main()

