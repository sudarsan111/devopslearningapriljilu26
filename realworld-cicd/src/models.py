from dataclasses import dataclass, field
from typing import Optional
import uuid

@dataclass
class Task:
    title: str
    description: str = ""
    done: bool = False
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
        }

_store: dict[str, Task] = {}

def get_all() -> list[Task]:
    return list(_store.values())

def get_by_id(task_id: str) -> Optional[Task]:
    return _store.get(task_id)

def create(title: str, description: str = "") -> Task:
    task = Task(title=title, description=description)
    _store[task.id] = task
    return task

def update(task_id: str, **kwargs) -> Optional[Task]:
    task = _store.get(task_id)
    if task is None:
        return None
    for key, value in kwargs.items():
        if hasattr(task, key):
            setattr(task, key, value)
    return task

def delete(task_id: str) -> bool:
    if task_id in _store:
        del _store[task_id]
        return True
    return False

def clear() -> None:
    _store.clear()
