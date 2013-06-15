def sign(n):
    '''Returns the sign of n'''

    if n < 0:
        return -1
    else:
        return 1

def braid_form(perm):

    '''Returns the braid form of an Ubercrossing with Sn representation perm'''

    braid = []
    n = len(perm)
    for i in range(n):
        k = (2*i) % n
        for l,j in enumerate(range(1,n,2)):
            braid.append(-(l+1)*sign(perm[k]-perm[(k+j)%n]))

    return 'braid['+str(braid)[1:-1]+'](0,0)(1,0)'

def reverse(n):

    '''Reverses a list (just for fun?)'''
   
    lst = []
    for i in range(n):
        lst.append(n-i)
    return lst

def permutations(n):

    '''Returns all elements of Sn which begin with '1'. Note that any other
    permutations would just be repetitive as uebercrossing representations.'''

    master = [[]]
    master1 = []
    while reverse(n) not in master:
        for j, lst in enumerate(master):
            for i in range(1, n+1):
                if i not in lst:
                    master.append(lst+[i])
    for j, lst in enumerate(master):
        if len(lst) == n and lst[0] == 1:
            master1.append(lst)
    return master1

if __name__ == "__main__":

    m = 7 #The size of the permutation(s) under consideration.

    #The knots up through 10 crossings are stored in a file called knots.txt
    knots = []
    f = open('knots.txt', 'r')
    for line in f:
        if line.strip() != '':
            knots.append(str(line).strip()) #stores the knots as a list.
    f.close()

    masterlst = permutations(m) #The elements of Sm
    allknots = [] #A list of all knots with an ubercrossing rep in Sm.
    for perm in masterlst: #'finds the knot of each permutation in masterlst
        lst = braid_form(perm) #first convert the permutation to a braid
        M = Manifold(lst) #this allows you to work with the knot complement
        try:
           for i,k in enumerate(knots): #goes thorugh the list of knots
              if Manifold(k).volume() > 0 and M.is_isometric_to(Manifold(k)):
                    print perm, k #finds a knot isometric to the braid
                    if k not in allknots: #adds the knot to the big list.
                        allknots.append(k)
                    break
        except RuntimeError: #I forget why this might happen.
              print perm
              continue
        except IOError: #I forget why this also might happen.
              print knots[i+1]
              continue

    print allknots #prints all hyperbolic knots with an m-uerbercrossing.
