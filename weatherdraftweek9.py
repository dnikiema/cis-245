import requests
welcome = input("Welcome to Weather Report Program: Press Enter to Continue")
def by_city():
    city = input('Please Enter Your City Name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=c1fd8d298201f0b37f0a5f1f30f1dadd&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Thank you for using the program. Good Bye!")
        exit()
def by_zip():
    zip_code = int(input('Please Enter Your Zip code: '))
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=c1fd8d298201f0b37f0a5f1f30f1dadd'.format(zip_code)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Thank you for using the program. Good Bye!")
        exit()
def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    press = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Pressure : {} hPa'.format(press))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))
def main():
    while True:
        answer = input("Want to know the weather? Please type zip code or city: ")
        if answer == 'city':
            try:
                print(" Connection was successful.")
                by_city()

            except Exception:
                print(" city was invalid. please Try again")
                by_city()

        if answer == 'zip code':
            try:
                print("Connection was successful.")
                by_zip()

            except Exception:
                print("zip code was invalid. please Try again")
                by_zip()

        else:
            print("not one of the options. please Try again.")
main()
yes