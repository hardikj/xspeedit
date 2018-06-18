from packer import Packer 

def launch(products):
  packer = Packer(10)
  packer.sortedPacking(products) 
  #packer.ship()
  
if __name__ == "__main__":
  launch(list("163841689525773"))
