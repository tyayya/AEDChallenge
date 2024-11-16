import os
import uuid
from participant import load_participants

current_directory = os.getcwd()
participants = load_participants(current_directory + "/data/datathon_participants.json")

class SimpleParticipant:
    def __init__(
                self, 
                id: uuid.UUID, 
                year: str, 
                program_skills: dict[str, int],
                experience: str, 
                hackathons: int, 
                roles: str, 
                languages: list[str], 
                challenges: list[str], 
                interests: list[str], 
                objective: str, 
                availability: dict[str, bool],
                friend_registration: list[uuid.UUID],
                preferred_team_size: int,

                ):
        self.id = id
        self.year = year 
        self.program_skills = program_skills 
        self.experience = experience 
        self.hackathons = hackathons 
        self.roles = roles
        self.languages = languages 
        self.challenges = challenges
        self.interests = interests
        self.objective = objective
        self.availability = availability # done
        self.friend_registration = friend_registration
        self.preferred_team_size = preferred_team_size

    
    def run(self):
        """here goes all the secondary function calls"""
        self.availability = self.check_availability()
        self.year = self.simple_year()
        self.program_skills = self.simple_skills()
        self.experience = self.simple_experience()
        self.roles = self.simple_roles()
        


    def check_availability(self) -> list[bool]:
        return list(self.availability.values())
    
    def simple_year(self) -> int:
        year_number:int
        
        if self.year[0] in ['1', '2', '3', '4']:
            year_number = int(self.year[0])
        elif self.year[0].lower() == 'm':
            year_number = 5
        elif self.year[0].lower() == 'p':
            year_number = 6
        
        #  if something goes wrong, assign 3 as it is the mean value:
        else:
            year_number = 3
        
        return year_number

    def simple_skills(self) -> int:
        skills = 0
        
        for skill, level in self.program_skills.items():
            skills += level
        #  we'll leave the normalization for later, when we have all the participants
        
        return skills
    
    def simple_experience(self) -> int:
        experience:int

        match self.experience:
            case "Beginner":
                experience = 0
            case "Intermediate":
                experience = 1
            case "Advanced":
                experience = 2
            
            #  if something goes wrong, assign 1 as it is the mean value:
            case _:
                experience = 1
        
        return experience

    def simple_roles(self) -> int:
        roles:int
        match self.roles:
            case "Analysis":
                roles = 1
            case "Visualization":
                roles = 2
            case "Development":
                roles = 3
            case "Design":
                roles = 4
            
            #  if it is "Don't know" or "Don't care", we'll assign 0:
            case _:
                roles = 0
        
        return roles


def normalize_skills(skills_list):
    max_value = max(skills_list)
    normalized_list = [value / max_value for value in skills_list]

    return normalized_list

def load_participants():
    participants_list = list()
    skills_list = list()
    for participant in participants:
        simple_participant = SimpleParticipant(
            participant.id,
            participant.year_of_study,
            participant.programming_skills,
            participant.experience_level,
            participant.hackathons_done,
            participant.preferred_role,
            participant.preferred_languages,
            participant.interest_in_challenges,
            participant.interests,
            participant.objective,
            participant.availability,
            participant.friend_registration,
            participant.preferred_team_size
        )

        simple_participant.run()
        participants_list.append(simple_participant)
        skills_list.append(simple_participant.program_skills)
    
    skills_list = normalize_skills(skills_list)

    for index, simple_participant in enumerate(participants_list):
        simple_participant.program_skills = skills_list[index]
    
    return participants_list

if __name__ == '__main__':
    load_participants()
