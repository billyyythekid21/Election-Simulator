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
        
        candidates_to_eliminate = [candidate for candidate, vote_count in votes.items() if vote_count == min_votes]
        
        for candidate in candidates_to_eliminate:
            for ballot in candidate.votes:
                while ballot:
                    ballot.pop(0)
                    if ballot and ballot[0] in self.candidates:
                        next_pref = ballot[0]
                        self.candidates[next_pref].votes.append(ballot)
                        break

            del self.candidates[candidate]
            return candidate

    def run_election(self):
        irv_round = 1

        print("\n--------------->")
        print(f"Electorate: {self.name}")

        while len(self.candidates) > 1:
            votes = self.count_votes()
            print(f"Votes: {votes}")
            eliminated_candidate = self.eliminate_candidate()
            print(f"Eliminated Candidate in Round {irv_round}: {eliminated_candidate.name}")
            irv_round += 1

        self.winner = list(self.candidates.values())[0]
        print(f"{self.name}'s winner: {self.winner.name} of {self.winner.party}")
        print("-------------->\n")
        return self.winner