import subprocess

def git_save(commit_message="Auto-commit from Python script"):
    try:
        # Add all changes to staging
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit the changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push to the remote repository
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print("Changes successfully committed and pushed to GitHub.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Call the function with a custom commit message
git_save("Updated project files")
