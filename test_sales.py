import unittest
from io import StringIO
import sys

class TestSalesTracking(unittest.TestCase):
    """Test cases for Sales Tracking System"""
    
    def setUp(self):
        """Initialize test data before each test"""
        self.sales = []
    
    def test_sales_list_initialization(self):
        """Test that sales list initializes as empty"""
        self.assertEqual(len(self.sales), 0)
        self.assertIsInstance(self.sales, list)
    
    def test_add_single_sale(self):
        """Test adding a single sales record"""
        self.sales.append(1000)
        self.assertEqual(len(self.sales), 1)
        self.assertEqual(self.sales[0], 1000)
    
    def test_add_multiple_sales(self):
        """Test adding multiple sales records"""
        sales_data = [1000, 2000, 3000]
        for sale in sales_data:
            self.sales.append(sale)
        self.assertEqual(len(self.sales), 3)
        self.assertEqual(self.sales, sales_data)
    
    def test_sales_list_not_empty(self):
        """Test that sales list contains data after addition"""
        self.sales.append(500)
        self.assertTrue(len(self.sales) > 0)
        self.assertNotEqual(self.sales, [])
    
    def test_sales_data_type(self):
        """Test that sales records are integers"""
        self.sales.append(1500)
        self.assertIsInstance(self.sales[0], int)

if __name__ == '__main__':
    unittest.main()
