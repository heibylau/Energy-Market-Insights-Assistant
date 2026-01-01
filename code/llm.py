from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
_llm = ChatOpenAI(
    model="gpt-5-mini",
    temperature=0.3,
)

def _build_context(df):
    summary = df.groupby("hub")["display_price"].mean()

    return f"""
    This dashboard analyzes Alberta AECO-C and Henry Hub natural gas prices
    using AER ST98 outlook data.

    Average prices:
    - Henry Hub: {summary['Henry Hub']:.2f}
    - AECO-C: {summary['AECO-C']:.2f}

    Prices are annual averages and include both historical and forecast values.
    """

def get_energy_chain(df):
    context = _build_context(df)

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are an energy market analyst specializing in North American natural gas."),
        ("human",
         "Context:\n{context}\n\nQuestion:\n{question}")
    ])

    def run(question: str) -> str:
        messages = prompt.format_messages(
            context=context,
            question=question
        )
        response = _llm.invoke(messages)
        return response.content

    return run