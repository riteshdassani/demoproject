# li=['ritesh','dabba']
# print (li)
#
#
# tuplex=tuple(li)
#
# print(tuplex)

class MyClass:
  # x = 5
  # my_dict={1:"brad pitt",2:"tom hnks"}
  # def my_function(self):
  #
  #     print("Hello from a function")
  #     print(MyClass.x)
  #     print(MyClass.my_dict)

  def list_function(self):
      a = [x ** 2 for x in range(1, 11)]
      print(a)

  def dict_function(self):
      key=[1,2,3,4,5]
      values=['jack','bradpitt','angelina','samanta','elen']
      dict=(zip(key,values))
      a={k:v for (k,v) in dict if k%2==1}
      print(a.values())
      s=a.values()
      str='ing'
      my_New=[x + str for x in s]
      print(my_New)
p1 = MyClass()
p1.list_function()
p1.dict_function()
