from dotenv import load_dotenv
from agents import Agent, Runner, trace, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI
import os

load_dotenv(override=True)


github_token = os.getenv("GITHUB_TOKEN")
openai_base_url = os.getenv("GITHUB_OPENAI_BASE_URL")

# print("GitHub Token:", github_token[:4] + "..." + github_token[-4:])
# print("OpenAI Base URL:", openai_base_url)

github_client = AsyncOpenAI(base_url=openai_base_url, api_key=github_token)

github_model = OpenAIChatCompletionsModel(openai_client=github_client, model="gpt-4o-mini")
