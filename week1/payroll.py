class Employee:
    def __init__(self, firstName, lastName, employeeID, hourlyPay):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID
        self.hourlyPay = hourlyPay

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def setEmployeeID(self, employeeID):
        self.employeeID = employeeID

    def setHourlyPay(self, hourlyPay):
        self.hourlyPay = hourlyPay

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmployeeID(self):
        return self.employeeID

    def __str__(self):
        retStr = self.firstName
        retStr += " "
        retStr += self.lastName
        retStr += " "

    def pay(self, hrsWorked):
        if(hrsWorked <= 40):
            grossPay = hrsWorked * self.hourlyPay
            return grossPay
        elif(hrsWorked >= 40):
            overtimePay = ((hrsWorked-40)*self.hourlyPay*1.5)+self.hourlyPay*40
            return overtimePay
    

employeeIDnumber = int(input("Please enter Employee's ID number:"))
employeeFirstName = str(input("Please enter Employee's first name:"))
employeeLastName = str(input("Please enter Employee's last name:"))
hourlyPayRate = float(input("Please enter Employee's hourly pay rate: "))
hrsWorked = float(input("Please enter the hours worked for this period: "))
employee = Employee(employeeFirstName, employeeLastName, employeeIDnumber, hourlyPayRate)
wages =  employee.pay(hrsWorked)

print(employeeFirstName + " " + employeeLastName + " " + str(wages))


