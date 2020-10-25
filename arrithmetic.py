def arithmetic_arranger(problems, showAns = False):
    if len(problems)>5:
      return 'Error: Too many problems.'
        
    arranged_problems=[]
    firstline = ""
    secondline = ""
    line = ""
    result = ""
    prob_len = len(problems)
    iterator = 0
    
    for i in problems:
      x = i.split()
      num1 = x[0]
      num2 = x[2]
      operation = x[1]
      iterator +=1

      if operation not in ["-","+"]:
        return "Error: Operator must be '+' or '-'."
      else:
        for i in num1:
           if i not in ["1","2","3","4","5","6","7","8","9","0"]:
             return "Error: Numbers must only contain digits."
           else:
              continue
        
        for i in num2:
           if i not in ["1","2","3","4","5","6","7","8","9","0"]:
             return "Error: Numbers must only contain digits."
           else:
              continue
         

      if len(num1)>4 or len(num2)>4:
            return "Error: Numbers cannot be more than four digits."

      else:
            
            width = max(len(num1), len(num2))+2
            firstline += str(num1).rjust(width) + ("    " if iterator != prob_len else "")
            
            secondline += operation + str(num2).rjust(width-1) + ("    " if iterator != prob_len else "")
            
            line += str("-"*width) + ("    " if iterator != prob_len else "")
            
           
      if showAns == True:
              if operation == "+":
                result += str(int(num1) + int(num2)).rjust(width) + ("    " if iterator != prob_len else "")
                
              elif operation == "-":
                result += str(int(num1) - int(num2)).rjust(width) + ("    " if iterator != prob_len else "")
                
              
              arranged_problems = (firstline + "\n" + secondline + "\n" + line +  "\n" + result )
      else:
              arranged_problems = (firstline + "\n" + secondline + "\n" + line )
    
    
    return print(arranged_problems)

arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True)