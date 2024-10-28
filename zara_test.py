from symbol_table import SymbolTable

# Initialize the symbol table
symbol_table = SymbolTable()

# Simulating Zara code with various data types and sub-programs

# Declare variables of different types
symbol_table.add_symbol("x", "integer", 10)
symbol_table.add_symbol("y", "float", 20.5)
symbol_table.add_symbol("name", "string", "ZaraLang")

# Declare an array (list in Python)
symbol_table.add_symbol("arr", "array", [1, 2, 3, 4, 5])

# Declare a stack (using a list to simulate a stack)
symbol_table.add_symbol("stack", "stack", [])

# Simulating updates in Zara code
symbol_table.update_symbol("x", 15)
symbol_table.update_symbol("y", 30.75)
symbol_table.update_symbol("name", "UpdatedZara")

# Retrieve the current stack (list) value
stack = symbol_table.retrieve_symbol("stack")['value']

# Push and pop operations on the stack
stack.append(1)  # Push
symbol_table.update_symbol("stack", stack)

stack.append(2)  # Push
symbol_table.update_symbol("stack", stack)

stack.pop()  # Pop a value
symbol_table.update_symbol("stack", stack)

# Retrieve variables and display their values
symbol_table.retrieve_symbol("x")
symbol_table.retrieve_symbol("y")
symbol_table.retrieve_symbol("name")
symbol_table.retrieve_symbol("arr")
symbol_table.retrieve_symbol("stack")

# Display the entire symbol table
symbol_table.display_table()
