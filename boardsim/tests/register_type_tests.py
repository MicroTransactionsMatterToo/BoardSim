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
