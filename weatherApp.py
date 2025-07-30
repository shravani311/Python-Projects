#Install requests using :- pip install request
import requests
def get_weather(city):
    API_KEY="79e7ae0e0c9149265b5ce7d435b69745"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params={'q':city, 'appid':API_KEY,'units':'metric'}
    try:
        response=requests.get(BASE_URL,params=params)
        response.raise_for_status()
        data=response.json()
        print(f"Weather in {data['name']}, {data['sys']['country']}")
        print(f"Temperature : {data['main']['temp']} *C")
        print(f"Condition : {data['weather'][0]['description'].capitalize()}")
        print(f"Humidty : {data['main']['humidity']}%")
        print(f"Wind Speed : {data['wind']['speed']} m/s")
    
    except requests.exceptions.HTTPError :
        print("City not found ! Invalid API ID")
    except Exception as e:
        print(f"Something went wrong : {e}")

if __name__=="__main__":
    while True :
        print("\n=====Weather App=====")
        print("1.Get Weather")
        print("2.Exit")
        ch=int(input("Enter your choice :- "))
        if ch==1:
            city_name=input("Enter city name : ")
            get_weather(city_name)
        elif ch==2:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")