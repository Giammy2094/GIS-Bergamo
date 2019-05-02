##Transportation assignment 2019
##Borgopalazzo group
##Frank-Wolfe algorithm to solve DUE using the Bureau of Public Roads function (1964)

def fw():
    #insert input values
    v = float(input("Insert number of vehicles: ")) #traffic to be assigned
    q1 = float(input("Insert value of capacity 1: ")) #capacity route 1
    q2 = float(input("Insert value of capacity 2: ")) #capacity route 2
    a = float(input("Insert value of alpha: ")) #alpha Bureau function
    b = float(input("Insert value of beta: ")) #beta Bureau function
    tf1 = float(input("Insert free float time 1: ")) #free float time route 1
    tf2 = float(input("Insert free float time 2: ")) #free float time route 2

    #initialize variables
    v1 = 0.0
    v2 = 0.0
    t1 = 10.0 # a random value bigger than 0.1 in order to start the cicle
    t2 = 0.0
    cont = 0

    #repeat iteration until difference between time is low
    while abs(t1 - t2) > 0.1: # times are float, hence to stop the cicle a treshold is needed
        t1 = tf1 * (1 + a * (v1 / q1) ** b) #Bureau function
        t2 = tf2 * (1 + a * (v2 / q2) ** b)
        w1 = 0.0 #initialize weight
        w2 = 0.0
        if t1 < t2: # condition to assign weights
            w1 = v
        else:
            w2 = v
        cont += 1 #increment the counter
        v1 = v1 + (1 / cont) * (w1 - v1) #assign new traffic volume to each route
        v2 = v2 + (1 / cont) * (w2 - v2)
        print("iteration n, v1, v2: ", cont, v1, v2)
    return cont,v1,v2,t1,t2

#main
cont,v1,v2,t1,t2 = fw()
print("-"*50)
print("Quantity 1: ",v1," ","Quantity 2: ",v2," ","Time 1: ",t1," ","Time 2: ",t2)
print("Iterations: ", cont)