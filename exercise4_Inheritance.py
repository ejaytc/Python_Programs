#Inheritance Exercise

class Bird:

    def __init__(self):
        print("Bird is nearby")

    def whoisThiss(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


#child class

class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

if __name__ == "__main__":

    peggy = Penguin()
    peggy.whoisThis()
    peggy.whosisThis()
    peggy.swim()
    peggy.run()
