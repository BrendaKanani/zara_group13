class SymbolTable:
    def __init__(self):
        # Initialize an empty dictionary to store symbols
        self.table = {}

    def add_symbol(self, name, data_type, value):
        """Adds a symbol to the table."""
        if name in self.table:
            raise Exception(f"Error: Symbol '{name}' already exists.")
        self.table[name] = {"type": data_type, "value": value}
        print(f"Symbol added: {name} => Type: {data_type}, Value: {value}")

    def update_symbol(self, name, value):
        """Updates the value of an existing symbol."""
        if name not in self.table:
            raise Exception(f"Error: Symbol '{name}' not found.")
        old_value = self.table[name]["value"]
        self.table[name]["value"] = value
        print(f"Symbol updated: {name} => Old Value: {old_value}, New Value: {value}")

    def retrieve_symbol(self, name):
        """Retrieves a symbol from the table."""
        if name in self.table:
            symbol = self.table[name]
            print(f"Retrieved Symbol: {name} => Type: {symbol['type']}, Value: {symbol['value']}")
            return symbol
        else:
            raise Exception(f"Error: Symbol '{name}' not found.")

    def display_table(self):
        """Displays the entire symbol table."""
        print("\nCurrent Symbol Table:")
        for name, details in self.table.items():
            print(f"{name} => Type: {details['type']}, Value: {details['value']}")
