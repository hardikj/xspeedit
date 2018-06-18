import argparse

from xspeedit.packer import Packer

def launch():
  parser = argparse.ArgumentParser(description='Pack items into mimimum number of package')
  parser.add_argument('items', metavar='items []', type=int, nargs='+', choices=range(1, 10),
                   help='List of itesm sizes')

  args = parser.parse_args()
  print "We got: " + ', '.join(map(str, args.items))
  packer = Packer(10)
  packages = packer.sortedPack(args.items) 
  print [ p.items for p in packages ]
  
if __name__ == "__main__":
  launch()
