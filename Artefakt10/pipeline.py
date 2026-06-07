import os
import shutil
import subprocess
import time

def run_command(command):
    subprocess.run(command, shell=True)

def run_pipeline():
    run_command("docker compose up -d")
    time.sleep(2)

    if os.path.exists("allure-results"):
        shutil.rmtree("allure-results")
    os.makedirs("allure-results", exist_ok=True)

    run_command("python -m pytest . --alluredir=allure-results")

    env_properties = (
        f"Pipeline.Status=SUCCESS\n"
        f"Execution.Time={time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Execution.Type=Automated Master Script\n"
        f"Infrastructure=Docker (Hello-World)\n"
        f"Platform={os.name}\n"
        f"Build.Engine=Python Subprocess"
    )
    with open("allure-results/environment.properties", "w") as f:
        f.write(env_properties)

    allure_path = ".\\allure-2.39.0\\bin\\allure.bat"
    run_command(f"{allure_path} generate allure-results -o allure-report --clean")

    run_command("docker compose down")

if __name__ == "__main__":
    run_pipeline()