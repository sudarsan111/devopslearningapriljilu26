import sys

# Get the name from the command line argument if provided, otherwise default to "jilu"
name = sys.argv[1] if len(sys.argv) > 1 else "jilu"

print(f"Hello {name}!")