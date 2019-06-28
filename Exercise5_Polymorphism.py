#Data Encapsulation


class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

    
class Penguin:
    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


if __name__ == "__main__":

    #common interface
    def flying_test(bird):
        bird.fly()

    def swimming_test(bird):
        bird.swim()
        
    blue = Parrot()
    peggy = Penguin()

    #pass the object
    flying_test(blue)
    flying_test(peggy)
    swimming_test(blue)
    swimming_test(peggy)

