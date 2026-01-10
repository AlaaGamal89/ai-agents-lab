
from crewai import Agent, Crew, Process, Task, tools
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from mobile_selector.tools.push_message_tool import PushNotification


@CrewBase
class MobileSelector():
    """MobileSelector crew"""

    agents: List[BaseAgent]
    tasks: List[Task]


    @agent
    def spec_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['spec_collector'],
            verbose=True
        )
    
    #you should use the PushNotification to sent a message with only the name of the selected mobile.
    @agent
    def choice_selector(self) -> Agent:
        return Agent(
            config=self.agents_config['choice_selector'],
            verbose=True,
            tools=[PushNotification()]
        )
        
    @task
    def collect_specs_task(self) -> Task:
        return Task(
            config=self.tasks_config['collect_specs_task'],
            verbose=True
        )
        
    @task
    def select_best_mobile_task(self) -> Task:
        return Task(
            config=self.tasks_config['select_best_mobile_task'],
            verbose=True
        )
        
    @crew
    def crew(self) -> Crew:
        """Creates the MobileSelector crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
