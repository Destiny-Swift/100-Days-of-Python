from IPython.display import display
import sys
sys.path.append('Gemini API/')
from gemini_ai import gemini_ai


display(gemini_ai(input('Enter prompt: ')))
