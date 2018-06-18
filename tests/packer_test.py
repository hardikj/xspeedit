import unittest

from xspeedit.packer import Packer

PACKAGE_CAPACITY = 10

class TestPacker(unittest.TestCase):

  def setUp(self):
    self.pkr = Packer(PACKAGE_CAPACITY)

  def test_packer_installation(self):
    self.assertEqual(self.pkr.packages, [])
    self.assertEqual(self.pkr.packageCapacity, PACKAGE_CAPACITY)

  def test_pack_things(self):
    packages = self.pkr.sortedPack([1])
    self.assertEqual(len(packages), 1)
    self.pkr.clear()

    packages = self.pkr.sortedPack([])
    self.assertEqual(len(packages), 0) 
    self.pkr.clear()


    packages = self.pkr.sortedPack([8,8,9])
    self.assertEqual(len(packages), 3) 
    self.pkr.clear()


    packages = self.pkr.sortedPack([8,1,1])
    self.assertEqual(len(packages), 1) 
    self.pkr.clear()

    packages = self.pkr.sortedPack([8,9,2,1])
    self.assertEqual(len(packages), 2) 
    self.pkr.clear()

if __name__ == '__main__':
  unittest.main()
