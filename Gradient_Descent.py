import matplotlib.pyplot as plt


def function(x):
    return (x+3)**2
def grad(x):
    return 2*(x+3)


value=[]
n=100
learning_rate=0.1
x=2

n=100
for i in range(n):
    value.append(function(x))
    gradient=grad(x)
    x-=learning_rate*gradient
plt.plot(value)
plt.show()
