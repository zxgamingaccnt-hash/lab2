def calculate_bmi(height,weight):
    print("value of height is :",height,"m")
    print(f"value of weight is: {weight}kg")
    bmi=weight/(height**2)
    print("bmi is",bmi)
    if bmi <18.5:
            print("bmi is underweight")
            value = -1
    elif bmi >=18.5 and bmi<24.9:
            print("BMI is normal")
            value= 1 
    else:
            print("bmi is overweight")
            value=1
    return [bmi,value]

def display_main_menu():
    print()
def get_user_input():
    print()

def main():
    print(calculate_bmi(1.8,55))
    


if __name__=="__main__":
      main()



