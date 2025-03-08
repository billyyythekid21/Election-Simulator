class Party:
    def __init__(self, name):
        self.name = name
        self.member_count = 0
        self.members = []

    def __str__(self):
        return f"{self.name}"
    
    def add_member(self, member_name: str):
        self.members.append(member_name)