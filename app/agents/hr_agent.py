from langchain_core.prompts import PromptTemplate
from app.prompts.hr_prompt import HR_PROMPT
from app.utils.llm import llm

def hr_agent(question):

    prompt = PromptTemplate(
        template=HR_PROMPT,
        input_variables=["question"]
    )

    chain = prompt | llm

    response = chain.invoke({
        "question": question
    })

    return response.content