# Projects-using-APIs
Projects integrate external APIs such as Sheety, OpenTrivia, OpenWeatherMap, Nutritionix, and Amadeus for real-time data.

## Technologies & Libraries Used
- requests – For making HTTP requests to various APIs.
- tkinter – For building graphical user interfaces (GUI).
- dotenv – For loading environment variables from a .env file.
- html – For decoding HTML-encoded text.
- twilio – For sending SMS notifications and WhatsApp messages.
- datetime – For handling date and time operations.
- os – For accessing environment variables and interacting with the operating system.
- smtplib – For sending emails .

## Project Descriptions

### Fligth Deals 🛫
This project retrieves flight deal data from a Google Sheet via the Sheety API. It updates missing IATA codes using a Amadeus API, finds the cheapest flights based on user-defined criteria, and sends notifications via SMS and email if a low price is found. The notifications can be sent to multiple recipients.
### GUI Quizz 🤔
A GUI-based trivia quizz game that fetches true/false questions from the OpenTrivia Database API. The game uses Tkinter for its interface and manages questions and scoring.
### Rain Alert ☔
This project fetches weather forecast data from the OpenWeatherMap API to determine if rain is expected. If rain is forecasted (based on weather condition codes), the app sends an SMS alert via Twilio.
### Workout Tracking👟
A workout tracker that uses the Nutritionix API to convert a natural language exercise description into structured workout data. The project logs details such as the exercise name, duration, and calories burned into a Google Sheet via the Sheety API.
