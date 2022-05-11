import os
import uvicorn
from dotenv import load_dotenv
from pathlib import Path

if __name__ == "__main__":

    dotenv_path = Path('Frontend/.env')
    load_dotenv(dotenv_path=dotenv_path)

    uvicorn.run("src.app:app", port=int(os.getenv('REACT_APP_BackendPORT')), reload=True, proxy_headers=True)