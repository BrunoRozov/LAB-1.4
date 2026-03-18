class Machine:
    def print(self, document):
        raise NotImplementedError("Print not implemented!")

    def fax(self, document):
        raise NotImplementedError("Fax not implemented!")

    def scan(self, document):
        raise NotImplementedError("Scan not implemented!")
    
class MultiFunctionPrinter(Machine):
    def print(self, document):
        print(f"Printing: {document}")

    def fax(self, document):
        print(f"Faxing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")


class OldFashionedPrinter(Machine):
    def print(self, document):
        print(f"Printing: {document}")

    def fax(self, document):
        pass # <-- ignoreei funksioon

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan!") # <-- lööb errori



printer = OldFashionedPrinter()

printer.print("Hello world")
printer.fax("Test document") 
printer.scan("Important document")