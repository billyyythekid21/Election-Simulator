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
        print("\n-------------->")
        print("Running Election...")
        print("-------------->\n")
        for electorate in self.electorates:
            winner = electorate.run_election()
            self.results[winner.party] += 1

        print("\n---------------")
        print("Election Results:")
        print("---------------")
        for party, seats in self.results.items():
            print(f"{party.name}: {seats} seats")
        print(f"Winner: {winner.party}")
        print("---------------\n")
        return self.results
    
election = Election()

party_a = Party("Right Party")
party_b = Party("Left Party")

candidate_1 = Candidate("Alice", party_a)
candidate_2 = Candidate("Bob", party_b)

electorate_1 = Electorate("Menzies", {candidate_1: candidate_1, candidate_2: candidate_2})

ballots_1 = [
    [candidate_1, candidate_2],
    [candidate_2, candidate_1],
    [candidate_1, candidate_2],
    [candidate_2, candidate_1],
    [candidate_2, candidate_1],
]

electorate_1.distribute_votes(ballots_1)

election = Election()

election.add_party(party_a)
election.add_party(party_b)
election.add_electorate(electorate_1)

results = election.run_election()