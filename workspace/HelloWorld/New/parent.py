class parent:
    def last_name(self):
        print("Mall")
class child(parent):
    def first_name(self):
        print("Moody")
    def last_name(self):
        print("girl")
ob=child()
ob.first_name()
ob.last_name()