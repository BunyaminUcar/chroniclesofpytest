import requests

url="https://todo.pixegami.io"


def test_call_url():
    response = requests.get(url)
    assert response.status_code == 200

def test_can_create_test():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    
    data=create_task_response.json()
    
    task_id = data["task"]["task_id"]
    get_task_response=get_task(task_id)
     
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]
    
    
def test_can_update_task():
    payload = new_task_payload()
    
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,  
        "content": "denemev3",
        "is_done": True,
  
    } 
    
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200
    
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]


def test_can_get_task():
    payload=new_task_payload()
    get_list_task_response = list_tasks(payload["user_id"])
    assert get_list_task_response.status_code == 200
    get_list_data=get_list_task_response.json()
    print(get_list_data)

def create_task(payload):
    return  requests.put(url + "/create-task", json=payload )

def update_task(payload):
    return  requests.put(url + "/update-task", json=payload )

def get_task(task_id):
    return requests.get(url + "/get-task/" + task_id)  
def list_tasks(user_id):
    return requests.get(url + "/list-tasks/" + user_id)
def new_task_payload():
    return {
  "content": "denemev2",
  "user_id": "Benjamin",
  
  "is_done": False,
  
}