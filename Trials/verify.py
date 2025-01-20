import importlib
import sys


libraries = {
    "numpy": "version",
    "scipy": "version",
    "pandas": "version",
    "matplotlib": "version",
    "seaborn": "version",
    "sklearn": "version",
    "spectral": "version",
    "opencv-python-headless": "version",
    "plotly": "__version__",
    "torch": "version",
    "torchvision": "version",
    "tensorflow": "__version__",
    "h5py": "__version__",
}

def test_libraries():
    all_success = True
    print("Testing library installations...\n")
    for library, version_attr in libraries.items():
        try:
            module = importlib.import_module(library.replace('-', '_'))
            version = getattr(module, version_attr, "Unknown version")
            print(f"{library}: Installed (Version: {version})")
        except ImportError:
            print(f"{library}: Not Installed")
            all_success = False
        except Exception as e:
            print(f"{library}: Error occurred - {e}")
            all_success = False

    print("\nTest Result:")
    if all_success:
        print("All libraries are installed successfully!")
    else:
        print("Some libraries are missing or have errors.")

if __name__ == "__main__":
    test_libraries()
