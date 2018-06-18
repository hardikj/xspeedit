from package import Package

class packer(object):

  def __init__(self, capacity):
    this.packageCapacity = capacity
    this.packages = []

  def someotherStrategyPacking():
    pass

  def sortedPacking(self, items):

    if not itemss:
      return []
  
    # sort and reverse items
    items.sort()
    items = items[::-1]
    print items

    limit = 10
    # Process items
    for item in items:
      stored = False
      for package in reversed(self.packages):
        #if sum(package) + int(item) < limit+1:
        try:
          package.add(int(item))
          stored = True
          break
        except e:
          # Throw Better ERror
          raise e

      # first package in the chain
      if not stored:
        # Create a new package
        pkg = Package(self.packageCapacity)
        pkg.add(int(item))
        self.packages.append(pkg)

    print packages
    return packages
