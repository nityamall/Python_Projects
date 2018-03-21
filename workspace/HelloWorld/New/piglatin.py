class word:
    l=0
    n=""
    c=0
    g=[]
    j=[]
    a=[]

    def input(self):
        self.n=input("Enter a word").casefold()
        self.l=len(self.n)
    def process(self):
        for self.i in range(0,self.l):
            if(self.n[self.i]=='a'or self.n[self.i]=='e'or self.n[self.i]=='i'or self.n[self.i]=='o' or self.n[self.i]=='u'):
                self.c=self.i
                break
            else:
                self.g.append(self.n[self.i])
        for self.k in range(self.c,self.l):
            self.j.append(self.n[self.k])
        self.g.append('ay')
        self.j.append(self.g)
        print(self.j)

ob=word()
ob.input()
ob.process()






