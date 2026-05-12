import requests

BASE_URL = "https://fakestoreapi.com"


def _get_ok(path: str) -> requests.Response:
    url = f"{BASE_URL}{path}"
    r = requests.get(url, timeout=30)
    assert r.status_code == 200, f"GET {path} expected 200, got {r.status_code}"
    return r


def test_get_products_status_code():
    """GET /products returns 200 (CI may get 403 and fail the job per assignment)."""
    _get_ok("/products")


def test_number_of_products():
    data = _get_ok("/products").json()
    assert len(data) == 20


def test_product_contains_required_fields():
    product = _get_ok("/products/1").json()
    assert "title" in product and "price" in product and "category" in product


def test_specific_product_data():
    product = _get_ok("/products/1").json()
    assert product["id"] == 1
    assert (
        product["title"]
        == "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops"
    )
