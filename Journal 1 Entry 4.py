class Cats:
    def __init__(self,ar_length, leg_length, num_eyes, tail, furry  ):
        self.ar_length = ar_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.tail = tail
        self.furry = furry

    def description(self):
        print("My fav animal is the cat, its average arm length is " ,self.ar_length,  " and its average leg length is ",  self.leg_length)
        print("It has " , self.num_eyes , " eyes")
        if self.tail:
            print("it has very cute tail")
        if self.furry:
            print("it also has a very soft and cute fur")
def main():
    cats = Cats(7, 7, 2, True, True)
    cats.description()

if __name__ == "__main__":
    main()
