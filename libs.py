class Member:
    def __init__(self, name):
        self.name = name
        self.is_active = True
    
    def __repr__(self):
        return self.name
    
    def deactivate(self):
        self.is_active = False
    
    def activate(self):
        self.is_active = True
        

class Library:
    def __init__(self, name) :
        self.name = name
        self.books = []
        self.members = []

    def register_member(self, member: Member):
        self.members.append(member)
    
    def get_active_members(self):
        active_members = [member.name for member in self.members if member.is_active is True]
        
        return active_members
