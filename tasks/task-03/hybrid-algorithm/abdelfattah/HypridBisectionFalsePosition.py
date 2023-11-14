class FalsePosition:
    def __init__(self , equDegree):
        if equDegree <= 0:
            print("invalid equation degree")
            return
        self.equDegree= equDegree
        self.operators= [0 for i in range(0 , self.equDegree+1 , 1)] 
        self.x= None
        self.a= None
        self.b= None 
        self.iters= None
    def setOperators(self):
        if self.equDegree > 0:
            for i in range(0 , self.equDegree+1 , 1):
                self.operators[i]= int(input(f"enter the operator of X{i}"))
    def power(self , x , exp):
        if exp != 0:
            res= x
            for i in range(0 , exp-1 , 1):
                res*= x 
            return res    
        return 1  
    def fx(self , x):
        res= self.operators[0]  
        for i in range(0 , self.equDegree , 1):
            res+= (self.operators[i+1] * self.power(x , i+1))
        return res    
    def calcRoot(self , a , b , eps): 
        if self.fx(a) * self.fx(b) >= 0:
            print("invalid interval") 
            self.operators=[0 for i in range(0 , self.equDegree+1 , 1)] 
            return
        self.a= a 
        self.b= b     
        self.iters= 0     
        while True:
            self.iters+= 1
            fa= self.fx(self.a)
            self.x= self.a - (fa * (self.b - self.a)) / (self.fx(self.b) - fa) 
            fx= self.fx(self.x)
            if abs(fx) <= eps:
                return self.a , self.b , self.x , self.iters , fx
            elif fx * fa < 0:
                self.b= self.x 
            else: 
                self.a= self.x 
obj= FalsePosition(3)
obj.setOperators()
print(obj.calcRoot(2 , 3 , 0.0005))
             