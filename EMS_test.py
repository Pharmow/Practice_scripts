import unittest
from unittest.mock import patch
from io import StringIO

class EmployeeManagementSystemTest(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_employee(self, mock_stdout):
        # Test adding an employee record
        emp_id = "1001"
        name = "John Doe"
        department = "Sales"
        salary = "50000"
        expected_output = "Employee record added successfully.\n"
        with patch('builtins.input', side_effect=[emp_id, name, department, salary]):
            add_employee()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(employee_records[emp_id], {"name": name, "department": department, "salary": salary})
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_view_employee(self, mock_stdout):
        # Test viewing an existing employee record
        emp_id = "1001"
        employee_records[emp_id] = {"name": "John Doe", "department": "Sales", "salary": "50000"}
        expected_output = "Employee ID: 1001\nName: John Doe\nDepartment: Sales\nSalary: 50000\n"
        with patch('builtins.input', return_value=emp_id):
            view_employee()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
        
        # Test viewing a non-existent employee record
        emp_id = "9999"
        expected_output = "Employee record not found.\n"
        with patch('builtins.input', return_value=emp_id):
            view_employee()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_employee(self, mock_stdout):
        # Test deleting an existing employee record
        emp_id = "1001"
        employee_records[emp_id] = {"name": "John Doe", "department": "Sales", "salary": "50000"}
        expected_output = "Employee record deleted successfully.\n"
        with patch('builtins.input', return_value=emp_id):
            delete_employee()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertNotIn(emp_id, employee_records)
        
        # Test deleting a non-existent employee record
        emp_id = "9999"
        expected_output = "Employee record not found.\n"
        with patch('builtins.input', return_value=emp_id):
            delete_employee()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
