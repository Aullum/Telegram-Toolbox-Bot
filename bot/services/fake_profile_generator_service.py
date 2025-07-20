from faker import Faker
from html import escape

def generate_fake_profile(gender: str = "random", locale: str = "en_US") -> str:
    fake = Faker(locale)

    profile = {
        "Name": fake.name_male() if gender == "male" else fake.name_female() if gender == "female" else fake.name(),
        "Email": fake.email(),
        "Phone": fake.phone_number(),
        "Address": fake.address().replace("\n", ", "),
        "Birthday": fake.date_of_birth().strftime("%Y-%m-%d"),
    }

    return "\n".join(f"<b>{escape(k)}:</b> {escape(str(v))}" for k, v in profile.items())
