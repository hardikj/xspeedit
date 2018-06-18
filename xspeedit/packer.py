from package import Package, NotEnoughSpace

class Packer(object):
  """
    A simple packer with two strategies. It should be able to wrap given items in
    minimum number of packages

    Usage:
    >> packer = Packer(10)
    >> packages = packer.pack(items, "sorted")

  """

  def __init__(self, capacity):
    self.packageCapacity = capacity
    self.packages = []

  def maxMinPack(self, items):
    pass

  def sortedPack(self, items):
    """
      Packing strategy which simply first sort the items and then process them
    """
    if not items:
      return []
  
    # sort and reverse items
    items.sort()
    items = items[::-1]

    # Process items
    for item in items:
      stored = False
      for package in reversed(self.packages):
        try:
          package.add(int(item))
          stored = True
          break
        except (NotEnoughSpace):
          pass
        else:
          raise RuntimeError("Something went wrong while processing the packages") 

      # item cannot fit in existing packages 
      if not stored:
        # Create a new package
        pkg = Package(self.packageCapacity)
        pkg.add(int(item))
        self.packages.append(pkg)

    return self.packages

  def clear(self):
    self.packages = []
