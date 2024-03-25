
def print_values(*args):
    for arg in args:
        print(arg)
def print_valuess(**args):
    for key,values in args.items():
        print(key,values)

def name_age(name,age):
    print(name,age)

numbers=[1,2,3,4,5]
first,*rest=numbers
print(first,rest)
print_values(numbers)
print_valuess(nu=numbers)
alice=('heihie',1)
name_age(*alice)
h={
    'name':'wo',
    'age':10
}
name_age(**h)


