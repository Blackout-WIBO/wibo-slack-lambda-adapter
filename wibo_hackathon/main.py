import aiohttp
from fastapi import FastAPI, BackgroundTasks, Request
import requests
import json

app = FastAPI()

@app.post("/wibo/rnr")
async def read_root(request: Request, background_tasks: BackgroundTasks):
    # Read the incoming request body
    try:
        body = await request.body()
        if not body:
            return {"error": "Request body is empty."}

        # Parse x-www-form-urlencoded body
        body_data = body.decode("utf-8")
        body_json = dict(pair.split('=') for pair in body_data.split('&'))
    except Exception as e:
        print(f"Error parsing request body: {e}")
        return {"error": "Invalid request body format."}

    # Log the body for debugging
    print(f"Request body: {body_json}")

    # Pass the same body to the background task
    headers = {
        "Content-Type": "application/json"
    }
    url = "https://mosdzl6z5wb6uwsc4ywolyvc2y0fcqdr.lambda-url.us-east-1.on.aws/"

    background_tasks.add_task(request_slack, body_json, headers, url)

    return "역할을 분담 중입니다! 잠시만 기다려주세요."

@app.post("/wibo/contribution/")
async def  contribution_calculation(request: Request, background_tasks: BackgroundTasks):
    # Read the incoming request body
    try:
        body = await request.body()
        if not body:
            return {"error": "Request body is empty."}

        # Parse x-www-form-urlencoded body
        body_data = body.decode("utf-8")
        body_json = dict(pair.split('=') for pair in body_data.split('&'))
    except Exception as e:
        print(f"Error parsing request body: {e}")
        return {"error": "Invalid request body format."}

    # Log the body for debugging
    print(f"Request body: {body_json}")

    # Pass the same body to the background task
    headers = {
        "Content-Type": "application/json"
    }
    url = "https://amfly3gcgavodxsgsbe2yec2ri0djcuy.lambda-url.us-east-1.on.aws/"

    background_tasks.add_task(request_slack, body_json, headers, url)

    return "기여도를 계산 중입니다! 잠시만 기다려주세요."



@app.post("/wibo/recall")
async def recall(request: Request, background_tasks: BackgroundTasks):
    # Read the incoming request body
    try:
        body = await request.body()
        if not body:
            return {"error": "Request body is empty."}

        # Parse x-www-form-urlencoded body
        body_data = body.decode("utf-8")
        body_json = dict(pair.split('=') for pair in body_data.split('&'))
    except Exception as e:
        print(f"Error parsing request body: {e}")
        return {"error": "Invalid request body format."}

    # Log the body for debugging
    print(f"Request body: {body_json}")

    # Pass the same body to the background task
    headers = {
        "Content-Type": "application/json"
    }
    url = "https://zecgdtxkbm5hm7xlaajyvnnzuy0cauxp.lambda-url.us-east-1.on.aws/"

    background_tasks.add_task(request_slack, body_json, headers, url)

    return "오늘 진행한 회의를 정리 중입니다! 잠시만 기다려주세요."


async def request_slack(body, headers, url):

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=body, headers=headers) as response:
                if response.status == 200:
                    result = await response.json()
                    print(f"Request succeeded: {result}")
                else:
                    text = await response.text()
                    print(f"Request failed with status code {response.status}: {text}")
    except Exception as e:
        print(f"Error during request: {str(e)}")



