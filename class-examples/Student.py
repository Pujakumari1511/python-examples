class Student:

    def __init__(self, first_name, last_name, klass):
        self.__first_name = first_name
        self.last_name = last_name
        self.klass = klass
        self.present = False

    def getFirstName(self):
        return self.__first_name

    def setFirstName(self, firstName):
        self.__first_name = firstName

    def deleteFirstName(self):
        del self.__first_name

    firstName = property(getFirstName, setFirstName, deleteFirstName)

    def getLastName(self):
        return self.last_name

    def setLastName(self, lastName):
        self.last_name = lastName

    lastName = property(getLastName, setLastName)

    def make_present(self):
        self.present = True

    def full_name(self):
        return self.__first_name + ' ' + self.last_name


puja = Student('Puja', 'Kumari', 7)
akash = Student('Akash', 'Kumar', 5)
piyush = Student('Piyush', 'Kumar', 12)

print(puja.getLastName())

puja.setLastName("Baranwal")
print(puja)
