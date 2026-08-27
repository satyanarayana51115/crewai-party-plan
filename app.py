import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, Process, LLM

# To load API key from .env file
load_dotenv()

# Configuration of GEMINI LLM
gemini_llm = LLM(
    model="gemini/gemini-3.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# 1. Agents (add gemini_llm to every agent)
satya = Agent(
    role="Satya - Party Planner",
    goal="Create the party plan, including the theme, timeline, and guest list.",
    backstory="You organize the vision for the party, create a timeline, and ensure all aspects are planned."
        "You send out invitations and coordinate with the other agents.",
    verbose=True,
    llm=gemini_llm
)
# 2. Agent
narayana = Agent(
    role="Narayana - Food & Beverage Coordinator.",
    goal="Organize the food and drinks for the party, ensuring there's enough variety for all guests.",
    backstory="You handle the food and drink preparations, whether it's cooking, ordering, or working with caterers."
        "You make sure guests have plenty to eat and drink throughout the event.",
    verbose=True,
    llm=gemini_llm
)
# 3. Agent
murthy = Agent(
    role="Murthy - Decorator",
    goal="Make the party venue look great, fitting the theme and making it fun for guests.",
    backstory="You decorate the venue to match the theme and create a welcoming and festive environment."
        "You ensure the venue is ready when the guests arrive.",
    verbose=True,
    llm=gemini_llm
)
# 4. Agent
raju = Agent(
    role="Raju - Entertainment & Guest Relations Coordinator",
    goal="Organize entertainment, games, and manage guest interactons to ensure a fun party",
    backstory="You make sure the guests have fun, whether it's through music, games, or other activities."
        "You also help guests with seating and ensure the event flows smoothly.",
    verbose=True,
    llm=gemini_llm
)

# Tasks
task1 = Task(
    description="Create party plan including theme, timeline, and guest list.",
    expected_output="Complete party plan with theme, timeline, and invitations.",
    agent=satya,
)

task2 = Task(
    description="Organize food and drinks menu and set up food stations.",
    expected_output="Food and drinks ready for the party.",
    agent=narayana,
)

task3 = Task(
    description="Decorate the venue according to the theme.",
    expected_output="Venue decorated and ready for guests.",
    agent=murthy,
)

task4 = Task(
    description="Organize music, games, and manage guest interactions.",
    expected_output="A fun and engaging atmosphere with happy guests.",
    agent=raju,
    output_file="final_report.md"
)
# setup crew workflow
party_crew = Crew(
    agents=[satya, narayana, murthy, raju], 
    tasks=[task1, task2, task3, task4],
    verbose=True,
    process=Process.sequential,
)

# 4. Execute Workflow
if __name__ == "__main__":
    print("--- Gemini Agentic Workflow Started ---")
    party_result = party_crew.kickoff()
    
    print("\n\n========================")
    print("## FINAL REPORT ##")
    print("========================\n")
    print(party_result)

