#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import unittest
from app.persona import Persona
from app.persona import Alumno

class TddInPythonExample(unittest.TestCase):

    def test_p_method_returns_correct_result(self):
        p = Persona("34799461R", "Susana", "Raval")
        result = "34799461R: Raval, Susana"
        self.assertEqual(str(p), result)

    def test_a_method_returns_correct_result(self):
        a = Alumno("46589499T", "Francisco", "Ceballos", "Python")
        result = "46589499T: Ceballos, Francisco (curso :Python)"
        self.assertEqual(str(a), result)


if __name__ == '__main__':
    unittest.main()
