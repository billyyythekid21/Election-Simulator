class Candidate:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.votes = []

    def __str__(self):
        return f"Candidate Name: {self.name}\nParty: {self.party}"
    
    def __hash__(self):
        return hash((self.name, self.party))

    def __eq__(self, other):
        return isinstance(other, Candidate) and self.name == other.name and self.party == other.party

    def __repr__(self):
        return f"{self.name} ({self.party})"