import unittest
import os

import sys
directory = os.path.dirname(os.path.dirname(__file__))
sys.path.append(directory)

from geolytic_modules.savegl import load_game
from geolytic_modules.CityClass import CityClass

class DirectoryTests(unittest.TestCase):
    
    def test_expected_directory_files_are_present(self):
        """
        O diretório Geolytic deve conter os conteúdos:
        Geolytic.py, geolytic_info, geolytic_modules, geolytic_saves, testing.        
        """
        list_current_directory = os.listdir(directory)
        list_correct_directory = ["Geolytic.py", "geolytic_info", "geolytic_modules", "geolytic_saves", "testing"]
        self.assertListEqual(list_current_directory, list_correct_directory)

class SavingTest(unittest.TestCase):
    pass
        

class LoadingTests(unittest.TestCase):

    def setUp(self):
        self.sample_city = CityClass('Sample City')
    
    def test_load_game_returns_none_for_unexistent_entries(self):
        """
        A função load_game() deve retornar None quando a cidade ainda não 
        existir no arquivo de saves
        """
        unexistent_city = CityClass('This city does not exist and will never exist, hopefully')
        self.assertIsNone(load_game(unexistent_city))
    
    def test_load_game_return_not_none_for_existing_entries(self):
        """
        A função load_game() deve retornar um valor que não seja None 
        quando a cidade existir no arquivo de saves
        """
        self.assertIsNotNone(load_game(self.sample_city))
        
    def test_sample_city_name_is_as_expected(self):
        """
        A função load_game() deve retornar uma cidade que tenha o mesmo
        nome da cidade enviada
        """
        name_city_unloaded = self.sample_city.name
        loaded_city = load_game(self.sample_city)
        name_city_loaded = loaded_city.name
        self.assertEqual(name_city_unloaded, name_city_loaded)

if __name__ == '__main__':
    unittest.main()
