import unittest
import sys
sys.path.append('../')
from lootbag import Lootbag

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestLootbaf(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.Loot = Lootbag()

  @classmethod
  def tearDownClass(self):
    print('Tear down class')