
temp_count = 0
label_count = 0

def new_temp():
    global temp_count
    temp = f"t{temp_count}"
    temp_count += 1
    return temp

def new_label():
    global label_count
    label = f"L{label_count}"
    label_count += 1
    return label


def parse_expression(tokens):
    """
    Handles expressions like a + b * c.
    """
    if len(tokens) == 3:
        left, op, right = tokens
        temp = new_temp()
        code = f"{temp} = {left} {op} {right}"
        return {"code": code, "place": temp}
    else:
       
        return {"code": "", "place": tokens[0]}

def parse_while(condition_code, body_code):
    """
    Generates intermediate code for while loops.
    """
    start_label = new_label()
    end_label = new_label()
    code = [
        f"{start_label}:",
        condition_code["code"],
        f"IF_FALSE {condition_code['place']} GOTO {end_label}",
        body_code["code"],
        f"GOTO {start_label}",
        f"{end_label}:"
    ]
    return "\n".join(code)

def parse_function(name, body_code):
    """
    Generates intermediate code for function definitions.
    """
    func_label = f"FUNC_{name}"
    code = [
        f"{func_label}:",
        body_code["code"],
        "RETURN"
    ]
    return "\n".join(code)


expression_code = parse_expression(["a", "+", "b"])
print("Expression Intermediate Code:")
print(expression_code["code"])

condition_code = parse_expression(["i", "<", "10"])  
body_code = parse_expression(["i", "+", "1"])  
while_code = parse_while(condition_code, {"code": body_code["code"]})
print("\nWhile Loop Intermediate Code:")
print(while_code)


function_code = parse_function("myFunction", {"code": expression_code["code"]})
print("\nFunction Intermediate Code:")
print(function_code)
