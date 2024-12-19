import os
import json
import requests
print("DEBUG: pre_gen_project.py is running...")

def get_latest_version(package_name):
    """Fetch the latest version of a package from PyPI."""
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["info"]["version"]
    else:
        raise ValueError(f"Could not fetch version for {package_name}")

def main():
    """Update cookiecutter context dynamically."""
    # Fetch versions for the required packages
    packages = {
        "vivarium": "vivarium",
        "vivarium_public_health": "vivarium-public-health",
        "vivarium_cluster_tools": "vivarium-cluster-tools",
        "vivarium_inputs": "vivarium-inputs",
        "gbd_mapping": "gbd-mapping",
    }
    versions = {key: get_latest_version(value) for key, value in packages.items()}

    # Update the context dynamically
    context_file = os.path.join(os.getcwd(), "cookiecutter.json")
    with open(context_file, "r") as file:
        context = json.load(file)

    # Inject the fetched versions into the context
    for key, version in versions.items():
        context[f"{key}_version"] = version

    # Write updated context back to cookiecutter.json
    with open(context_file, "w") as file:
        json.dump(context, file, indent=4)

if __name__ == "__main__":
    main()
