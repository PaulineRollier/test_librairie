import os
import sys

if not os.getenv("COMPILED_LIB_TEST", False) == "true":
    my_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, my_path + "/../")

print("Path : " + str(sys.path))
