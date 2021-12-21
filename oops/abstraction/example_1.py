from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print('You drive the Car')

    def stop(self):
        print('Car stopped')        

class MotorCycle(Vehicle):

    def go(self):
        print('You ride the MotorCycle')    

    def stop(self):
        print('MotorCycle stopped')        

# v = Vehicle()
c = Car()
m = MotorCycle()
# v.go()
c.stop()
m.stop()
c.go()
m.go()      