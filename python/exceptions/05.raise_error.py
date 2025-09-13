def brew_chai(flavour):
    if flavour not in ["masala", "ginger", "elaichi"]:
        raise ValueError(f"We don't have {flavour} chai")
    print(f"Brewing {flavour} chai....")

# brew_chai("mint") # this line gives error
brew_chai("masala")