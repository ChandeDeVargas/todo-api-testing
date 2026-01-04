import sys


sys.path.append('../app')
from app.database import create_tasks, get_all_tasks, get_task_by_id, update_task, delete_task, mark_as_completed


def test_create_task():
    # Arrange (for prepare data)
    title = "Test Task"
    description = "Testing Create Function"

    # Act (execute the function)
    create_tasks(title, description)
    tasks = get_all_tasks()

    # Verificamos el resultado.
    assert len(tasks) > 0


def test_get_all_task():
    title = "Test Task"
    description = "Testing Get All Task"
    create_tasks(title, description)
    tasks = get_all_tasks()
    assert tasks is not None


def test_get_task_by_id():
    # 1. ARRANGE: Crear una tarea para tener algo que buscar
    title = "Tarea de prueba"
    description = "Descripción de prueba"
    create_tasks(title, description, None)

    # Obtener todas las tareas para saber el ID de la última
    all_tasks = get_all_tasks()
    last_task = all_tasks[-1]  # La última tarea creada
    task_id = last_task[0]  # El primer elemento es el ID

    # 2. ACT: Buscar esa tarea específica por ID
    task = get_task_by_id(task_id)

    # 3. ASSERT: Verificar que encontró la tarea correcta
    assert task is not None  # Que exista
    assert task[0] == task_id  # Que el ID coincida
    assert task[1] == title  # Que el título coincida
    assert task[2] == description  # Que la descripción coincida


def test_update_task():
    # 1. ARRANGE: Crear una tarea
    create_tasks("Título original", "Descripción original", None)

    # Obtener el ID de esa tarea
    all_tasks = get_all_tasks()
    task_id = all_tasks[-1][0]

    # 2. ACT: Actualizar la tarea
    new_title = "Título actualizado"
    new_description = "Descripción actualizada"
    update_task(task_id, new_title, new_description, None)

    # 3. ASSERT: Verificar que se actualizó
    updated_task = get_task_by_id(task_id)
    assert updated_task[1] == new_title  # ¿Qué debe ser?
    assert updated_task[2] == new_description  # ¿Qué debe ser?


def test_delete_task():
    create_tasks("Tarea a eliminar", "Esta tarea sera eliminada", None)

    all_tasks = get_all_tasks()
    task_id = all_tasks[-1][0]

    delete_task(task_id)

    deleted_task = get_task_by_id(task_id)
    assert deleted_task is None

def test_mark_as_completed():
    create_tasks("Tarea completada", "Esta tarea sera completada", None)

    all_tasks = get_all_tasks()
    task_id = all_tasks[-1][0]

    mark_as_completed(task_id)
    completed_task = get_task_by_id(task_id)
    assert completed_task is not None
    assert completed_task[5] == 1