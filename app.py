# Simple Python script to greet users and display Git workflow steps

def show_welcome():
    print("Welcome to Git Practice Handbook!")
    print("---------------------------------")

def show_steps():
    steps = [
        "1. Create a feature branch",
        "2. Commit your changes",
        "3. Push to GitHub",
        "4. Open a Pull Request (PR)",
        "5. Review and Merge into main"
    ]
    print("Git Workflow Steps:")
    for step in steps:
        print(step)

if __name__ == "__main__":
    show_welcome()
    show_steps()

