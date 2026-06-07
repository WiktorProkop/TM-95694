import pytest
import allure

@allure.epic("Blok 10: Raportowanie")
@allure.feature("10.3: Dowody wizualne (Załączniki)")
def test_failure_with_attachments():
    """Test ze zrzutem ekranu (Symulacja)"""
    
    
    api_data = "{ 'status': 'fail', 'error': 'ElementNotVisibleException' }"
    
   
    allure.attach(
        "Tu byłby screen błędu z telefonu", 
        name="Screenshot_Error_01", 
        attachment_type=allure.attachment_type.TEXT
    )
    
    allure.attach(
        api_data, 
        name="API_Response", 
        attachment_type=allure.attachment_type.JSON
    )

    with allure.step("Krok 1: Próba kliknięcia w przycisk 'Zapisz'"):
        print("Log: ElementNotVisibleException")
        
        assert False, "Failed: Test padł, ale mamy dowody! Log: ElementNotVisibleException"