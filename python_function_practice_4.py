#Write a Python function called max_num()to find the maximum of three numbers.
#https://www.w3schools.com/python/module_math.asp
def max_num(x,y,z):
    return max([x,y,z])
print(max_num(5,10,15))    
print(max_num(0.5,1,1.5))   
print(max_num(1/2,1,1/7))   
print(max_num(0.0001,0.01,1.5))       
#Write a Python function called mult_list() to multiply all the numbers in a list.
#The len() function returns the number of items in an object.
#When the object is a string, the len() function returns the number of characters in the string.
#he math.prod() method returns the product of the elements from the given iterable

def mult_list(list):
 # if not items in the list
    if len(list)==0:
        return 0
 # start first item of the list       
    prod = list[0]    
# go thru the list items
    if len(list)>1:
        for i in list[1:]:
          prod = prod * i
    return prod           
print(mult_list([1,2,3,4,5,6]))
print(mult_list([]))
print(mult_list([2]))
print(mult_list([0]))

#Write a Python function called rev_string() to reverse a string.
#The fastest (and easiest?) way is to use a slice that steps backwards, -1.
#https://www.w3schools.com/python/python_howto_reverse_string.asp
def rev_string(string):
    return string[::-1]

txt = "Hello World"[::-1]
print(txt)    

#Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(x,a,b):
    return x in range(a,b+1)

#The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
   #Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.    
print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))


#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#code start with pascal()
triangle = [[1],[1,1]]
def pascal(n):
##your code here
    if n < 1: 
        print("need one row")
    elif n==1:
        print(triangle[0])
    else:
      row_number=2
      while len(triangle)< n:
          row=[]
          row_prev = triangle[row_number -1]
          ##length needs to be bigger than first row by 1
          length= len(row_prev)+1
          for i in range(length):
           if i ==0:
               row.append(1)    
           elif i>0 and 1 < length-1:
               row.append(triangle[row_number-1][i-1]
+ triangle[row_number-1][i])
      else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    ##print triangle
    for row in triangle:
     print(row)

pascal(2)
pascal(5)               


   #def generate(self, numRows:int)-> List[List[int]]:
        #res=[[1]]
        #for i in range(numRows -1):
            #temp=[0]+res[-1]+[0]
            #row=[]
            #for j in range(len(res[-1])+1):
                #row.append(temp[j]+temp[j+1])
            #res.append(row)
        #return res        