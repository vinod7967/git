"""Importing sys & datetime modules"""
import datetime

import math
def output(exp_lst):
    """Prints the output data"""
    print("\nDate", datetime.date.today())
    print("Time", datetime.datetime.now().strftime("%H:%M:%S"))
    print("E X P E N D I T U R E S  T A B L E".ljust(41, " "))
    print("-" * 50)
    print("SALARY".ljust(40, " "), ":", SALARY, "/-")
    print("-" * 50)
    for j in DICT:
        if exp_lst.count(j) > 1:
            print(j,"-",exp_lst.count(j)," "*(40-len(j)-len(str(exp_lst.count(j)))-4),":",DICT[j])
        else:
            print(j, " " * (40 - len(j) - 1), ":", DICT[j])
    print("-" * 50)
    print("TOTAL_EXP".ljust(40, " "), ":", TOTAL_EXP, "/-")
    print("Balance".ljust(40, " "), ":", SALARY - TOTAL_EXP, "/-")
    
    
def exp_dict_update(exp_n, exp_a):
    """Return the updated Dictionary"""
    global SALARY_BALANCE, DICT, TOTAL_EXP
    if exp_n in DICT:
        DICT[exp_n] = DICT[exp_n] + exp_a
        SALARY_BALANCE -= exp_a
        TOTAL_EXP += exp_a
    else:
        DICT[exp_n] = exp_a
        SALARY_BALANCE -= exp_a
        TOTAL_EXP += exp_a
        
        
def exp_dict(exp_n, exp_a):
    """Validating of Inputs & Updating Dictionary"""
    global LST_OF_EXP, SALARY_BALANCE
    try:
        if exp_a > SALARY_BALANCE:
            print("\nExpenditure exceeded your SALARY amount:")
            #exp_dict_update(exp_n, exp_a)
            raise Exception
        else:
            exp_dict_update(exp_n, exp_a)
            return True
    except:
        output(LST_OF_EXP)
        print("\nSystem is terminating. Thankyou!")
        return False


def validate(Input):
    while True:
        try:
            value = float(input(f"ENTER YOUR {Input}:: "))
            if value < 0:
                raise Exception
            else:
                return value
                break
        except:
            print("ENTER VALID INPUT")
            
    
if __name__ == "__main__":
    TOTAL_EXP = 0
    DICT = {}
    LST_OF_EXP = []
    SALARY = validate("SALARY")
    SALARY_BALANCE = SALARY
    VALIDITY = True
    while VALIDITY:
        exp_name = input("ENTER YOUR EXPENDITURE NAME: ").lower()
        LST_OF_EXP.append(exp_name)
        exp_amt = validate("AMOUNT")
        valid = exp_dict(exp_name,exp_amt)
        if not valid :
            break
        while VALIDITY:
            try:
                opt = input("YOU WANT INSERT ONE MORE RECORD? [yes|no]:").lower()
                if opt == ("yes" or "y") :
                    break
                elif opt == ('no' or "n"):
                    output(LST_OF_EXP)
                    VALIDITY = False  
                else:
                    raise Exception
            except:
                print("Enter valid Option [either 'yes' or 'no']: ")
                
                