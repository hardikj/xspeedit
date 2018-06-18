import unittest 

from xspeedit.package import Package, NotEnoughSpace

PACKAGE_CAPACITY = 10

class TestPackage(unittest.TestCase):

  def setUp(self):
    self.pkg = Package(PACKAGE_CAPACITY)

  def test_package_installation(self):
    self.assertEqual(self.pkg.items, [])
    self.assertEqual(self.pkg.capacity, PACKAGE_CAPACITY)
    self.assertEqual(self.pkg.remainingSpace, PACKAGE_CAPACITY)

  def test_add_things(self):
    self.pkg.add(1)
    self.pkg.add(2)
    self.assertEqual(len(self.pkg.items), 2)
    self.assertEqual(self.pkg.remainingSpace, 7)

  def test_throw_error(self):
    with self.assertRaises(NotEnoughSpace):
      self.pkg.add(11)
    
  def test_remove(self):
    self.pkg.add(2)
    self.pkg.add(1)
    self.pkg.remove([1])
    self.assertEqual(len(self.pkg.items), 1)

if __name__ == '__main__':
  unittest.main()

