import json
import pathlib
import uuid
from dataclasses import dataclass, asdict
from typing import Dict, List, Literal
import os

current_directory = os.getcwd()


@dataclass
class Participant:
    id: uuid.UUID  # Unique identifier

    # Personal data
    name: str
    email: str
    age: int
    year_of_study: Literal["1st year", "2nd year", "3rd year", "4th year", "Masters", "PhD"]
    shirt_size: Literal["S", "M", "L", "XL"]
    university: str
    dietary_restrictions: Literal["None", "Vegetarian", "Vegan", "Gluten-free", "Other"]

    # Experience and programming skills
    programming_skills: Dict[str, int]
    experience_level: Literal["Beginner", "Intermediate", "Advanced"]
    hackathons_done: int

    # Interests, preferences and constraints
    interests: List[str]
    preferred_role: Literal[
        "Analysis", "Visualization", "Development", "Design", "Don't know", "Don't care"
    ]
    objective: str
    interest_in_challenges: List[str]
    preferred_languages: List[str]
    friend_registration: List[uuid.UUID]
    preferred_team_size: int
    availability: Dict[str, bool]

    # Description of the participant
    introduction: str
    technical_project: str
    future_excitement: str
    fun_fact: str


def load_participants(path: str) -> List[Participant]:
    if not pathlib.Path(path).exists():
        raise FileNotFoundError(
            f"The file {path} does not exist, are you sure you're using the correct path?"
        )
    if not pathlib.Path(path).suffix == ".json":
        raise ValueError(
            f"The file {path} is not a JSON file, are you sure you're using the correct file?"
        )

    # Convert UUID strings back to UUID objects
    participants_data = json.load(open(path))
    for participant in participants_data:
        participant["id"] = uuid.UUID(participant["id"])
        participant["friend_registration"] = [
            uuid.UUID(friend_id) for friend_id in participant["friend_registration"]
        ]
    return [Participant(**participant) for participant in participants_data]


def save_participant(data: dict, path: str = (current_directory + "datathon_participants.json")):
    """Create a Participant object from data and save it to a JSON file."""

    # Create a Participant object
    participant = Participant(
        id=uuid.uuid4(),
        name=data["name"],
        email=data["email"],
        age=data["age"],
        year_of_study=data["year_of_study"],
        shirt_size=data["shirt_size"],
        university=data["university"],
        dietary_restrictions=data["dietary_restrictions"],
        interests=data["interests"],
        preferred_role=data["preferred_role"],
        experience_level=data["experience_level"],
        hackathons_done=data["hackathons_done"],
        objective=data["objective"],
        introduction=data["introduction"],
        technical_project=data["technical_project"],
        future_excitement=data["future_excitement"],
        fun_fact=data["fun_fact"],
        preferred_languages=data["preferred_languages"],
        friend_registration=[
            uuid.UUID(friend_id) for friend_id in data["friend_registration"]
        ],
        preferred_team_size=data["preferred_team_size"],
        availability=data["availability"],    
        programming_skills=data["programming_skills"],
        interest_in_challenges=data["interest_in_challenges"],
    )

    # Convert Participant object to a dictionary and serialize UUIDs to strings
    participant_data = asdict(participant)
    participant_data["id"] = str(participant_data["id"])
    participant_data["friend_registration"] = [
        str(friend_id) for friend_id in participant_data["friend_registration"]
    ]

    # Load existing participants
    with open(path, "r") as f:
        participants = json.load(f)

    # Add the new participant
    participants.append(participant_data)

    # Save updated participants
    with open(path, "w") as f:
        json.dump(participants, f, indent=4)