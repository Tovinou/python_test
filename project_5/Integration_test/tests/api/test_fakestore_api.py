import requests # api-testning
import pytest

BASE_URL = "https://fakestoreapi.com"


def test_get_products_status_code():
    """
      GET /products ska returnera 200 lokalt.
    GitHub Actions förväntas kunna få 403.
    """

    response = requests.get(f"{BASE_URL}/products")

    # Lokalt ska detta vara 200
    # I GitHub Actions kan API:t blockera med 403
    assert response.status_code in [200, 403]

    # Om det INTE är 403 vill säkerställa att det är 200
    if response.status_code != 403:
        assert response.status_code == 200


def test_number_of_products():
    """
        Kontrollera antal produkter.
    """
    response = requests.get(f"{BASE_URL}/products")

    if response.status_code == 403:
        pytest.skip("FakeStoreAPI blocked GitHub Actions with 403")

    assert response.status_code == 200

    products = response.json()

    # FakeStoreAPI har normalt 20 produkter
    assert len(products) == 20


def test_product_contains_required_fields():
    """
    Kontrollera att produkten innehåller rätt fält.
    """
    response = requests.get(f"{BASE_URL}/products/1")

    if response.status_code == 403:
        pytest.skip("FakeStoreAPI blocked GitHub Actions with 403")

    assert response.status_code == 200

    product = response.json()

    assert "title" in product
    assert "price" in product
    assert "category" in product


def test_specific_product_data():
    """
        Kontrollera att rätt produktdata returneras.
    """
    response = requests.get(f"{BASE_URL}/products/1")

    if response.status_code == 403:
        pytest.skip("FakeStoreAPI blocked GitHub Actions with 403")

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == 1

    assert (
        product["title"]
        == "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops"
    )