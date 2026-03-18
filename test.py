class Machine:
    def print(self, document):
        raise NotImplementedError("Print not implemented!")

    def fax(self, document):
        raise NotImplementedError("Fax not implemented!")

    def scan(self, document):
        raise NotImplementedError("Scan not implemented!")