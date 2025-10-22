import sys
import os
from scripts import bookmarks, cookies, formhistory, history

# ---------------- Helper Functions ----------------
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

# wait for input helper function
def wait():
    input("Press any key")

def exit_script():
    print("Exiting...")
    sys.exit(0)

# Hardcoded path to the browser files
firefox_folder = os.path.join(os.path.dirname(__file__), "browser_files")

# ---------------- Analysis Functions ----------------
def analyze_bookmarks():
    print("\nRunning bookmark analysis")
    file_path = os.path.join(firefox_folder, "places.sqlite") 
    if os.path.exists(file_path):
        bookmarks.analyze_bookmarks(file_path)
    else:
        print("places.sqlite file not found")
        wait()
        clear_screen() 

# Cookies
def analyze_cookies():
    print("\nRunning cookies analysis") 
    file_path = os.path.join(firefox_folder, "cookies.sqlite") 
    if os.path.exists(file_path):
        cookies.analyze_cookies(file_path)
    else:
        print("cookies.sqlite file not found")
        wait() 
        clear_screen()

# Form History
def analyze_form_history():
    print("\nRunning form history analysis")
    file_path = os.path.join(firefox_folder, "formhistory.sqlite") 
    if os.path.exists(file_path): 
        formhistory.analyze_form_history(file_path)
    else:
        print("formhistory.sqlite file not found")
        wait()
        clear_screen()

# History
def analyze_history():
    print("\nRunning history analysis")
    file_path = os.path.join(firefox_folder, "places.sqlite") 
    if os.path.exists(file_path): 
        history.analyze_history(file_path)
    else: 
        print("No supported files found")
        wait()
        clear_screen()

# ---------------- Main Loop ----------------
def main():
    clear_screen()

    menu_actions = {
            "1": analyze_bookmarks,
            "2": analyze_cookies,
            "3": analyze_form_history,
            "4": analyze_history,
            "5": exit_script
    }

    while True:
        print("\nBen's Browser Artifact Analyzer")
        print("1. Analyze Bookmarks")
        print("2. Analyze Cookies")
        print("3. Analyze Form History")
        print("4. Analyze History")
        print("5. Exit")
        choice = input("Enter choice: ").strip()
        action = menu_actions.get(choice)

        if action:
            action()
        else:
            print("Invalid Choice, try again.")
            wait()
            clear_screen()

if __name__ == "__main__":
    main()

