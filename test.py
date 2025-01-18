from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent


@tool
def multiply(x: float, y: float) -> float:
    """ Multiply 'x' times 'y'."""
    return x * y

@tool
def exponentiate(x: float, y: float) -> float:
    """ Raise 'x' to the 'y'."""
    return x**y

@tool
def add(x: float, y: float) -> float:
    """ Add 'x' and 'y'."""
    return x + y


@tool
def create_file(x: str, y: float) -> float:
    """ yの文字列が書き込まれたファイルをxの場所に生成 """
    with open(x, "w") as file:
        file.write(f"{str(y)} \n")



tools = [multiply, exponentiate, add, create_file]

prompt = ChatPromptTemplate.from_messages([
    ("system", "you're a helpful assistant"), 
    ("human", "{input}"), 
    ("placeholder", "{agent_scratchpad}"),
])

llm = ChatOllama(model="llama3.1:8b-instruct-q8_0")

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

question_list = [
    "5に3を足した数字を計算", 
    "その結果を ppp9999.txt に出力", 
]
question_text = ""
for question in question_list:
    question_text += question + "\n"

agent_executor.invoke({"input": question_text})
