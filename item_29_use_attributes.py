"""
This is python and not java. Do not use this stlye of setters and getters

Demonstrates how to use property with a setter method
"""


class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


class BoundedResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms


class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms


def main():
    # r1 = Resistor(50e3)
    # # a set operation is natural
    # r1.ohms = 10e3
    # r1.ohms += 5e3

    # r2 = VoltageResistance(1e3)
    # print('Before: %5r amps' % r2.current)
    # r2.voltage = 10
    # print('After: %5r amps' % r2.current)

    # r3 = BoundedResistor(1e3)
    # try:
    #     r3.ohms = 0
    # except ValueError as e:
    #     print(e)

    # r4 = FixedResistance(1e3)
    # print('r4 __dict__ is: ', r4.__dict__)
    # print('Current resistance is: ', r4.ohms)
    # try:
    #     r4.ohms = 2e3
    # except AttributeError as e:
    #     print(e)

    r7 = MysteriousResistor(10)
    r7.current = 0.01
    print('before %5r' % r7.voltage)
    r7.ohms
    print('after: %5r' % r7.voltage)



if __name__ == '__main__':
    main()
