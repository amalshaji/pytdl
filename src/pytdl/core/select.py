from PyInquirer import prompt
from typing import Dict


def generate_options(videos: Dict) -> Dict:
    questions = [
        {
            "type": "list",
            "name": "Choose download format",
            "message": "Choose the download format",
            "choices": videos.keys(),
        }
    ]

    answers = prompt(questions)
    return answers
