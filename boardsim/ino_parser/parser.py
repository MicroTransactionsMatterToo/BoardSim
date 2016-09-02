# ardsim :: 
# 
# Date Created: 1/09/16
# License: Apache License, 2.0
# Authors: Ennis Massey <ennisbaradine@gmail.com>
#
#
#

from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as re

def inofile(): return ZeroOrMore(inocode), EOF
def inofunc(): return TypeName, call, '{' ZeroOrMore(call), '}'
def TypeName(): return re(r'void|int|bool|float|double|long|long long')
def call()