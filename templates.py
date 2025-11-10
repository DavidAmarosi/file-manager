"""
    if __name__ == "__main__":

    GIT 
    git config --global user.name "Your Name"
    git config --global user.email "your@email.com"
    git config --global init.defaultBranch main

    git init                # Initialize a new repo
    git clone <url>         # Copy a remote repo to local

    git status              # Show changes
    git log                 # Commit history
    git log --oneline       # Short history

    git add <file>          # Stage file
    git add .               # Stage all
git commit -m "INITIAL PUSH"               # Commit
git commit -m                # Commit


git push -u origin main     # First push
git push                    # Next pushes

    git branch              # List branches
    git branch <name>       # Create new branch
    git checkout <name>     # Switch branch (older syntax)
    git switch <name>       # Better way for switching
    git switch -c <name>    # Create + switch

    git pull               # Fetch + merge from remote
    git fetch              # Fetch only (no merge)

    
    git clone https://github.com/DavidAmarosi/file-manager.git
    
    To see the remote Git URL of the current repository, use:
    git remote -v

    python -m venv venv


    TERSR
"""



# +=================+
# | CLASS           |
# +=================+

class MyClass:
    def __init__(self, attr1, attr2, attr3, attr4, attr5, attr6, attr7, attr8):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = attr4
        self.attr5 = attr5
        self.attr6 = attr6
        self.attr7 = attr7
        self.attr8 = attr8

super().__init__(attr1, attr2)



# +=================+
# | ERROR HANDELING |
# +=================+

try:
    # Code that might raise an exception
    print("Enter your code here")

# Catch any exception
except Exception as e:
    print(f"Unexpected error: {e}")

# Common Python exceptions individually
except AttributeError as e:
    print(f"AttributeError: {e}")
except TypeError as e:
    print(f"TypeError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")
except IndexError as e:
    print(f"IndexError: {e}")
except KeyError as e:
    print(f"KeyError: {e}")
except NameError as e:
    print(f"NameError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except IOError as e:
    print(f"IOError: {e}")
except ImportError as e:
    print(f"ImportError: {e}")
except StopIteration as e:
    print(f"StopIteration: {e}")
except AssertionError as e:
    print(f"AssertionError: {e}")
except MemoryError as e:
    print(f"MemoryError: {e}")
except OverflowError as e:
    print(f"OverflowError: {e}")

