import random
from candidate import Candidate
from party import Party
from collections import Counter

class Electorate:
    def __init__(self, name: str, candidates: dict):
        self.name = name
        self.candidates = candidates
        self.ballots = []
        self.winner = None

    def distribute_votes(self, ballots):
        self.ballots = ballots
        for ballot in self.ballots:
            if ballot:
                first_pref = ballot[0]
                self.candidates[first_pref].votes.append(ballot)

    def count_votes(self):
        return {candidate: len(candidate.votes) for candidate in self.candidates.values()}

    def eliminate_candidate(self):
        votes = self.count_votes()
        min_votes = min(votes.values())
        for candidate, vote_count in votes.items():
            if vote_count == min_votes:
                for ballot in candidate.votes:
                    ballot.pop(0)
                    if ballot:
                        next_pref = ballot[0]
                        self.candidates[next_pref].votes.append(ballot)
                del self.candidates[candidate]
                return candidate

    def run_election(self):
        print(f"Electorate: {self.name}")

        while len(self.candidates) > 1:
            votes = self.count_votes()
            print(f"Votes: {votes}")
            eliminated_candidate = self.eliminate_candidate()
            print(f"Eliminated Candidate: {eliminated_candidate.name}")

        self.winner = list(self.candidates.keys())[0]
        print(f"{self.name}'s winner: {self.winner.name} of {self.winner.party}")
        return self.winner

party_a = Party("Party A")
party_b = Party("Party B")

candidate_1 = Candidate("Alice", party_a)
candidate_2 = Candidate("Bob", party_b)

electorate = Electorate("Chisholm", {candidate_1: candidate_1, candidate_2: candidate_2})

ballots = [
    [candidate_1, candidate_2],
    [candidate_2, candidate_1],
    [candidate_1, candidate_2]
]

electorate.distribute_votes(ballots)
print(type(electorate.candidates))
winner = electorate.run_election()