class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    @staticmethod
    def greet():
        print(":) Hey there , i hope you guys are doinn good ?")


data = [("Alice",120000, "Dev-A"), ("Bob",400000, "Dev-B"), ("Charlie",300000, "Dev-C")]
programmer_list = []

for name,salary,role in data:
    emp = Programmer(name,salary,role)
    programmer_list.append(emp)

    print(emp.name,emp.salary,emp.role,emp.company)
    emp.greet()

print("\n--- Verifying Saved Objects ---")
print(f"Total programmers hired: {len(programmer_list)}")
