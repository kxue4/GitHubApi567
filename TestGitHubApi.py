#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/13/18 16:03
# @Author  : Kaiwen Xue
# @File    : TestGitHubApi.py
# @Software: PyCharm
import unittest
from GitHubApi import get_information


class GetInformationTest(unittest.TestCase):

    def test_get_information(self):
        self.assertEqual(get_information('xmicrox'), (1, ['SSW-810', 'test'], [1, 1]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)