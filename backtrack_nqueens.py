

'''class NQueens:

    def __init__(self):
        self.n=8
        self.sol=[None]*(self.n)
        self.value=[0,1,2,3,4,5,6,7]

    def checkpast(self,index,c):
        if(self.sol):
            for v in range(index):
                if(self.sol[v]==c):
                    return False
                if(c-self.sol[v]==index-v):
                    return False
                if(self.sol[v]-c==index-v):
                    return False

        return True


    def dfs_visited(self,index):
        #Exit condition
        if(index==self.n):
            return True
        for c in (self.value):
            #Check past
            if(self.checkpast(index,c)):
                self.sol[index]=c
                if(self.dfs_visited(index+1)):
                    return True
                else:
                    continue
        self.sol[index]=None
        return False


    def dfs(self):
        self.dfs_visited(0)
        return

obj=NQueens()
obj.dfs()
print(obj.sol)'''

#CSP for nqueens.



'''class NQueens:
    def __init__(self):
        self.n=8
        self.value=[0,1,2,3,4,5,6,7]
        self.sol=[None]*(self.n)

    def checkpast(self,index,c):
        if(self.sol):
            for v in range(index):
                if(self.sol[v]==c):
                    return False
                if(self.sol[v]-c==index-v):
                    return False
                if(c-self.sol[v]==index-v):
                    return False


        return True


    def dfs_visited(self,index):
        #Exit condition.
        if(self.n==index):
            return True
        for c in self.value:
            #Check past
            if(self.checkpast(index,c)):
                self.sol[index]=c
                if(self.dfs_visited(index+1)):
                    return True
                else:
                    continue
        #Backtrack
        self.sol[index]=None
        return False



    def dfs(self):
        self.dfs_visited(0)
        return
n=NQueens()
n.dfs()
print("****************The configuration of the NQueens Chessboard is***********")
print(n.sol)'''




class NQueens:
    def __init__(self):
        self.n=4
        self.val=[0,1,2,3]
        self.sol=[None]*(self.n)

    def checkpast(self,index,c):
        if self.sol:
            for v in range(index):
                if self.sol[v]==c:
                    return False
                if index-v==c-self.sol[v]:
                    return False
                if index-v==self.sol[v]-c:
                    return False
        return True
    def dfs_visited(self,index):
        if index==self.n:
            return True
        for c in self.val:
            if self.checkpast(index,c):
                self.sol[index]=c
                if self.dfs_visited(index+1):
                    return True
                else:
                    continue
        self.sol[index]=None
        return False
    def dfs(self):
        self.dfs_visited(0)

n1=NQueens()
n1.dfs()
print(n1.sol)
































