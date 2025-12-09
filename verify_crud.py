import requests
import time
import subprocess
import sys

# Base URL
BASE_URL = "http://127.0.0.1:8000"

def test_crud():
    # 1. Create an Item (POST)
    print("Testing POST /items/ ...")
    item_data = {"id": 1, "name": "Test Item", "price": 10.5, "is_offer": True}
    response = requests.post(f"{BASE_URL}/items/", json=item_data)
    if response.status_code == 200:
        print("POST success:", response.json())
    else:
        print("POST failed:", response.text)
        sys.exit(1)

    # 2. Read all Items (GET)
    print("\nTesting GET /items/ ...")
    response = requests.get(f"{BASE_URL}/items/")
    if response.status_code == 200:
        print("GET all success:", response.json())
        assert len(response.json()) > 0
    else:
        print("GET all failed:", response.text)
        sys.exit(1)

    # 3. Read specific Item (GET)
    print("\nTesting GET /items/1 ...")
    response = requests.get(f"{BASE_URL}/items/1")
    if response.status_code == 200:
        print("GET one success:", response.json())
        assert response.json()["name"] == "Test Item"
    else:
        print("GET one failed:", response.text)
        sys.exit(1)

    # 4. Update an Item (PUT)
    print("\nTesting PUT /items/1 ...")
    update_data = {"id": 1, "name": "Updated Item", "price": 20.0, "is_offer": False}
    response = requests.put(f"{BASE_URL}/items/1", json=update_data)
    if response.status_code == 200:
        print("PUT success:", response.json())
        assert response.json()["name"] == "Updated Item"
    else:
        print("PUT failed:", response.text)
        sys.exit(1)

    # Verify update
    print("Verifying update...")
    response = requests.get(f"{BASE_URL}/items/1")
    assert response.json()["price"] == 20.0

    # 5. Delete an Item (DELETE)
    print("\nTesting DELETE /items/1 ...")
    response = requests.delete(f"{BASE_URL}/items/1")
    if response.status_code == 200:
        print("DELETE success:", response.json())
    else:
        print("DELETE failed:", response.text)
        sys.exit(1)

    # Verify deletion
    print("Verifying deletion...")
    response = requests.get(f"{BASE_URL}/items/1")
    if response.status_code == 404:
        print("Verification success: Item not found as expected.")
    else:
        print("Verification failed: Item still exists or other error.", response.status_code)
        sys.exit(1)

if __name__ == "__main__":
    # Wait for server to start if running via a workflow, but here I'll assume it's running or I'll run it separately.
    # For this script to work, the server must be up.
    try:
        test_crud()
        print("\nAll CRUD operations verified successfully!")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to server. Is it running?")
        sys.exit(1)
