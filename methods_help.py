# def greetings(name):
#   print("hello " + name)
def method_help():
  # pass (pass is used when thre's no code, but it wont give you an error)
  dic = {"key1": 100, "key2":200}
  dic.popitem()
  a = dic.popitem()
  print(a)
########################################################################################################################
  # Methods, Help & Documentation Practice #1
  # Remove the characters to the left of our main text:
  
  # ,
  
  # :
  
  # %
  
  # _
  
  # #
  
  # Use the lstrip() method. Print the result to the screen:
  
  # ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"
  
  # Search the documentation for the requested method to learn how it works. You can use intermediate variables if you need them.

word = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"



print(",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#".lstrip(",:%_#"))






########################################################################################################################
  # Methods, Help & Documentation Practice #2
  # Add the element "orange" as the fourth element of the following list fruits, using the insert() method:
  
fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
  
  # Search the documentation for the requested method to know how it works.

fruits.insert(3, 'orange')

print(fruits)





########################################################################################################################
  #   Methods, Help & Documentation Practice #3
  # Check if the sets below are isolated (that is, they have no elements in common), using the isdisjoint() method. Store this result in the isolated_sets variable:
  
phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}
  # Search the documentation for the requested method to know how it works.

print(phone_brands.isdisjoint(tv_brands))