import requests
import smtplib
MY_EMAIL = "Your Email"
MY_PASSWORD = "Your Email Password Or If you using Gmail Then App Key"
parameter={
    "lat":"16.667499", # Your latitude
    "lon":"Your longitude",# Your longitude
    "exclude":"current,minutely,daily",
    "appid":"af83206df502bdace12cf1e2d57933f0"
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameter)
response.raise_for_status()
weather_data=response.json()

weather_slice=weather_data["hourly"][:12]

will_rain=False
for hour_data in weather_slice:
    codition_code=hour_data["weather"][0]["id"]
    if int(codition_code)<700:
        will_rain=True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg="Subject:Today is Rain Weather\n\nBring the umbella")

   

   