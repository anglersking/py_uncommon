from dataclasses import dataclass


@dataclass
class Test_struct:
    name:str
    age:str
if __name__ == "__main__":
    T1=Test_struct("xiao",18)
    T2=Test_struct("xiao",18)
    print(T1)
    print(T1==T2)
    T1.name="ming"
    print(T1.name)
    
