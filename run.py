import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from custom_bikes.main import menu_principal

if __name__ == "__main__":
    menu_principal()


