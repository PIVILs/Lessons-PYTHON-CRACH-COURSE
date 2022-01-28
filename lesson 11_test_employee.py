import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee"""
    
    def setUp(self):
        """Создание сотрудника для всех тестов"""
        first_name = 'Павел'
        last_name = 'Гуськов'
        annual_salary = 7000
        self.my_employee = Employee(first_name, last_name, annual_salary)
        
    def test_give_default_raise(self):
        """Проверяет увеличение по умолчанию на 5000"""
        self.my_employee.give_raise()
        self.assertEqual(12000, self.my_employee.annual_salary)
        
    def test_give_custom_raise(self):
        """Проверяет увеличение на любую величину"""
        self.my_employee.give_raise(6000)
        self.assertEqual(13000, self.my_employee.annual_salary)
        
unittest.main()
