'''
x = 10

def my_function():
    global x
    x = 20
    print("Trong hàm:", x)

my_function()
print("Ngoài hàm:", x)
'''
def greet(name,age = 30): 
    print("hello,"+ name + "!you are"+ str(age)+ "years old.")
greet("alice") # gọi hàm và bỏ qua đối số tham age