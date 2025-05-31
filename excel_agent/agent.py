from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv
from excel_agent.tools import read_excel

load_dotenv()

model = LiteLlm(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_base=os.getenv("AZURE_OPENAI_API_ENDPOINT"),
)

root_agent = Agent(
    name="excel_agent",
    model=model,
    description="你是個Excel專家，可以幫助使用者處理Excel文件",
    instruction="""
        1. 你是一個Excel專家，可以幫助使用者處理Excel文件。
        2. 你可以讀取Excel檔案名稱，並且讀取Excel檔案的內容。
        3. 你可以讀取工作表名稱。
        4. 如果使用者給你一個Excel檔案名稱，請使用工具`read_excel`來讀取Excel檔案的內容。
        5. 如果使用者給你一個工作表名稱，請使用工具`read_excel`來讀取Excel檔案的內容，如果沒有則為None。
    """,
    tools=[read_excel],
)
