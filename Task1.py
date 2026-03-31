def display_menu():
    """Displays the main menu options to the user."""
    print("\n" + "="*25)
    print("📋 TO-DO LIST MENU")
    print("="*25)
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")
    print("="*25)

def main():
    tasks = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            if not tasks:
                print("\n✨ Your to-do list is currently empty!")
            else:
                print("\n--- Your Tasks ---")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")
                    
        elif choice == '2':
            new_task = input("\nEnter the task description: ")
            tasks.append(new_task)
            print(f"✅ '{new_task}' has been added to your list.")
            
        elif choice == '3':
            if not tasks:
                print("\n⚠️ No tasks to remove. Your list is empty.")
                continue
                
            try:
                task_num = int(input("\nEnter the task number you want to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"🗑️ '{removed_task}' has been removed.")
                else:
                    print("❌ Invalid task number. Please try again.")
            except ValueError:
                print("❌ Please enter a valid numerical digit.")
                
        elif choice == '4':
            print("\nExiting the To-Do List. Have a productive day! 👋")
            break
            
        else:
            print("\n❌ Invalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()

