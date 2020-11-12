# import os
# import sys
# import time
# import datetime

from autolib.neo import NeoTestCase, Data
from testcase.testflow import executable

_ALIAS_ = 'Testcases'

@executable(context=Data)
class Trainee(NeoTestCase):

    def CreateEnvironment(self): pass

    def RemoveEnvironment(self): pass

    def Setup(self): pass

    def Close(self): pass

    def Test1_Test(self):
        self.AddMessage("Hello!")
