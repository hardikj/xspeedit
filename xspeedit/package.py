# TODO:
# Then add some docs

class Package(object):

  def __init__(self, capacity):
    self.capacity = capacity
    self.remainingSpace = capacity
    self.items = []  

  def add(self, thing):
    if self.remainingSpace >= thing:
      self.items.append(thing)
      self.remainingSpace -= thing
    else:
      raise NotEnoughSpace('Not enough space in the package. \
                            Capacity: %s, Remaining space: %s' 
                            % (self.capacity, self.remainingSpace));

  def isFull(self):
    return self.remainingSpace == 0

  def remove(self, thing):
    return self.items.remove(thing)

class NotEnoughSpace(Exception):
    pass
