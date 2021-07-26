import requests


def get_response(user_agent, session, day_num):
    """Get response from the website"""

    headers = {"User-Agent": user_agent, "Cookie": f"session={session}"}
    url = f"https://adventofcode.com/2020/day/{day_num}/input"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return False
    return response.text.strip()


def write_response(day_num, response):
    """Write the response in a file"""

    with open(f"AoC_{day_num}_input.txt", "w") as file:
        file.writelines(response)


def main():
    user_agent = input("Enter your user-agent: ")
    session = input("Enter your cookie: ")
    max_days = 25
    for day in range(1, max_days + 1):
        response = get_response(user_agent, session, day)
        if response:
            write_response(day, response)


main()
