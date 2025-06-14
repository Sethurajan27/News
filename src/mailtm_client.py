import requests
import time

class MailTMClient:
    def __init__(self):
        self.base_url = 'https://api.mail.tm'
        self.session = requests.Session()
        self.account = self.create_account()
        self.token = self.get_token()

    def create_account(self):
        domain = self.session.get(f'{self.base_url}/domains').json()['hydra:member'][0]['domain']
        email = f'test{int(time.time())}@{domain}'
        password = 'UserPassword123!'
        response = self.session.post(f'{self.base_url}/accounts', json={'address': email, 'password': password})
        return {'email': email, 'password': password}

    def get_token(self):
        response = self.session.post(f'{self.base_url}/token', json=self.account)
        return response.json()['token']

    def wait_for_email(self, subject_keyword, timeout=300):
        headers = {'Authorization': f'Bearer {self.token}'}
        start_time = time.time()
        while time.time() - start_time < timeout:
            messages = self.session.get(f'{self.base_url}/messages', headers=headers).json()['hydra:member']
            for message in messages:
                if subject_keyword in message['subject']:
                    msg = self.session.get(f"{self.base_url}/messages/{message['id']}", headers=headers).json()
                    return msg['text']
            time.sleep(5)
        raise TimeoutError("Email not received within timeout period.")
