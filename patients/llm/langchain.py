import os
import json
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from langchain.agents import create_csv_agent

from django.conf import settings

openai_api_key = "<ADD OPEN AI API KEY HERE>"
# os.environ.get("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai_api_key, temperature=0)

database_name = settings.DATABASES['default']['NAME']
dburi = 'sqlite:///'+ os.path.abspath(database_name)

db = SQLDatabase.from_uri(dburi)

db_chain = SQLDatabaseChain(llm=llm, database=db)





def queryDb(prompt: str):
    result = db_chain.run(prompt)
    
    res = json.dumps(result)
    
    return res
    
    
def queryCSV(prompt: str):
    # Query csv 
    try:
        file_name = 'MOCK_DATA_4_COLUMNS.csv'
        file_path = os.path.join(os.getcwd(), file_name)
        agent = create_csv_agent(llm=llm, path=file_path, verbose=True)
        result = agent.run(prompt)
        res = json.dumps(result)
        return res
    except Exception as e:
        print(e)

