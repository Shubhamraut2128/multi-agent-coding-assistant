from app.agents.supervisor_agent import supervisor_agent
from app.agents.java_agent import java_agent
from app.agents.sql_agent import sql_agent
from app.agents.dsa_agent import dsa_agent
from app.agents.hr_agent import hr_agent
from app.agents.validator_agent import validator_agent

def run_workflow(question):

    route = supervisor_agent(question)

    if route == "java":
        response = java_agent(question)

    elif route == "sql":
        response = sql_agent(question)

    elif route == "dsa":
        response = dsa_agent(question)

    else:
        response = hr_agent(question)

    validated = validator_agent(response)

    return validated