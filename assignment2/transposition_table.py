class TranspositionTable(object):
# Table is stored in a dictionary, with board code as key, 
# and minimax score as the value

    # Empty dictionary
    def __init__(self):
        self.table = {}

    # Used to print the whole table with print(tt)
    def __repr__(self):
        return self.table.__repr__()
        
    def storeScore(self, code, score):
        if self.lookup(code) == None:
            self.table[code] = [score, None]
        else:
            self.table[code][0] = score

    def storeMove(self, code, move):
        if self.lookup(code) == None:
            self.table[code] = [None, move]
        else:
            self.table[code][1] = move
    
    # Python dictionary returns 'None' if key not found by get()
    def lookup(self, code):
        return self.table.get(code)
