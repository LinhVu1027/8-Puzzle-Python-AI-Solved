import Queue as Q
import math
def insert(arr):
    a=[]
    for i in arr:
        a.append(i)

    return a
def up(arr):
    l=len(arr)
    x=int(math.sqrt(l))
    #print x
    for i in range(l):
        if(arr[i]==0):
            if(i/x==0):
                return arr;
            t=arr[i];
            arr[i]=arr[i-x];
            arr[i-x]=t
            return arr
def down(arr):
    l=len(arr)
    x=int(math.sqrt(l))
    for i in range(l):
        if(arr[i]==0):
            if(i/x==x-1):
                return arr
            t=arr[i];
            arr[i]=arr[i+x];
            arr[i+x]=t
            return arr
def left(arr):
    l=len(arr)
    x=int(math.sqrt(l))
    for i in range(l):
        if(arr[i]==0):
            if(i%x==0):
                return arr;
            t=arr[i];
            arr[i]=arr[i-1];
            arr[i-1]=t
            return arr
def right(arr):
    l=len(arr)
    x=int(math.sqrt(l))
    for i in range(l):
        if(arr[i]==0):
            if(i%x==x-1):
                return arr
            t=arr[i];
            arr[i]=arr[i+1];
            arr[i+1]=t
            #print arr    
            return arr
def misplaced(arr,goal):
    c=0
    l=len(arr)
    for i in range(l):
        if(arr[i]!=goal[i] and arr[i]!=0):
            c=c+1;
    return c;        
            
visited=[]
path=[]
l=[];
ini=[1,2,3,4,8,0,7,6,5]
goal=[1,2,3,4,5,6,7,8,0]
visited.append(ini);
path.append(ini);

q=Q.PriorityQueue()
x=misplaced(ini,goal)
l.append(x)
l.append(0)
l.append(ini)
q.put(l)
l=[]
v=[]
f=0
#print q.queue
#print q.get()

while not q.empty():
    l=q.get()
    arr=l[2]
    f=l[1]
    if(arr==goal):
        visited.append(goal)
        print "goal reached"
        break;
    #print arr
    if l[2] not in visited:
        
      visited.append(l[2]);
    arr2=insert(arr)
      
    arr1=up(arr2)
    """print "up"
    print arr
    print arr2"""
    
    if((arr==arr1)== False):
        #print "a"
        z=misplaced(arr1,goal)
        f=f+1
        v.append(z+f)
        v.append(f)
        v.append(arr1)
        q.put(v)
        #print v
        v=[]
        f=f-1
        #print q.queue
    arr2=insert(arr)    
    arr1=down(arr2);
    """print "down"
    print arr
    print arr2"""
    if(arr!=arr1):
        z=misplaced(arr1,goal)
        f=f+1
        v.append(z+f)
        v.append(f)
        v.append(arr1)
        q.put(v)
        v=[]
        f=f-1
        #print q.queue
    arr2=insert(arr)
    arr1=left(arr2)
    """print "left"
    print arr
    print arr2"""
    if(arr1!=arr):
        z=misplaced(arr1,goal)
        f=f+1
        v.append(z+f)
        v.append(f)
        v.append(arr1)
        q.put(v)
        v=[]
        f=f-1
    arr2=insert(arr)

    arr1=right(arr2)
    #print "right"
    #print arr
    #print arr2
    if(arr1!=arr):
        z=misplaced(arr1,goal)
        f=f+1
        v.append(z+f)
        v.append(f)
        #print arr1
        v.append(arr1)
        q.put(v)
        v=[]
        f=f-1
    #print q.queue    
    l=[]  
print visited        
        
         
          
    
        
        

    
    
    
