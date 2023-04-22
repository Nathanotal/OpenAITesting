import os
import openai
import json

# Load your API key from secrets.json
with open("secrets.json") as f:
    secrets = json.load(f)
    os.environ["OPENAI_API_KEY"] = secrets["OPENAI_API_KEY"]
    os.environ["OPENAI_ORG_ID"] = secrets["OPENAI_ORG_ID"]

openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
