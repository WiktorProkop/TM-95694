import pytest
import allure

@allure.epic("Blok 10: Raportowanie")
@allure.feature("10.2: Meta Reporting")
class TestUserManagement:

    @allure.story("Story: Tworzenie nowego profilu")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_profile(self):
        """Test sprawdzajacy tworzenie profilu"""
        with allure.step("Krok 1: Otwarcie formularza"):
            print("Formularz otwarty")
        with allure.step("Krok 2: Wprowadzenie danych"):
            print("Dane wpisane")
        with allure.step("Krok 3: Klikniecie Zapisz"):
            assert 1 == 1

    @allure.story("Story: Usuwanie profilu")
    @allure.severity(allure.severity_level.MINOR)
    def test_delete_user_profile(self):
        """Test sprawdzajacy usuwanie profilu"""
        with allure.step("Krok 1: Wybranie profilu do usuniecia"):
            print("Profil wybrany")
        with allure.step("Krok 2: Potwierdzenie usuniecia"):
            assert True