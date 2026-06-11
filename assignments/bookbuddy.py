import os
import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Path to the config directory
CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")

@CrewBase
class BaseBookBuddyCrew:
    agents_config_path = os.path.join(CONFIG_DIR, "agents.yaml")
    tasks_config_path = os.path.join(CONFIG_DIR, "tasks.yaml")

    def __init__(self, blurb: str):
        self.blurb = blurb

        # TODO: Load agents.yaml into self.agents_config
        # TODO: Load tasks.yaml into self.tasks_config

    # --------------------
    # Agents
    # --------------------

    @agent
    def genre_detector_agent(self) -> Agent:
        # TODO: Create an Agent using self.agents_config["genre_detector_agent"]
        pass

    @agent
    def tagline_writer_agent(self) -> Agent:
        # TODO: Create an Agent using self.agents_config["tagline_writer_agent"]
        pass

    # --------------------
    # Tasks
    # --------------------

    @task
    def detect_genre_task(self) -> Task:
        # TODO: Create a Task using self.tasks_config["detect_genre_task"]
        pass

    @task
    def write_tagline_task(self) -> Task:
        # TODO: Create a Task using self.tasks_config["write_tagline_task"]
        pass

# --------------------
# Crew Assembly
# --------------------

@CrewBase
class BookBuddyCrew(BaseBookBuddyCrew):
    @crew
    def crew(self) -> Crew:
        # TODO: Assemble agents and tasks in sequential order
        pass

# --------------------
# Main Execution (tests)
# --------------------

if __name__ == "__main__":
    print("=== BookBuddyCrew Test Run ===")
    blurb = "A brave knight sets out on a quest to save the kingdom from a dragon."

    # TODO: Instantiate BookBuddyCrew with the blurb
    # TODO: Run crew.kickoff() with correct input and print results
