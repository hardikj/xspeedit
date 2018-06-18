# TODO:
# Then add some docs

class Package(object):

  def __init__(self, capacity):
    self.capacity = capacity
    self.remainingSpace = capacity
    self.items = []  

  def add(self, things):
    for thing in things:
      if self.remainingSpace >= thing:
        this.items.push(thing)
        this.remainingSpace -= thing
      else:
        #throw new PackageNotEnoughSpace(this.capacity, this.remainingSpace);
        pass

  def isFull(self):
    return self.remainingSpace == 0

  def remove(self, things):
    for thing in things:
      capacity.remove(thing)

class PackageNotEnoughSpace(Error):
  def __init__(self, capacity, remainingSpace):
    #super('Not enough space in the package. Capacity: ${capacity} Remaining space: ${remainingSpace}');
    pass
