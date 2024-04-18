from typing import Dict, List


def add_data_to_complete_chat(
        complete_chat: List[Dict[str, str]],
        role: str,
        content: str
        ) -> List[Dict[str, str]]:
    """TBD"""
    complete_chat.append(
        {
            "role": role,
            "content": content
        }
    )

    return complete_chat