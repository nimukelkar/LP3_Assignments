

'''class Knapsack:

    def __init__(self):
        self.val=[2,3,1,4]
        self.wt=[3,4,6,5]
        self.val.insert(0,0)
        self.wt.insert(0,0)
        self.target=9
        self.m=len(self.val)
        self.n=self.target+1

        self.table = []

        for i in range(self.m):
            l = [0] * (self.n)
            self.table.append(l)
        for i in range(1,self.m):
            for j in range(1,self.n):
                rem=j-self.wt[i]
                if rem>=0:
                    self.table[i][j]=max(self.table[i-1][j],self.val[i]+self.table[i-1][rem])
                else:
                    self.table[i][j]=self.table[i-1][j]

        print(self.table[self.m-1][self.n-1])

    def display(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.table[i][j],end=" ")
            print()

k=Knapsack()
k.display()'''



class Solution:

    def __init__(self):
        self.n=7
        self.wt=[0,1,3,4,5]
        self.value=[0,1,4,5,7]
        self.table=[]
        l=[]
        for i in range(len(self.wt)):
            l=[0]*(self.n)
            self.table.append(l)
        print(self.table)
    def compute(self):
        m=len(self.value)


        for i in range(m):
            for j in range(self.n):
                if j<self.wt[i]:
                    self.table[i][j]=0
                else:
                    rem = j - self.wt[i]
                    self.table[i][j]=max(self.table[i-1][j],self.value[i]+self.table[i-1][rem])
    def display(self):
        for i in range(len(self.value)):
            for j in range(self.n):
                print(self.table[i][j],end=" ")
            print()
s=Solution()
s.compute()
s.display()





























