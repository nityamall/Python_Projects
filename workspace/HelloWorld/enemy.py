class Enemy:
    life=3
    def attack(self):
        print("Ouch !!")
        self.life=self.life-1
    def checklife(self):
        if self.life<=0:
            print("I am dead !*!")
        else:
            print("I am alive. my health is :"+str(self.life))
ob=Enemy()
ob.attack()
ob.attack()
ob.checklife()