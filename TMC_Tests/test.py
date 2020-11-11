import os, sys
import time

import datetime

from atl.utils.sequences.namespace import Namespace
from autolib.neo import NeoTestCase, Data
from autolib.pmax import TestList, TestRunner, LoadTestsFromClass
from testcase.testcase import TestCase
from testcase.testflow import executable

_ALIAS_ = 'Testcases'


class Data(Namespace):
    def __init__(self): pass


@executable(context=Data)
class Trainee(NeoTestCase):
    def __init__(self, data, test):
        self.data = data
        super().__init__(test)

    def CreateEnvironment(self): pass

    def RemoveEnvironment(self): pass

    def Setup(self): pass

    def Close(self): pass

    def Test1_Test(self):
        self.AddMessage("Hello!")
