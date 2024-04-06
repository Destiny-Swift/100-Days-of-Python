# import pathlib
import textwrap
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = 'AIzaSyB-r64jmCJlf6OM4obk0yytT7UIX-naqvg'
genai.configure(api_key=GOOGLE_API_KEY)


# for model in genai.list_models():
#     if 'generateContent' in model.supported_generation_methods:
#         print(model.name)

model = genai.GenerativeModel('gemini-pro')


def gemini_ai(prompt):
    response = model.generate_content(prompt)
    message = response.text
    return to_markdown(message)


if __name__ == '__main__':
    display(gemini_ai('What is the meaning of life?'))

# for chunk in response:
#     print(to_markdown(chunk.text))
#     print('_' * 80)
