def main():
    workhours = int(input('Enter your work hours: '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

   ##################################################
   # Code your program here
   ##################################################
    if workhours - reg_hours > 0:
        overtime = workhours - reg_hours
        workhours = 40
    else: 
        overtime = 0
    overtime_wage = overtime * ov_rate
    regular_wage = workhours * reg_rate
    total_wage = regular_wage + overtime_wage

    print(f"Regular hours: {workhours} Regular Charge: {regular_wage}")
    print(f"Overtime hours: {overtime} Overtime Charge: {overtime_wage:.2f}")
    print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
