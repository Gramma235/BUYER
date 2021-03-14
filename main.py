class buyer:
    def __init__(self):
        name = 'Имя: '+input('Введите имя: ')
        surname = 'Фамилия: '+input('Введите фамилию: ')
        lastname = 'Отчество: '+input('Введите отчество: ')
        cardnumber = 'Номер карты: '+input('Введите номер кредитной карточки: ')
        banknumber = 'Номер банковского счета: '+input('Введите номер банковского счета: ')
        self.buyer=[name,surname,lastname,cardnumber,banknumber]

    def setname(self):
        newattr = input('Введите новое значение имени: ')
        self.buyer[0] = 'Имя: ' + newattr

    def setsurname(self):
        newattr = input('Введите новое значение фамилии: ')
        self.buyer[1] = 'Фамилия: ' + newattr

    def setlastname(self):
        newattr = input('Введите новое значение имени: ')
        self.buyer[2] = 'Отчество: ' + newattr

    def setcardnumber(self):
        newattr = input('Введите новое значение номера карточки ')
        self.buyer[3] = 'Номер карты: ' + newattr

    def setbanknumber(self):
        newattr = input('Введите новое значение номера банковского счета: ')
        self.buyer[4] = 'Номер банковского счета: ' + newattr

    def getAttributes(self):
        for i in range(5):
            print(self.buyer[i])

    def getname(self):
        print(self.buyer[0])

    def getsurname(self):
        print(self.buyer[1])

    def getlastname(self):
        print(self.buyer[2])

    def getcardnumber(self):
        print(self.buyer[3])

    def getbanknumber(self):
        print(self.buyer[4])



