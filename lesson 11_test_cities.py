import unittest
from city_functions import get_sities_name

class NamesTestCase(unittest.TestCase):
    """Тесты для 'city_functions.py'."""
    
    def test_siti_coutry_name(self):
        """Имена вида 'Santiago и Chile' работают правильно?"""
        sities_name = get_sities_name('santiago', 'chile')
        self.assertEqual(sities_name, 'Santiago Chile')

    def test_siti_coutry_name_population(self):
        """Имена вида 'Santiago Chile и население 5000000'"""
        sities_name = get_sities_name('santiago', 'chile', '5000000')
        self.assertEqual(sities_name, 'Santiago Chile- population 5000000')

unittest.main()
