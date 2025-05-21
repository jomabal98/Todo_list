from controllers import task_controller

def main_menu():
    while True:
        print("\n===== MENÚ DE TAREAS =====")
        print("1. Crear tarea")
        print("2. Ver todas las tareas")
        print("3. Ver tarea por ID")
        print("4. Actualizar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            title = input("Título: ")
            description = input("Descripción: ")
            task = task_controller.create_task(title, description)
            if not task:
                print(f"El campo nombre no puede estar vacío")
            else:
                print(f"Tarea creada con ID {task.id}")

        elif option == "2":
            tasks = task_controller.get_all_tasks()
            if not tasks:
                print(f"No hay tareas aún")
            for t in tasks:
                status = "✅ Completada" if t.completed else "❌ Pendiente"
                print(f"[{t.id}] {t.title} - {status}")

        elif option == "3":
            task_id = int(input("ID de la tarea: "))
            task = task_controller.get_task_by_id(task_id)
            if task:
                status = "✅ Completada" if task.completed else "❌ Pendiente"
                print(f"[{task.id}] {task.title}\nDescripción: {task.description}\nEstado: {status}")
            else:
                print("Tarea no encontrada.")

        elif option == "4":
            task_id = int(input("ID de la tarea a actualizar: "))
            title = input("Nuevo título (deja vacío para no cambiar): ")
            description = input("Nueva descripción (vacía para no cambiar): ")
            completed_input = input("¿Está completada? (s/n): ").lower()
            completed = True if completed_input == "s" else False if completed_input == "n" else None

            updated_task = task_controller.update_task(
                task_id,
                title or None,
                description or None,
                completed
            )

            if updated_task:
                print("✅ Tarea actualizada.")
            else:
                print("❌ Tarea no encontrada.")

        elif option == "5":
            task_id = int(input("ID de la tarea a eliminar: "))
            result = task_controller.delete_task(task_id)
            if result:
                print("🗑️ Tarea eliminada.")
            else:
                print("❌ Tarea no encontrada.")

        elif option == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")
