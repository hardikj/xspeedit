# -*- coding: utf-8 -*-

class Package(object):
  """
    Serve as a base wrapper with costant space to store the items
  """

  def __init__(self, capacity):
    self.capacity = capacity
    self.remainingSpace = capacity
    self.items = []  

  def add(self, thing):
    # Add an item if there is space else throw an error
    if self.remainingSpace >= thing:
      self.items.append(thing)
      self.remainingSpace -= thing
    else:
      raise NotEnoughSpace('Not enough space in the package. \
                            Capacity: %s, Remaining space: %s' 
                            % (self.capacity, self.remainingSpace));

  def isFull(self):
    # Check if there is space
    return self.remainingSpace == 0

  def remove(self, things):
    # Remove an items
    for thing in things:
      return self.items.remove(thing)


class NotEnoughSpace(Exception):
    pass
