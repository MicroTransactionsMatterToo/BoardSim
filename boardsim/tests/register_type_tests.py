import unittest
from boardsim.core import Register
from boardsim.core.base import RegisterPermissionError


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

class test_writing_of_registers(unittest.TestCase):
	def test_writing_to_default_register(self):
		test_register = Register(8)
		# ~~~~ Permission Checks ~~~~ #
		self.assertEqual(test_register[0], bin(False))
		test_register[0] = True
		self.assertEqual(test_register[0], bin(True),
						 "Writing of index 0 of Register(8) failed")

	def test_writing_to_readonly_register(self):
		test_register = Register(8, 'ro')
		# ~~~~ Permission Checks ~~~ #
		def test_write():
			test_register[0] = True
		self.assertRaises(RegisterPermissionError, test_write)

	def test_writing_to_writeonly_register(self):
		test_register = Register(8, 'wo')
		# ~~~~~~ Permission Checks ~~~~ #
		def test_read(): b = test_register[0]
		self.assertEqual(test_register.state[0], bin(False))
		test_register[0] = True
		self.assertEqual(test_register.state[0], bin(True), "Writing to Register(8, 'wo') failed")
		self.assertRaises(RegisterPermissionError, test_read)

	


