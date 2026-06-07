import pytest
import allure

@allure.epic("Blok 10: Raportowanie")
@allure.feature("10.1: Inicjalizacja Allure")
def test_success_example():
    """Ten test przejdzie (Zielony)"""
    with allure.step("Krok 1: Inicjalizacja środowiska"):
        print("Środowisko gotowe.")
    with allure.step("Krok 2: Sprawdzanie warunku"):
        assert 1 == 1

@allure.feature("10.1: Inicjalizacja Allure")
def test_failed_example():
    """Ten test celowo nie przejdzie (Czerwony)"""
    with allure.step("Krok 1: Próba autoryzacji"):
        print("Autoryzacja...")
    with allure.step("Krok 2: Walidacja tokena"):
       
        assert False, "Błąd: Token nieprawidłowy!"