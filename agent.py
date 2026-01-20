"""
LangChain Agent with Anthropic Claude
"""
import os
from langchain_anthropic import ChatAnthropic
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


def create_agent():
    """Create and configure the LangChain agent."""
    # Initialize the Claude model
    model = ChatAnthropic(
        model="claude-sonnet-4-5-20250929",
        api_key=os.getenv("ANTHROPIC_API_KEY"),
    )

    # Define the tools
    tools = [get_weather]

    # Create the prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    # Create the agent
    agent = create_tool_calling_agent(model, tools, prompt)

    # Create the agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor


def main():
    """Run the agent with a sample query."""
    agent = create_agent()

    # Run the agent
    result = agent.invoke({"input": "what is the weather in sf"})

    print("\n" + "="*50)
    print("RESULT:")
    print("="*50)
    print(result["output"])


if __name__ == "__main__":
    main()
