from candidate import Candidate
from party import Party
from electorate import Electorate
import menu

class Election:
    def __init__(self):
        self.electorates = []
        self.parties = []
        self.results = {}

    def add_electorate(self, electorate: Electorate):
        self.electorates.append(electorate)

    def add_party(self, party: Party):
        self.parties.append(party)
        self.results[party] = 0

    def run_election(self):
        print("Running Election...")
        for electorate in self.electorates:
            winner = electorate.run_election()
            self.results[winner.party] += 1

        print("\nElection Results:")
        for party, seats in self.results.items():
            print(f"{party.name}: {seats} seats")
        return self.results
    
election = Election()

party_a = Party("Party A")
party_b = Party("Party B")

alice = Candidate("Alice", party_a)
bob = Candidate("Bob", party_b)

electorate_1 = Electorate("Electorate 1", {alice: alice, bob: bob})

ballots = [
    [alice, bob],
    [bob, alice],
    [alice, bob],
]

electorate_1.distribute_votes(ballots)

election = Election()

election.add_party(party_a)
election.add_party(party_b)
election.add_electorate(electorate_1)

results = election.run_election()