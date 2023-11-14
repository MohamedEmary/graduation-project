class SHA256:
    def __init__(self):
        self._64PrimrNumbers= None 
        self._8PrimeNumbers= None
        self._64ConstantsRecords= None 
        self._8HashsRecords= None 
        self.lenOrginalText= None 
        self.binaryOrginalText= None 
        self.paddingText= None 
        self.lenPaddinText= None
        self.targetBinaryHash= None
    def get64Constants(self , beg , end):
        if beg < 2: 
            print("valid interval for the start of prime numbers")
            return 
        nums= self.getPrimeNumbers(beg , end , 64)  
        if nums:
            self._64PrimrNumbers= nums
            self._64ConstantsRecords= self.getRecordsValues(self._64PrimrNumbers)
    def get8Constants(self , beg , end):
        if beg < 2: 
            print("valid interval for the start of prime numbers")
            return 
        nums= self.getPrimeNumbers(beg , end , 8)    
        if nums:
            self._8PrimeNumbers= nums
            self._8HashsRecords= self.getRecordsValues(self._8PrimeNumbers)
    def getPrimeNumbers(self , beg , end , numOfNums):
        if numOfNums <= 0:
            print("invalid number of prime numbers to find it")
            return False 
        nums= [ ] 
        numsCount= 0 
        for i in range(beg , end + 1, 1):
            iDivJCount= 0
            for j in range(1 , i + 1, 1):
                if i % j == 0:
                    iDivJCount+= 1
            if iDivJCount == 2:
                numsCount+= 1 
                nums.append(i) 
            if numsCount == numOfNums:
                return nums
        print(f"can not found {numOfNums} prime numbers in the interval {beg} to {end}") 
        return False
    def getRecordsValues(self , primeNums):
        from math import pow 
        targetPow= None 
        if len(primeNums) == 64:
            targetPow= 1/3
        else:
             targetPow= 1/2    
        res= [ ]     
        for prime in primeNums: 
            Root= pow(prime , targetPow)
            strRoot= str(Root)
            fractionalNums= strRoot.split(".")[1]
            res.append(bin(int(fractionalNums))[2 : 34])
        return res        
    def setText(self , text):
        if len(text) == 0 or type(text) != str:
            print("invalid passing data")
            return
        self.lenOrginalText= len(text)    
        val= [ ]    
        for info in text: 
            val.append(bin(ord(info))[2 : ]) 
        self.binaryOrginalText= "".join(val) 
        self.paddingText= self.binaryOrginalText
        self.padingOriginalText()
    def padingOriginalText(self):
        self.paddingText= self.paddingText + "1"
        count= len(self.paddingText)
        while (count + 64) % 512 != 0:  
            self.paddingText= self.paddingText + "0"
            count+= 1
        binaryLenOriginalText= bin(self.lenOrginalText)[2 : ]  
        count= len(binaryLenOriginalText)
        while count % 64 != 0:
            binaryLenOriginalText= "0" + binaryLenOriginalText
            count+= 1 
        self.paddingText= self.paddingText + binaryLenOriginalText
        self.lenPaddinText= len(self.paddingText)    
    def rotateR(self , record , bitsNum):
        lenRecord= len(record)
        if lenRecord == 0 or bitsNum < 0:
            print("invalid passing params")  
            return 
        if bitsNum == 0 or bitsNum % lenRecord == 0:
            return record
        val= ""    
        if bitsNum > lenRecord:
            index= -1 * (bitsNum % lenRecord)
            for i in range(index , 0 , 1):
               val+= record[i]    
            for i in range(0 , lenRecord + index , 1):
               val+= record[i]
        else:
            index= lenRecord - bitsNum 
            for i in range(index , lenRecord , 1):
               val+= record[i]    
            for i in range(0 , index , 1):
               val+= record[i]
        return val     
    def shiftR(self , record , bitsNum):
        lenRecord= len(record)
        lenRecord= len(record)
        if lenRecord == 0 or bitsNum < 0:
            print("invalid passing params")  
            return 
        if bitsNum == 0:
            return record
        if bitsNum > lenRecord: 
            res= ["0" for i in range(lenRecord)]
            return "".join(res) 
        val= ""
        for i in range(0 , bitsNum , 1):
            val+= "0" 
        for i in range(0 , lenRecord - bitsNum , 1): 
            val+= record[i]  
        return val   
    def maj(self , a , b , c):
        lenA= len(a)     
        lenB= len(b)
        lenC= len(c)
        if lenA == lenB == lenC:
            val= ""
            for i in range(0 , lenA , 1):
                count0= 0
                count1= 0
                if a[i] == "0":
                    count0+= 1
                else: 
                    count1+= 1 
                if b[i] == "0":
                    count0+= 1
                else: 
                    count1+= 1 
                if c[i] == "0":
                    count0+= 1
                else: 
                    count1+= 1
                if count0 > count1:
                    val+= "0"
                else:
                    val+= "1"   
            return val                   
        print("invalid passing records") 
    def ch(self , a , b , c):
        lenA= len(a)     
        lenB= len(b)
        lenC= len(c)   
        if lenA == lenB == lenC:
            val= ""
            for i in range(0 , lenA , 1):
                if a[i] == "1":
                    val+= b[i]
                else:
                    val+= c[i]    
            return val         
        print("invalid passing records")  
    def calcTerm(self , a , b , c):
        val= "" 
        for i in range(0 , 32 , 1):
           val+= str(int(a[i]) ^ int(b[i]) ^ int(c[i]))
        return "".join(val) 
    def calcRes(self , a , b , c , d):
        val= "" 
        for i in range(0 , 32 , 1):
           val+= str(int(a[i]) ^ int(b[i]) ^ int(c[i]) ^ int(d[i]))
        return "".join(val)    
    def checkLength(self , record):
        lenRecord= len(record) 
        while lenRecord != 32:
           record= "0" + record  
           lenRecord+= 1
        return record   
    def convertHashBunaryToHex(self):
        val= ""
        beg= 0 
        for i in range(0 , 64 , 1):
            slice= self.targetBinaryHash[beg : beg+4]
            val+= hex(int(slice , 2))[2 : ]
            beg+= 4
        return "".join(val)  
    def getHashCode(self):
        blocksBeg= 0
        internalBlocksBeg= 0 
        modules= 2**32
        for i in range(0 , int(self.lenPaddinText / 512), 1):
            slice= self.paddingText[blocksBeg : blocksBeg + 512]
            internalBlocks= [ ] 
            for j in range(0 , 16 , 1):
                internalBlocks.append(slice[internalBlocksBeg : internalBlocksBeg+32])
                internalBlocksBeg+= 32
            internalBlocksBeg= 0    
            for j in range(16 , 64 , 1):
                fTerm= self.calcTerm(self.rotateR(internalBlocks[j-2] , 17) , self.rotateR(internalBlocks[j-2] , 19) , self.shiftR(internalBlocks[j-2] , 10))
                sTerm= internalBlocks[j - 7]
                tTerm= self.calcTerm(self.rotateR(internalBlocks[j-15] , 7) , self.rotateR(internalBlocks[j-18] , 19) , self.rotateR(internalBlocks[j-15] , 3))
                foTerm= internalBlocks[j - 16]
                internalBlocks.append(self.calcRes(fTerm , sTerm , tTerm , foTerm))
            # a b c d e f g h
            # 0 1 2 3 4 5 6 7 
            for j in range(0 , 64 , 1):
                t1= int(self._8HashsRecords[7]) + int(self.calcTerm(self.rotateR(self._8HashsRecords[4] , 6) , self.rotateR(self._8HashsRecords[4] , 7) , self.rotateR(self._8HashsRecords[4] , 25)))
                t1+= int(self.ch(self._8HashsRecords[4] , self._8HashsRecords[5] , self._8HashsRecords[6]))
                t1+= (int(self._64ConstantsRecords[j]) + int(internalBlocks[j]))
                t1= bin(t1 % modules)[2 : ]
                t1= self.checkLength(t1)
                t2= bin((int(self.calcTerm(self.rotateR(self._8HashsRecords[0] , 2) , self.rotateR(self._8HashsRecords[0] , 13) , self.rotateR(self._8HashsRecords[0] , 32))) + int(self.maj(self._8HashsRecords[0] , self._8HashsRecords[1] , self._8HashsRecords[2]))) % modules)[2 : ]
                t2= self.checkLength(t2)
                self._8HashsRecords[7]= self._8HashsRecords[6]
                self._8HashsRecords[6]= self._8HashsRecords[5]
                self._8HashsRecords[5]= self._8HashsRecords[4]
                self._8HashsRecords[4]= bin((int(self._8HashsRecords[3]) + int(t1)) % modules)[2 : ]
                self._8HashsRecords[4]= self.checkLength(self._8HashsRecords[4])
                self._8HashsRecords[3]= self._8HashsRecords[2]
                self._8HashsRecords[2]= self._8HashsRecords[1]
                self._8HashsRecords[1]= self._8HashsRecords[0]
                self._8HashsRecords[0]= bin((int(t1) + int(t2)) % modules)[2 : ]
                self._8HashsRecords[0]= self.checkLength(self._8HashsRecords[0])
            blocksBeg+= 512 
        self.targetBinaryHash= ""  
        for i in range(0 , 8 , 1):
            self.targetBinaryHash+= self._8HashsRecords[i]
        return self.convertHashBunaryToHex()
obj= SHA256()   
obj= SHA256()   
obj.get8Constants(2 , 100)  
obj.get64Constants(2 , 1000) 
obj.setText("he'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififoififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfidhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififoififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfidhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififoififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfidhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififoififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfid")
print("the length of input text is: ")
print(len("he'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififoififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfidhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififoififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfidhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififoififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfidhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififoififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfididifififififkfifififhe'llhigififididififififififofofofififofofifkgkfidudjfjfid"))
hashVal= obj.getHashCode()
print(f"the length of output is {len(hashVal)}")
print(hashVal)
print("*********************")
obj.setText("h")
print(f"the length of input text is: {len('h')}")
hashVal= obj.getHashCode()
print(f"the length of output is {len(hashVal)}")
print(hashVal)   