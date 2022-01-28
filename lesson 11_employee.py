class Employee():
    """Создает работника или сотрудника."""
    
    def __init__(self, first_name, last_name, annual_salary):
        """Инициализирует атрибуты сотрудника."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, salary=5000):
        """Увеличивает ежегодный окалад на 5000$."""
        self.annual_salary += salary
