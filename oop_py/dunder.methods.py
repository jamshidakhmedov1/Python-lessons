# DUNDER METODLAR

class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobil xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1 

    def __str__(self):
        return f"Avto: {self.make} {self.model}" 

    def __repr__(self):
        return f"Avto: {self.make} {self.model}" 

    def __eq__(self,y):
        return self.narh==y.narh

    def __lt__(self,y):
        return self.narh<y.narh

    def __le__(self,y):
        return self.narh<=y.narh

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
    def __repr__(self):
        return f"{self.name} avtosaloni"
    def __getitem__(self,index):
        return self.avtolar[index]
    def __setitem__(self,index,qiymat):
        self.avtolar[index]  
        def add_avto(self,*qiymat):
            for avto in qiymat:
                if isinstance(avto,Avto):
                   self.avtolar.append(avto)
                else:
                    print("Avto kiriting")

salon1 = AvtoSalon("MaxAvto")

avto1 = Avto('GM','Malibu',"Qora",2020,40000)
avto2 = Avto('GM',"Lacetti","Oq",2020,2000) 
# print(avto1)

