from langchain.tools import tool

class TitleCaser:
    @tool("Title case a string")
    def enforce(text: str) -> str:
        """
        Enforce Title Case on input text.
        - Input: arbitrary string
        - Output: string in Title Case
        - Must not print; must return the transformed string.
        """
        # TODO: Implement a basic Title Case transformation
        # Instruction: Split on spaces, capitalize each word, join with spaces, return.
        raise NotImplementedError

