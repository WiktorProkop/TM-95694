import json
import os

def solve_task():

    package = "io.appium.android.apis"
    main_activity = "io.appium.android.apis.ApiDemos"


    capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "appPackage": package,
        "appActivity": main_activity,
        "deviceName": "emulator-5554",
        "noReset": True
    }


    try:
        with open('51_caps.json', 'w') as json_file:
            json.dump(capabilities, json_file, indent=4)
        

        print(f"Sukces! Wykryto: {package} / {main_activity}")
    except Exception as e:
        print(f"Błąd zapisu: {e}")

if __name__ == "__main__":
    solve_task()
