import asyncio
import datetime
import webbrowser
from urllib import parse

import fastapi
import msal
import requests
import tqdm
import uvicorn
from starlette.responses import PlainTextResponse

# noinspection PyUnresolvedReferences
from traceback_with_variables import activate_by_import


async def _get_token_by_app():
    callback_result = []
    app = fastapi.FastAPI()

    @app.route("/callback")
    async def callback(request):
        token = str(request.query_params)
        callback_result.append(token)
        try:
            return PlainTextResponse(token)
        finally:
            server.should_exit = True

    config = uvicorn.Config(
        app, host="localhost", port=50051, reload=False, log_level="error"
    )
    server = uvicorn.Server(config)
    await server.serve()
    return callback_result[0]


def _get_ms_token():
    auth_app = msal.ConfidentialClientApplication(
        client_id="cc4ec66f-9be5-41f2-a42d-7a70c8e0adad",
        authority="https://login.microsoftonline.com/common",
        client_credential="zi08Q~dmsDCibAiE3EaCSnqoKICCQL.HziFngbMz",
    )
    flow = auth_app.initiate_auth_code_flow(
        scopes=[
            "user.read",
            "mailboxsettings.read",
            "calendars.readwrite",
            "Tasks.Read",
            "Tasks.ReadWrite",
        ],
        redirect_uri="http://localhost:50051/callback",
    )
    open_url = flow["auth_uri"]
    webbrowser.open(open_url)
    print(f"web browser will open {open_url}")
    token: str = asyncio.run(_get_token_by_app())
    resp = dict(parse.parse_qsl(token))
    result = auth_app.acquire_token_by_auth_code_flow(flow, resp)
    return result["access_token"]


def save_output(text: str):
    print(text)
    output_file = r"D:\CodeProjects\WG\note\docs\日报.md"
    with open(output_file, "r", encoding="utf8") as f:
        day_log = f.read()
    day_log = day_log.replace("# 日报\n", "# 日报\n\n" + text)
    print("save to {}".format(output_file))
    with open(output_file, "w", encoding="utf8") as f:
        f.write(day_log)


def get_day_log(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    todo_task_lists = requests.get(
        "https://graph.microsoft.com/v1.0/me/todo/lists", headers=headers
    ).json()

    # Get today's date in the correct format for the query filter
    today_date = datetime.datetime.today().strftime("%Y-%m-%dT00:00:00Z")

    # Set the query parameters to filter tasks by created, modified, or completed dates
    query_params = {
        "$filter": f"createdDateTime ge {today_date} or lastModifiedDateTime ge {today_date}",
    }
    ret_text = today_date.split("T")[0] + "\n\n"

    for task_list in todo_task_lists["value"]:
        todo_tasks = requests.get(
            f"https://graph.microsoft.com/v1.0/me/todo/lists/{task_list['id']}/tasks",
            params=query_params,
            headers=headers,
        ).json()
        for task in tqdm.tqdm(todo_tasks["value"], desc=task_list["displayName"]):
            status = "x" if task["status"] == "completed" else " "
            due_date_time = (
                task.get("dueDateTime", {}).get("dateTime", "").split("T")[0]
            )
            if due_date_time:
                due_date_time = f" 截止 {due_date_time}"
            importance = " !" if task.get("importance", "") == "high" else ""
            ret_text += f"\n- [{status}] {task['title']}" + due_date_time + importance
            for i in task.get("checklistItems", []):
                status = "x" if i["isChecked"] else " "
                ret_text += f"\n  - [{status}] {i['displayName']}"
            # print(task)

    # print(ret_text)
    return ret_text


def service():
    ms_token = _get_ms_token()
    print("token", ms_token)
    text = get_day_log(access_token=ms_token)
    save_output(text)


if __name__ == "__main__":
    print(_get_ms_token())
    # service(2)
