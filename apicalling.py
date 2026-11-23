#handling api will run on sandbox or vs code
import requests

def fetch_random_user_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"] ["username"]
        user_country = user_data["location"] ["country"]
        return user_name , user_country
    else:
        raise Exception("fail to fetch user data") # for errors  
        
def main():
    try:
        user_name , user_country =  fetch_random_user_api()
        print(f"Username : {user_name}, \n Country : {user_country}")
    except Exception as e :  # e is short form of exception and called as casting
        print(str(e))
           


if __name__ == "__main__":
    main() 
