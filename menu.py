import sys
from election import Election
from party import Party
from electorate import Electorate
from candidate import Candidate
import matplotlib.pyplot as plt

def display_menu():
    print("\nElection Management System")
    print("1. Add Electorate")
    print("2. Add Party")
    print("3. Add Candidate")
    print("4. Run Election")
    print("5. Exit")

def handle_add_electorate(election):
    name = input("Enter electorate name: ")
    election.add_electorate(Electorate(name, {}))
    print(f"'{name}' Electorate added.")

def handle_add_party(election):
    name = input("Enter party name: ")
    party = Party(name)
    election.add_party(party)
    print(f"'{name}' added (Party).")

def handle_add_candidate(election):
    name = input("Enter candidate name: ")
    party_name = input("Enter party name: ")
    party = next((p for p in election.parties if p.name == party_name), None)
    if not party:
        print("Party not found. Please add the party first.")
        return
    electorate_name = input("Enter electorate name: ")
    electorate = next((e for e in election.electorates if e.name == electorate_name), None)
    if not electorate:
        print("Electorate not found. Please add the electorate first.")
        return
    candidate = Candidate(name, party)
    electorate.candidates[candidate] = candidate
    print(f"Candidate: '{name}' added to '{electorate_name}' Electorate.")

def handle_run_election(election):
    results = election.run_election()
    print("Election completed!")

    party_names = []
    vote_counts = []

    for party, votes in results.items():
        party_names.append(party.name)

def main():
    election = Election()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                handle_add_electorate(election)
            case "2":
                handle_add_party(election)
            case "3":
                handle_add_candidate(election)
            case "4":
                handle_run_election(election)
            case "5":
                print("Exiting...")
                sys.exit()
            case "6":
                election.run_example_election()
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()