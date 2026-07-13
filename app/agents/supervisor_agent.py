def supervisor_agent(question):

    question = question.lower()

    if "java" in question:
        return "java"

    elif "sql" in question:
        return "sql"

    elif "array" in question or "leetcode" in question:
        return "dsa"

    else:
        return "hr"