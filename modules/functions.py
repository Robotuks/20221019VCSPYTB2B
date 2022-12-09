
def hello():
    print('Hello from Python module')


# this runs only if you start running code from this file
if __name__ == '__main__':
    x = 5 
    y = 3 + x
    print('x + y =', x+y)
    hello()
    print ('script end')