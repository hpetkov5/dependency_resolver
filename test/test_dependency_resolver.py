'''
Unit tests for dependency resolver.

This module uses Python's unittest framework to validate the correctness of dependency resolver.
'''

import unittest
from src.dependency_resolver import DependencyResolver

class TestDependencyResolver(unittest.TestCase):
    """Test class defining the test cases to validate dependency resolver functionality"""

    def test_single_valid_dependency(self):
        """Call dependency resolver with package B and expect to receive single package F"""
        expected_result = ["F", "B"]
        actual_result = dependency_resolver("B")
        self.assertEqual(expected_result,actual_result)

    def test_multiple_valid_complex_dependency(self):
        """
        Call dependency resolver with package A and expect to receive packages B, D, E.
        B depends on F. D depends on G. Total dependecy list F, B, G, D, E, A."""
        expected_result = ["F", "B", "G", "D", "E", "A"]
        actual_result = dependency_resolver("A")
        self.assertEqual(expected_result,actual_result)

if __name__ == "__main__":
    unittest.main()