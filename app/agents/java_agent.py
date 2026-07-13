from langchain_core.prompts import PromptTemplate
from app.prompts.java_prompt import JAVA_PROMPT
from app.utils.llm import llm

def java_agent(question):

    prompt = PromptTemplate(
        template=JAVA_PROMPT,
        input_variables=["question"]
    )

    chain = prompt | llm

    response = chain.invoke({
        "question": question
    })

    return response.content