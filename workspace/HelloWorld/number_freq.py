class number_freq:
    def freq(self):
        self.n=input("ENTER A NO.")
        self.n=int(self.n)
        self.b=0
        self.c=0
        self.p=self.n
        for self.i in range(0,10):
            while self.n>0:
                self.b=self.n%10
                if (self.i==self.b):
                    self.c=self.c+1
                self.n=int(self.n/10)
            print("%d"%self.i)
            print("%d"%self.c)
            print("\n")
            self.c=0
            self.n=self.p
ob=number_freq()
ob.freq()