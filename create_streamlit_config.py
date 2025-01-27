import os

# Create the .streamlit folder
os.makedirs(".streamlit", exist_ok=True)

# Define the content of the config.toml file
config_content = """
[theme]
base="light"
primaryColor="#403d58"
secondaryBackgroundColor="#e4efe9"
textColor="#333333"
font="serif"
wideMode = true
"""

# Write the content to the config.toml file
with open(".streamlit/config.toml", "w") as config_file:
    config_file.write(config_content)

print("The .streamlit folder and config.toml file have been created!")