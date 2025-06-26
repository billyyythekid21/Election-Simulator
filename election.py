import matplotlib.pyplot as pyplot
from candidate import Candidate
from party import Party
from electorate import Electorate

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
            winner: Candidate = electorate.run_election()
            self.results[winner.party] += 1

        print("\n---------------")
        print("Election Results:")
        print("---------------")
        for party, seats in self.results.items():
            print(f"{party.name}: {seats} seats")
        print(f"Winner: {winner.party}")
        print("---------------\n")

        party_names = []
        seat_counts = []

        for party, seats in self.results.items():
            party_names.append(party.name)
            seat_counts.append(seats)

        pyplot.figure(figsize=(10, 6))
        pyplot.bar(party_names, seat_counts, color='skyblue')
        pyplot.xlabel('Parties')
        pyplot.ylabel('Seats Won')
        pyplot.title('Election Results - Seat Distribution')
        pyplot.tight_layout()
        pyplot.show()
        print(pyplot.get_backend())
        return self.results
    
    def run_example_election(self):
        election = Election()

        party_a = Party("Right")
        party_b = Party("Left")
        party_c = Party("Centre")
        party_d = Party("Alternative")

        candidate_1 = Candidate("Alice", party_a)
        candidate_2 = Candidate("Bob", party_b)
        candidate_3 = Candidate("Charlie", party_c)
        candidate_4 = Candidate("David", party_d)
        candidate_5 = Candidate("Eve", party_a)
        candidate_6 = Candidate("Frank", party_b)

        electorate_1 = Electorate("Menzies", {
            candidate_1: candidate_1,
            candidate_2: candidate_2,
            candidate_3: candidate_3,
            candidate_4: candidate_4,
            candidate_5: candidate_5,
            candidate_6: candidate_6
        })

        electorate_2 = Electorate("Chisholm", {
            candidate_1: candidate_1,
            candidate_2: candidate_2,
            candidate_3: candidate_3,
            candidate_4: candidate_4,
            candidate_5: candidate_5,
            candidate_6: candidate_6
        })

        ballots_1 = [
            [candidate_1, candidate_2, candidate_3, candidate_4, candidate_5, candidate_6],
            [candidate_2, candidate_1, candidate_3, candidate_4, candidate_5, candidate_6],
            [candidate_3, candidate_4, candidate_1, candidate_2, candidate_5, candidate_6],
            [candidate_4, candidate_3, candidate_2, candidate_1, candidate_5, candidate_6],
            [candidate_5, candidate_6, candidate_1, candidate_2, candidate_3, candidate_4],
            [candidate_6, candidate_5, candidate_2, candidate_1, candidate_3, candidate_4],
            [candidate_4, candidate_3, candidate_2, candidate_1, candidate_5, candidate_6],
            [candidate_5, candidate_6, candidate_1, candidate_2, candidate_3, candidate_4],
            [candidate_6, candidate_5, candidate_2, candidate_1, candidate_3, candidate_4],
            [candidate_2, candidate_1, candidate_3, candidate_4, candidate_5, candidate_6],
            [candidate_3, candidate_4, candidate_1, candidate_2, candidate_5, candidate_6],
            [candidate_4, candidate_3, candidate_2, candidate_1, candidate_5, candidate_6]
        ]

        electorate_1.distribute_votes(ballots_1)

        election.add_party(party_a)
        election.add_party(party_b)
        election.add_party(party_c)
        election.add_party(party_d)
        election.add_electorate(electorate_1)
        election.add_electorate(electorate_2)

        results = election.run_election()

        import random
        total_seats = 151
        seat_distribution = {}
        parties = election.parties.copy()
        remaining_seats = total_seats

        for i in range(len(parties) - 1):
            seats = random.randint(0, remaining_seats)
            seat_distribution[parties[i]] = seats
            remaining_seats -= seats

        seat_distribution[parties[-1]] = remaining_seats

        print("\nRandom Outcome (151 seats):")
        for party, seats in seat_distribution.items():
            print(f"{party.name}: {seats} seats")

        party_names = [party.name for party in seat_distribution]
        seat_counts = [seat_distribution[party] for party in seat_distribution]

        pyplot.figure(figsize=(10, 6))
        pyplot.bar(party_names, seat_counts, color='lightcoral')
        pyplot.xlabel('Parties')
        pyplot.ylabel('Seats Won')
        pyplot.title('Random Outcome - 151 Seat Distribution')
        pyplot.tight_layout()
        pyplot.show()