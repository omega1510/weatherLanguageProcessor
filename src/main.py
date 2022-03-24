#!/usr/bin/env python3

from random import choice, randint

days = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
    "today",
    "tomorrow",
]


def get_forecast(day, time, place, question):

    forecast = ["sunny", "cloudy", "rainy", "snowy", "stormy", "windy"]

    if "when" in question:
        for element in question:
            for condition in forecast:
                if element[:3] in condition:
                    return f"It will be {condition} {choice(days).capitalize()} {choice(times)} in {place.capitalize()}."

    for word in ["weather", "forecast"]:
        if word in question:
            return f"The weather for {(day + ' ' + time) if time != 'now' else day} in {place.capitalize()} is {choice(forecast)}."

    for word in ["temperature", "temp", "temperatures", "temperatures"]:
        if word in question:
            return f"The temperature for {(day + ' ' + time) if time != 'now' else day} in {place.capitalize()} is {randint(60, 110)} degrees."


def get_question():
    question = input("Query: ").lower().strip()
    punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    for char in question:
        if char in punctuation:
            question = question.replace(char, "")

    question = question.split()  # splits the string into a list of words

    return question


def get_day(question: list):

    for element in question:
        if element in days:
            return element
        else:
            return "today"


times = ["morning", "afternoon", "evening", "night", "now"]


def get_time(question: list):
    for element in question:
        if element in times:
            return element
        else:
            return "now"


def get_place(question: list):
    for index, element in enumerate(question):
        if element in ["in", "at", "near", "nearby", "nearby"]:
            return question[index + 1]

    return "here"


question = get_question()
day = get_day(question)
time = get_time(question)
place = get_place(question)

print(get_forecast(day, time, place, question))
