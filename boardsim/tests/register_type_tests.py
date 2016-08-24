import unittest
from boardsim import Register


class test_instantiation_of_registers(unittest.TestCase):
    def test_with_generic_args(self):
        test_register = Register(8)  # Create a new register, with a size of 8
        # ~~~ Value Checks ~~~~~ #
        self.assertEqual(len(test_register), 8,
                         "Length of Register(8) not equal to 8")
        self.assertEqual(test_register.state,
                         [bin(False) for x in range(8)],
                         "Default Value of all bits in Register(8)"
                         "not set to False")
        self.assertEqual(test_register.perms,
                         ['rw' for x in range(8)],
                         "Default permissions incorrectly set")

    def test_with_readonly_args(self):
        test_register = Register(8, 'ro')
        # ~~~~ Value Checks ~~~~~ #
        self.assertEqual(len(test_register), 8,
                         "Length of Register(8) not equal to 8")
        self.assertEqual(test_register.state,
                         [bin(False) for x in range(8)],
                         "Default Value of all bits in Register(8)"
                         "not set to False")
        self.assertEqual(test_register.perms,
        				 ['ro' for x in range(8)],
        				 "Permissions incorrectly set for Register(8, 'ro')")

    def test_with_write_only_args(self):
    	test_register = Register(8, 'wo')
    	# ~~~~ Value Checks ~~~~ #
    	self.assertEqual(len(test_register), 8, 
    					 "Length of Register(8, 'ro') not equal to 8")
    	self.assertEqual(test_register.state,
    					 [bin(False) for x in range(8)],
    					 "Default value of all bits in Register(8) not set to False")
    	self.assertEqual(test_register.perms,
    					 ['wo' for x in range(8)],
    					 "Permissions set incorrectly for Register(8, 'wo')")

    def test_with_non_standard_len(self):
    	test_register = Register(2)
    	# ~~~~~ Value Checks ~~~ #
    	self.assertEqual(len(test_register),
    					 2, "Length of Register(2) is not equal to 2")

