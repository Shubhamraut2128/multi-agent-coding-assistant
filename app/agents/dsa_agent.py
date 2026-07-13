from langchain_core.prompts import PromptTemplate
from app.prompts.dsa_prompt import DSA_PROMPT
from app.utils.llm import llm

def dsa_agent(question):

    prompt = PromptTemplate(
        template=DSA_PROMPT,
        input_variables=["question"]
    )

    chain = prompt | llm

    response = chain.invoke({
        "question": question
    })

    return response.content