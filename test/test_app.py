import requests

def test_service_a():
    response = requests.get("http://service-a:5000")
    assert response.status_code == 200
    print("Service A is up and running!")

def test_service_b():
    response = requests.get("http://service-b:5000")
    assert response.status_code == 200
    print("Service B is up and running!")

if __name__ == "__main__":
    test_service_a()
    test_service_b()
