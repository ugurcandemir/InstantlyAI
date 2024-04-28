
import requests
import json

class Instantly : 

    def __init__(self , api_key):
        
        self.api_key = api_key

    def authenticate(self) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/authenticate?api_key={api_key}"

        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)

        return response

                
    
class Campaign(Instantly) :

    def __init__(self , api_key ) :

        super().__init__(api_key)

    def list_campaigns(self) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/campaign/list?api_key={api_key}"

        headers = {
        'Content-Type': 'application/json'
        }


        response = requests.request("GET", url, headers=headers)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def get_campaign_name(self , campaign_id) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/campaign/get/name?api_key={api_key}&campaign_id={campaign_id}"

        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def get_campaign_status(self , campaign_id) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/campaign/get/status?api_key={api_key}&campaign_id={campaign_id}"

        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def set_campaign_name(self , campaign_id , new_name) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/campaign/set/name"

        payload = json.dumps({
        "api_key": api_key,
        "campaign_id": campaign_id,
        "name": new_name
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
        
    def get_accounts_of_campaign(self , campaign_id) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/campaign/get/accounts?api_key={api_key}&campaign_id={campaign_id}"

        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def set_accounts_of_campaign(self , campaign_id , account_list) :       

        api_key = self.api_key


        url = "https://api.instantly.ai/api/v1/campaign/set/accounts"

        payload = json.dumps({
        "api_key": api_key,
        "campaign_id": campaign_id,
        "account_list": account_list       
        })
        
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

        
    def add_account_to_campaign(self , campaign_id , email) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/campaign/add/account"


        payload = json.dumps({
        "api_key": api_key,
        "campaign_id": campaign_id,
        "email": email
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def remove_account_from_campaign(self , campaign_id , email) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/campaign/remove/account"


        payload = json.dumps({
        "api_key": api_key,
        "campaign_id": campaign_id,
        "email": email
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def set_campaign_schedule(self , campaign_id , email) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/campaign/set/schedules"

        payload = json.dumps({
        "api_key": api_key,
        "campaign_id": campaign_id,
        "start_date": "2023-01-01",
        "end_date": "false",
        "schedules": [
            {
            "name": "Monday to Friday - 8am to 5pm Eastern",
            "days": {
                "1": True,
                "2": True,
                "3": True,
                "4": True,
                "5": True
            },
            "timezone": "America/Detroit",
            "timing": {
                "from": "08:00",
                "to": "17:00"
            }
            }
        ]
        })

        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def launch_campaign(self , campaign_id ) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/campaign/launch"

        payload = json.dumps({
        "api_key": api_key,
        "campaign_id": campaign_id
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def pause_campaign(self , campaign_id ) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/campaign/pause"

        payload = json.dumps({
        "api_key": api_key,
        "campaign_id": campaign_id
        })
        

        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

    
        
    


        


class Analytics(Instantly) :

    def __init__(self , api_key ) :

        super().__init__(api_key)

    def get_campaign_summary(self , campaign_id) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/analytics/campaign/summary?api_key={api_key}&campaign_id={campaign_id}"
  
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def get_campaign_summary(self , campaign_id , start_date , end_date) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/analytics/campaign/summary?api_key={api_key}&campaign_id={campaign_id}&start_date={start_date}&end_date={end_date}"
  
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None





class Lead(Instantly) :

    def __init__(self , api_key ) :

        super().__init__(api_key)


    def add_leads_to_campaign(self , campaign_id , skip_if_in_workspace , leads) : 

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/lead/add"

        payload = json.dumps({
          "api_key": api_key ,
          "campaign_id": campaign_id,
          "skip_if_in_workspace": skip_if_in_workspace,
          "leads": leads
        })

        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def get_or_search_for_lead(self , campaign_id , email) : 

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/lead/get?api_key={api_key}&campaign_id={campaign_id}&email={email}"

        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)
        
        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def delete_leads_from_campaign(self , campaign_id , delete_all_same_domain , delete_list) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/lead/delete"


        payload = json.dumps({
          "api_key": api_key ,
          "campaign_id": campaign_id,
          "delete_all_from_company": delete_all_same_domain,
          "delete_list": delete_list
        })

        headers = {
          'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    
    def update_lead_status(self , campaign_id , email , new_status) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/lead/update/status"

        payload = json.dumps({
          "api_key": api_key ,
          "campaign_id": campaign_id,
          "email": email,
          "new_status": new_status
        })

        headers = {
          'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)


        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
    def lead_variable_set(self , campaign_id , email , variables) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/lead/data/set"

        payload = json.dumps({
          "api_key": api_key ,
          "campaign_id": campaign_id,
          "email": email,
          "variables": variables
        })
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None


    def lead_variable_update(self , campaign_id , email , variables) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/lead/data/update"

        payload = json.dumps({
          "api_key": api_key ,
          "campaign_id": campaign_id,
          "email": email,
          "variables": variables
        })
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None


    def lead_variable_delete(self , campaign_id , email , variables) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/lead/data/update"

        payload = json.dumps({
          "api_key": api_key ,
          "campaign_id": campaign_id,
          "email": email,
          "variables": variables
        })
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

        


class Blocklist(Instantly) :

    
    def __init__(self , api_key ) :

        super().__init__(api_key)


    def add_entries_to_blocklist(self ,  entries) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/blocklist/add/entries"


        payload = json.dumps({
          "api_key": api_key ,
          "entries": entries
        })

        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def remove_entries_from_blocklist(self ,  entries) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/blocklist/delete/entries"

        payload = json.dumps({
          "api_key": api_key ,
          "entries": entries
        })
        
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None




class Account(Instantly) :

    def __init__(self , api_key ) :

        super().__init__(api_key)


    def list_accounts(self ) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/account/list?api_key={api_key}"

        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)
        
        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
        

    def check_account_vitals(self , accounts) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/account/test/vitals"

        payload = json.dumps({
            "api_key": api_key,
            "accounts": accounts
        })
                
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def get_account_status(self , email ) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/account/status?api_key={api_key}&email={email}"

        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)
        
        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def enable_warmup(self , email ) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/account/warmup/enable"

        payload = json.dumps({
            "api_key": api_key,
            "email": email
        })
                
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def pause_warmup(self , email) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/account/warmup/pause"


        payload = json.dumps({
            "api_key": api_key,
            "email": email
        })
                
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def mark_accounts_as_fixed(self , email ) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/account/mark_fixed"

        payload = json.dumps({
            "api_key": api_key,
            "email": email
        })
                
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def delete_account(self , email ) :

        api_key = self.api_key

        url = "https://api.instantly.ai/api/v1/account/delete"

        payload = json.dumps({
            "api_key": api_key,
            "email": email
        })
                
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

  

class Unibox(Instantly) :

    def __init__(self , api_key ) :

        super().__init__(api_key)


    def emails_list(self ) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/unibox/emails/?api_key={api_key}"

        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)
        
        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def emails_count_unread(self ) :

        api_key = self.api_key

        url = f"https://api.instantly.ai/api/v1/unibox/emails/count/unread?api_key={api_key}"

        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)
        
        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            campaign_data = json.loads(response.text)
            return campaign_data
        else:
            # If the request was not successful, print an error message
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def threads_mark_as_unread(self ) :

        pass

