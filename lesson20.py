class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class CarnivorousMixIn(Animal):
    pass


class HerbivoresMixIn(Animal):
    pass


class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass


class Bat(Mammal, FlyableMixIn, HerbivoresMixIn):
    pass

# 2 tcp udp forking threading co-routine


class TCPServer(object):
    pass


class UDPServer(object):
    pass


class ForkingMixIn(object):
    pass


class ThreadingMixIn(object):
    pass


class CoroutineMixIn(object):
    pass


class MyTCPServer(TCPServer, ForkingMixIn):
    pass


class MyUDPServer(UDPServer, ThreadingMixIn):
    pass


class MyTCPServer2(TCPServer, CoroutineMixIn):
    pass