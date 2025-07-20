from faker import Faker
from html import escape

faker = Faker()

def generate_lorem(paragraphs: int = 3) -> str:
    return "\n\n".join(
        f"<i>{escape(faker.paragraph())}</i>" for _ in range(paragraphs)
    )
