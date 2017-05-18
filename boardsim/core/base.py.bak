#           GNU GENERAL PUBLIC LICENSE
#             Version 3, 29 June 2007

# BoardSim - Microcontroller Emulation Framework
# Copyright (C) 2016  Ennis Massey

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import array

class ATM328P:
    RGSTR = [] # List of 32 Register addresses
    SFLASH = range(32) # Byte Array or something
    EEPROM = range(1000)
    IO = range(23)
    RTC = "RTC" # Placeholder for Real Time Counter
    FTC = "Flexible Counters" # No fucking clue what this is
    WDT = "Watchdog Timer" # Resets device if main loop halts for too long
    SPI = [] # Single SPI serial out
    PWRMD = [1, 2, 3, 4, 5, 6]  # 6 power modes
    TWI = [] # I2C Systems
    USART = [] # USART

    def ALU(self):
        link = registers
        link2 = registers

class RegisterPermissionError(Exception):
    """Incorrect permissions on register bit being written"""

class Register:
    def __init__(self, size: int, perms: list or str ='rw'):
        self.size = size
        self.state = [bin(False) for x in list(range(size))]
        if type(perms) is str:
            self.perms = [perms for x in range(size)]

    def __getitem__(self, item):
        if type(item) is not int:
            raise TypeError("Register indices must be slice or int, not str")
        if item < self.size and self.perms[item] in ('rw', 'ro'):
            return self.state[item]
        if item >= self.size:
            raise IndexError
        if self.perms[item] in ('wo'):
            raise RegisterPermissionError("Register bit is not readable")

    def __setitem__(self, item, value):
        if (type(value) is not bool or 
            type(item) is not int):
            raise TypeError("Register indices must be slice or int, not str")
        if item < self.size:
            if self.perms[item] in ('rw', 'wo'):
                self.state[item] = bin(value)
            elif self.perms[item] in ('ro'):
                raise RegisterPermissionError("Register bit is read-only")
        else:
            raise IndexError

    def __str__(self):
        return str("{} \n{}".format(str(self.state), str(self.perms)))

    def __len__(self):
        return len(self.state)

class IONode:
    TYPE = 'DGT'
    MEDIUM = "PIN"
    NAME = "PIN0"

class InstructionSet:
    pass

class RISCInstructionSet(InstructionSet):
    OPCODES = {
        0b000: {
            "mnemonic": "add",
            "format": "RRR",
            "result": "rB + rC -> rA"
        },
        0b001: {
            "mnemonic": "iadd",
            "format": "RRI",
            "result": "rB + iA -> rA"
        },
        0b010: {
            "mnemonic": "nand",
            "format": "RRR",
            "results": "rB + iA -> rA"
        }
    }
