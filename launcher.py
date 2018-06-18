def launch(products):
  Packer = Packer();
  Packer.pack(products, 10); 
  Packer.ship()
  
if __name__ == "__main__":
  launch(list("163841689525773"))
