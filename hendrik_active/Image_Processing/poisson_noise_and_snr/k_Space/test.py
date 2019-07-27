class myClass:
    def __init__(self,n=1):
        self.__n=n

    def set_n(self, a):
        print("setter method called")
        self.__n = a
    def val_n(self):
        return self.__n


#create an instance, __n is 2
obj=myClass(2)

#update __n to 3
obj.set_n(3)

#verify obj.__n has changed from 2 to 3
print(obj.__n)

#why does this still return 2?
print(obj.val_n())

