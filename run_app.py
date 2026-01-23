#!/usr/bin/env python3
"""
Script to run the Customer Segmentation Streamlit app
"""

import os
import sys
import subprocess

def main():
    """Run the Streamlit application"""
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the Streamlit app
    app_path = os.path.join(script_dir, 'src', 'segmentation_app.py')
    
    # Check if the app file exists
    if not os.path.exists(app_path):
        print(f"Error: App file not found at {app_path}")
        sys.exit(1)
    
    # Run the Streamlit app
    try:
        print("Starting Customer Segmentation App...")
        print(f"App will open in your browser at: http://localhost:8501")
        subprocess.run(['streamlit', 'run', app_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running the app: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nApp stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()