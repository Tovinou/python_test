import pytest
import requests

BASE_URL = "https://fakestoreapi.com"

def test_get_products_200():
    """
    Test case 1 (G): GET /products returns status code 200.
    Note: This is expected to fail in GitHub Actions with 403 due to bot protection,
    which is the desired outcome for the assignment.
    """
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200

def test_product_count():
    """
    Test case 2 (VG): Verify that 20 products are returned.
    """
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    products = response.json()
    assert len(products) == 20

def test_product_structure():
    """
    Test case 3 (VG): Verify a specific product has correct fields.
    """
    response = requests.get(f"{BASE_URL}/products/1")
    assert response.status_code == 200
    product = response.json()
    
    assert "title" in product
    assert "price" in product
    assert "category" in product
    assert isinstance(product["title"], str)
    assert isinstance(product["price"], (int, float))

def test_specific_product_data():
    """
    Test case 4 (VG): Verify specific product ID returns correct data.
    """
    response = requests.get(f"{BASE_URL}/products/1")
    assert response.status_code == 200
    product = response.json()
    
    assert product["id"] == 1
    assert product["title"] == "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops"
