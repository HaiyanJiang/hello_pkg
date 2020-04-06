#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:01:27 2020

@author: ginger
@email:  gingerxjiang@gmail.com
"""

import random


class gen_random():
    def __init__(self):
        pass

    def gen_normal_vector(self, n):
        x = [random.normalvariate(0, 1) for _ in range(n)]
        return x


def funGenData():
    print("funGen in subPack.")
    return

