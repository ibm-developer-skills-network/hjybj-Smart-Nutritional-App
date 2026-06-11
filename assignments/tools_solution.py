from langchain.tools import tool

class TitleCaser:
    @tool("Title case a string")
    def enforce(text: str) -> str:
        """
        Convert input text to Title Case.
        - Input: arbitrary string
        - Output: same string in Title Case
        """
        if not text or text.strip() == "":
            return ""
        words = text.split()
        return " ".join(w.capitalize() for w in words)

