import requests
import json

# API asosiy manzili
BASE_URL = "http://localhost:8000"

# Test foydalanuvchisi ma'lumotlari
TEST_USER = {
    "email": "misha@example.com",
    "username": "misha",
    "password": "misha1123",
    "first_name": "misha",
    "last_name": "misha"
}

# Yangi post ma'lumotlari
TEST_POST = {
    "title": "Test Post",
    "content": "This is a test post content."
}


def print_response(response, title):
    """Responseni chiroyli ko'rinishda chop etish"""
    print(f"\n{'=' * 50}")
    print(f"{title.upper()}")
    print(f"Status Code: {response.status_code}")
    try:
        print("Response Body:")
        print(json.dumps(response.json(), indent=4))
    except ValueError:
        print("Response Text:")
        print(response.text)
    print(f"{'=' * 50}\n")


def test_register():
    """Foydalanuvchi registratsiyasini test qilish"""
    url = f"{BASE_URL}/api/auth/register/"
    data = TEST_USER.copy()
    data["password2"] = data["password"]  # Registratsiya uchun password2 kerak

    response = requests.post(url, json=data)
    print_response(response, "Register Test")

    return response


def test_login():
    """Login testi va token olish"""
    url = f"{BASE_URL}/api/auth/login/"
    data = {
        "email": TEST_USER["email"],
        "password": TEST_USER["password"]
    }

    response = requests.post(url, json=data)
    print_response(response, "Login Test")

    if response.status_code == 200:
        return response.json()["access"]
    return None


def test_protected_endpoint(token):
    """Himoyalangan endpointni test qilish"""
    url = f"{BASE_URL}/api/users/"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    print_response(response, "Protected Endpoint Test")


def test_create_post(token):
    """Post yaratish testi"""
    url = f"{BASE_URL}/api/posts/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=TEST_POST)
    print_response(response, "Create Post Test")

    if response.status_code == 201:
        return response.json()["id"]
    return None


def test_get_posts(token):
    """Postlarni olish testi"""
    url = f"{BASE_URL}/api/posts/"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    print_response(response, "Get Posts Test")


def test_update_post(token, post_id):
    """Postni yangilash testi"""
    url = f"{BASE_URL}/api/posts/{post_id}/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    updated_data = {
        "title": "Updated Test Post",
        "content": "This is updated content."
    }

    response = requests.put(url, headers=headers, json=updated_data)
    print_response(response, "Update Post Test")


# def test_delete_post(token, post_id):
#     """Postni o'chirish testi"""
#     url = f"{BASE_URL}/api/posts/{post_id}/"
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }
# 
#     response = requests.delete(url, headers=headers)
#     print_response(response, "Delete Post Test")


def main():
    print("Django REST Framework JWT API Test Skripti")
    print("=" * 50)

    # 1. Registratsiya testi
    register_response = test_register()

    # 2. Login testi va token olish
    token = test_login()
    if not token:
        print("Login testida xatolik! Token olinmadi.")
        return

    # 3. Himoyalangan endpoint testi
    test_protected_endpoint(token)

    # 4. Post yaratish testi
    post_id = test_create_post(token)
    if not post_id:
        print("Post yaratish testida xatolik! Post ID olinmadi.")
        return

    # 5. Postlarni olish testi
    test_get_posts(token)

    # 6. Postni yangilash testi
    test_update_post(token, post_id)

    # 7. Postni o'chirish testi
    # test_delete_post(token, post_id)

    print("Barcha testlar muvaffaqiyatli yakunlandi!")


if __name__ == "__main__":
    main()