class Foglalas:
    def __init__(self,fo,datum,tol,ig,id=0):
        self.__fo=fo
        self.__datum=datum
        self.__tol=tol
        self.__ig=ig
        self.__id=id

    def set_id(self,id):
        self.__id=id

    def set_fo(self,fo):
        self.__fo=fo

    def set_datum(self,datum):
        self.__datum=datum

    def set_tol(self,tol):
        self.__tol=tol

    def set_ig(self,ig):
        self.__ig=ig

    def get_id(self):
        return self.__id

    def get_fo(self):
        return self.__fo

    def get_datum(self):
        return self.__datum

    def get_tol(self):
        return self.__tol

    def get_ig(self):
        return self.__ig

    def __str__(self):
        return f"{self.get_fo()},{self.get_datum()},{self.get_tol()},{self.get_ig()},{self.get_id()}"

    def __lt__(self, other):
        if self.__datum==other.datum():
            if self.__tol==other.tol():
                return self.__fo()<other.fo()

    def __le__(self, other):
        if self.__datum==other.datum():
            if self.__tol==other.tol():
                return self.__fo()<=other.fo()

    def __ge__(self, other):
        if self.__datum==other.datum():
            if self.__tol==other.tol():
                return self.__fo()>=other.fo()

    def __gt__(self, other):
        if self.__datum==other.datum():
            if self.__tol==other.tol():
                return self.__fo()>other.fo()

    def __eq__(self, other):
        if self.__datum == other.datum():
            if self.__tol == other.tol():
                return self.__fo()==other.fo()
