from langchain_core.prompts import PromptTemplate
from app.prompts.sql_prompt import SQL_PROMPT
from app.utils.llm import llm

def sql_agent(question):

    prompt = PromptTemplate(
        template=SQL_PROMPT,
        input_variables=["question"]
    )

    chain = prompt | llm

    response = chain.invoke({
        "question": question
    })

    return response.content