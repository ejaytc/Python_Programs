#class practice


class Parrot:

  species = 'bird'

  def __init__(self, name, age):
    self.name = name
    self.age = age

if __name__ == "__main__":

  #instantiate the parrot class
  blue = Parrot("blue", 10)
  woo = Parrot("woo", 10)

  #access the class attributes
  print("blue is a {}".format(blue.__class__.species))
  print("woo is a {}".format(woo.__class__.species))

  #access the instance attributes
  print("{} is {}  year old".format(blue.name, blue.age))
  print("{} is {} year old".format(woo.name, woo.age))
  
