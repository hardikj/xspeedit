from package import Package, NotEnoughSpace

class Packer(object):

  def __init__(self, capacity):
    self.packageCapacity = capacity
    self.packages = []

  def someotherStrategyPacking():
    pass

  def sortedPack(self, items):

    if not items:
      return []
  
    # sort and reverse items
    items.sort()
    items = items[::-1]
    print items

    # Process items
    for item in items:
      stored = False
      for package in reversed(self.packages):
        #if sum(package) + int(item) < limit+1:
        try:
          package.add(int(item))
          stored = True
          break
        except (NotEnoughSpace):
          pass
        else:
          raise RuntimeError("Something went wrong while processing the packages") 

      # first package in the chain
      if not stored:
        # Create a new package
        pkg = Package(self.packageCapacity)
        pkg.add(int(item))
        self.packages.append(pkg)

    print [ p.items for p in self.packages ]
    return self.packages

  def clear(self):
    self.packages = []
