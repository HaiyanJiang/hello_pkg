#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:54:33 2020

@author: ginger
@email:  gingerxjiang@gmail.com
"""

from hellopkg.add_method import *
from hellopkg.utils.functions import *
from hellopkg.gendata.gen_random import *
from hellopkg.gendata.hello_gen import *


print("hellopkg succeed installed!")


hello_utils()

a = AddTwo()
a.add_data(4, 6.0)


b = AddThree()
b.add_data(4, 6.0, -3)
