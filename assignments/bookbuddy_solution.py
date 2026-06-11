import os
import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")

@CrewBase
class BaseBookBuddyCrew:
    agents_config_path = os.path.join(CONFIG_DIR, "agents.yaml")
    tasks_config_path = os.path.join(CONFIG_DIR, "tasks.yaml")

    def __init__(self, blurb: str):
        self.blurb = blurb

        # Load agent configs
        with open(self.agents_config_path, "r") as f:
            self.agents_config = yaml.safe_load(f)

        # Load task configs
        with open(self.tasks_config_path, "r") as f:
            self.tasks_config = yaml.safe_load(f)

    # --------------------
    # Agents
    # --------------------

    @agent
    def genre_detector_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["genre_detector_agent"],
            allow_delegation=False,
            verbose=True
        )

    @agent
    def tagline_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["tagline_writer_agent"],
            allow_delegation=False,
            verbose=True
        )

    # --------------------
    # Tasks
    # --------------------

    @task
    def detect_genre_task(self) -> Task:
        task_cfg = self.tasks_config["detect_genre_task"]
        return Task(
            description=task_cfg["description"],
            agent=self.genre_detector_agent(),
            expected_output=task_cfg["expected_output"]
        )
      
    @task
    def write_tagline_task(self) -> Task:
        task_cfg = self.tasks_config["write_tagline_task"]
        return Task(
            description=task_cfg["description"],
            agent=self.tagline_writer_agent(),
            expected_output=task_cfg["expected_output"]
        )

# --------------------
# Crew Assembly
# --------------------

@CrewBase
class BookBuddyCrew(BaseBookBuddyCrew):
    @crew
    def crew(self) -> Crew:
        tasks = [
            self.detect_genre_task(),
            self.write_tagline_task()
        ]
        agents = [
            self.genre_detector_agent(),
            self.tagline_writer_agent()
        ]
        return Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )

# --------------------
# Main Execution (tests)
# --------------------

if __name__ == "__main__":
    print("=== BookBuddyCrew Test Run ===")
    blurb = "A brave knight sets out on a quest to save the kingdom from a dragon."

    crew = BookBuddyCrew(blurb=blurb).crew()

    print("\nRunning crew with sample blurb:")
    print(f"Blurb: {blurb}\n")

    crew_output = crew.kickoff(inputs={'blurb': blurb})

    print(f"Raw Output: {crew_output}")
    
