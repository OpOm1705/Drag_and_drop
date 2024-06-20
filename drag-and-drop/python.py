

# n = int(input("entyer the number : "))
# sum = 0 
# def sum_cal(n):
#     if(n==0):
#         return 0
#     return sum_cal(n-1) + n
    

# sum = sum_cal(n)
# print(sum)


# list  = ("ram" , "shyam" , "naman")
# x = len(list)-1
# def mfsl(list , x):
#     if(x == -1):
#          return
#     mfsl(list , x-1) 
#     print(list[x]) 



# mfsl(list , x)


# f = open("practice.txt" , "a")

# f.write("hi everyone \n we are learining i/o" )


# print(f.read())



# q = "learning"
# line_num = 1
# with open("practice.txt" , "r") as f:
#     data = True
   
#     while  data:
#         data = f.readline()
#     # print(data)
#         if( q in data):
#             print(line_num)
#         else :
#             line_num += 1

   


# with open("practice.txt" , "r") as f :
#     data = f.read()
#     print(data)

#     num =""
#     list = []

#     for i in range(len(data)) :
#         if (data[i] == ","):
#             print("number is ",num)
#             list.append(num)
#             num = ""
#         else :
#             num += data[i]
    
#     print(list)

#     count = 0
#     i = 0
#     while i < len(list) :
#         if(int(list[i])%2 == 0) :
#             count +=1
#             i +=1
#         else:
#             i+=1
#     print(count)
# with open("practice.txt" , "r") as f :
#     data = f.read()
#     print(data)

#     list = data.split(',')
#     print(list)
#     i = 0
#     l = len(list)
#     while i < l :
#         list[i] = int(list[i])
#         i +=1
    
#     print(list)





# class Student :

#     def __init__(self , fullname):
#         self.name = fullname
#         self.sub  = "maths"


# s1 = Student("karan")

# print(s1.name)


# class Student :

#     def __init__(self , name , m1):
#         self.name = name
#         self.m1 = m1
        
    
#     def cal_avg(self):
#         sum = self.m1[0] + self.m1[1] + self.m1[2]
#         avg = sum/3
#         return avg 


# m1 = [4,5,7,4]
# s1 = Student("karan" , m1)
# # s2 = Student("omp" , 3,5,9)

# print(s1.cal_avg())
# # print(s2.cal_avg())







# class Account :

#     def __init__(self  , acc_no , balance):
#         self.acc_no = acc_no
#         self.balance = balance

#     def details_method(self , debit , credit) :
#         self.debit = debit
#         self.credit = credit 
#         self.balance = self.balance - self.debit + self.credit

#         print(self.balance)


# c1 = Account(101 , 1000)

# c1.details_method(100 , 1001)






# class circle : 
#     def __init__(self , radius):
#         self.radius = radius 

#     def cal_area (self) :
#         area = self.radius * self.radius * 3.14
#         return area

#     def cal_peri (self) :
#         peri = 2 * 3.14 * self.radius 
#         return peri



# c1 = circle(1)

# permimeter = c1.cal_peri()
# print(permimeter)

# print(c1.cal_area())






# class Employee :

#     def __init__(self , role , dep , salary):
#         self.role = role
#         self.dep = dep
#         self.salary = salary

    
#     def show_details(self):
#         print("role :" , self.role)
#         print("department :", self.dep)
#         print("salary :" , self.salary)


# class Engineer(Employee) :

#     def __init__(self , name , age):
#         self.name = name 
#         self.age = age 
#         super().__init__("engineer" , "it" , "2000")


#     # def show_details(self):
#     #     print(self.name , self.age)
#     #     super().__init__("engineer" , "it" , "2000")

# e1 = Employee("data analyst" , 1 , 1000)

# # e1.show_details()

# e2 = Engineer("omp" , 20)

# e2.show_details()






class order :

    def __init__(self , item , price):
        self.item = item 
        self.price = price 

    
    def __gt__(self , order1) : 
        if(self.price > order1.price):
            return True
        else : 
            return False



order1 = order(1 ,5)
order2 = order(2 , 10)

print(order1 > order2)
