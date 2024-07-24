import os

# Set the environment variable
os.environ['OPT_DIR'] = "/opt"

# Get the environment variable
opt_dir = os.getenv('OPT_DIR')
print(f"The directory is {opt_dir}")

# Use the environment variable
if opt_dir:
    os.chdir(opt_dir)
    print(f"Changed directory to {opt_dir}")
else:
    print("Failed to get OPT_DIR environment variable")
