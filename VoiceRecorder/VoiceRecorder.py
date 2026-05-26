# the dictionary store ( for the data)

project_vault = {
    "Voice Recorder": "In Progress",
    "Folder Automation": "Completed"
    }

def show_projects():  # function to show the projects in the vault
    print("\n--- CURRENT PROJECTS ---")
    if not project_vault:
        print("Your vault is empty!")
    for project, status in project_vault.items():
        print(f"{project} [{status}]")
    print("-" * 25)

def add_project():
    print("\n--- ADD NEW PROJECT ---")
    name = input("Enter project name: ")
    if name.strip() == "":
        print("Project name cannot be blank!")
        return

    project_vault[name] = "Planned"
    print(f"Success! Added {name} to your vault.")


while True:
    print("\n===== TASHWILL's APP =====")
    print("1. View ALl Projects")
    print("2. Add New Project")
    print("3. Exit Application")
    print("===========================")

    choice = input("Select an option (1-3): ")

    if choice == "1":
        show_projects()
    elif choice == "2":
        add_project()
    elif choice == "3":
        print("\nShutting down application. ")
        break
    else:
        print("\n[Invalid SELECTION] Please press 1, 2, or 3")
    