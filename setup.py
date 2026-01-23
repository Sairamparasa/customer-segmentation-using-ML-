#!/usr/bin/env python3
"""
Setup script for Customer Segmentation Project
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def install_requirements():
    """Install required packages"""
    try:
        print("Installing required packages...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True)
        print("✓ All packages installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
        sys.exit(1)

def verify_files():
    """Verify that all required files exist"""
    required_files = [
        'data/customer_segmentation.csv',
        'models/kmeans_model.pkl',
        'models/scaler.pkl',
        'src/segmentation_app.py',
        'notebooks/EDA.ipynb'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("Error: Missing required files:")
        for file_path in missing_files:
            print(f"  - {file_path}")
        sys.exit(1)
    
    print("✓ All required files found")

def main():
    """Main setup function"""
    print("Setting up Customer Segmentation Project...")
    print("=" * 50)
    
    check_python_version()
    verify_files()
    install_requirements()
    
    print("=" * 50)
    print("✓ Setup completed successfully!")
    print("\nTo run the application:")
    print("  python run_app.py")
    print("\nOr manually:")
    print("  cd src")
    print("  streamlit run segmentation_app.py")

if __name__ == "__main__":
    main()