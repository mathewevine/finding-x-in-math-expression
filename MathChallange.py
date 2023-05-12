def listToString(s):
   
    # initialize an empty string
    str1 = ""   
    # return string 
    return (str1.join(s))

def MathChallange(expression):
    result = None
    if expression[4] != "x": #If x presents left side of =
        for value in expression:
            if len(value) == 1: 
                if value == "x": 
                    indexx = expression.index(value)
                    for i in range(10):
                        expression[indexx] = i
                        result = eval(f'{expression[0]} {expression[1]} {expression[2]}')
                        if result == int(expression[-1]):
                            result = i
                            break
            else:
                value_list = []
                value_index = expression.index(value)
                for char in value:
                    value_list.append(char)
                
                for char in value_list:
                    indexx = value_list.index(char)
                    if char == "x":
                        for i in range(10):
                            value_list[indexx] = str(i)
                            convert_to_string = listToString(value_list)
                            expression[value_index] = convert_to_string
                            result = eval(f'{expression[0]} {expression[1]} {expression[2]}')
                            if result == int(expression[-1]):
                                result = i
                                break
    else: #If x presents right side of =
        result = eval(f'{expression[0]} {expression[1]} {expression[2]}')
        
    return result


print(MathChallange(input().split()))


