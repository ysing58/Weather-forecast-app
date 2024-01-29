import requests


def get_data(city, days, type):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=141710af2113bab9f55ef73e1bcd33d5"
    response = requests.get(url)
    data = response.json()
    filter_data = data['list']
    filtered_data = filter_data[:8*days]
    return filtered_data



if __name__ == "__main__":
    info = get_data('Tokyo', 3, 'Temperature')
    print(info)
