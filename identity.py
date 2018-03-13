class linearCombination:
    def __init__(self):
        self.mat=[[1,2,3,4],[5,6,7,8],[12,3,4,2],[12,4,5,6]]
        self.w=[[-6],[-2],[2],[3]]
    def call(self,k,x,l):
        for i in range(len(self.mat)):
           for j in range(len(self.mat)):
               if(k==i and x!=j):
                   self.mat[i][j]=self.mat[i][j]/l                   
                   print("div",self.mat)
    def set(self,i,j):
        l=[None for i in range(len(self.mat))]
        for i1 in range(len(self.mat)):
            for j1 in range(len(self.mat)):
                if(i==i1):
                    l[j1]=self.mat[i1][j1]
        return l
    def call2(self,i,j):
        for i1 in range(len(self.mat)):
            l1=self.set(i,j)
            w=self.w[i][0]
            for j1 in range(len(self.mat)):
                if(j ==j1 and i!=i1):
                    xx=1
                    r=self.mat[i1][j1]
                    l=[x*r for x in l1]
                    l1=l1[j1]
                    if(xx==1):
                        w1=self.w[i1][0]
                        w=w*r
                        w1=w1*l1
                        self.w[i1][0]=w1-w
                    xx=xx+1
                    for x2 in range(len(self.mat)):
                        self.mat[i1][x2]=l1*self.mat[i1][x2]-l[x2]
                        

    def Identiry(self):
        for i in range(len(self.mat)):
            x=0
            for j in range(len(self.mat)):               
                    if((j)==i):
                        print("time",self.mat)
                        x=j
                        l=self.mat[i][j]
                        self.mat[i][j]=self.mat[i][j]/l
                        self.w[i][0]=self.w[i][0]/l
                        k=i
                        self.call(i,j,l)
                        self.call2(i,j)                                    
        print(self.mat)
        print(self.w)              
l=linearCombination()
print(l.Identiry())



