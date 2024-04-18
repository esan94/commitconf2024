from typing import Any, Callable
from loguru import logger

import openai


def moderation(func: Callable) -> Callable:
    """
    A decorator that adds moderation handling to a function or method.

    This decorator catches `InvalidRequestError` exceptions related to content filtering 
    from the wrapped function and returns a predefined moderation message.

    Parameters:
    -----------
    func : Callable
        The function or method to be wrapped by the decorator.

    Returns:
    --------
    Callable
        A wrapper function that includes exception handling for content moderation.

    Notes:
    ------
    - The decorator expects the first argument of the wrapped function to be a class instance (self).
    - This class instance should have an attribute `config` with an attribute `openai_moderation_ad` 
      which contains the predefined moderation response.
    - This decorator is used with method OpenAIManager.get_response_openai.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            response = func(*args, **kwargs)
        except openai.OpenAIError as err:
            logger.error(err)
            if err.code == "content_filter":
                response = "Moderation error"
        return response
    return wrapper  


class OpenAIManager:
    """Manager to handle the Cognitive Services"""

    def __init__(self) -> None:
        """
        Initializes variables to be used by the class.
        """
        # Initialize OpenAI
        self.openai_client = openai.AzureOpenAI(
            api_key="4dc75d20794742658e5331081105f1c5",  
            api_version="2023-05-15",
            azure_endpoint="https://emt-commitconf.openai.azure.com/"
        )


    @moderation
    def get_response_openai(
        self,
        complete_chat,
        temperature=0.8
        ) -> str:
        response = self.openai_client.chat.completions.create(
            model="gpt-35-turbo-16k",
            messages=complete_chat,
            temperature=temperature,
        )
        response = response.choices[0].message.content.strip()

        return response
