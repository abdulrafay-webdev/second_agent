import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio
from dotenv import load_dotenv



# load env 
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

gemini_api_key = "AIzaSyByA-Ioxj0rJCVjR_rkoN7xgPUg66slOIA"


# create client 
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# define model 
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=client
)

# configuration 
config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

# ai Agent 

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are helpful Assistent.",
        model=model
    )

    result = await Runner.run(agent, "write a counting of 1 to 10", run_config=config)
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
