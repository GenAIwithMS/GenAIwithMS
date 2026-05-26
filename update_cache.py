import re
import time

def update_readme():
    file_path = "README.md"
    
    # Read the current README content
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Generate a new Unix timestamp
    new_version = str(int(time.time()))

    # Find '&v=<number>' and replace it with the new timestamp
    updated_content = re.sub(r"&v=\d+", f"&v={new_version}", content)

    # Write the fresh URLs back and print the result for the bash script
    if content != updated_content:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(updated_content)
        # Print the version so the GitHub Action can read it
        print(f"v{new_version}")
    else:
        print("unchanged")

if __name__ == "__main__":
    update_readme()
