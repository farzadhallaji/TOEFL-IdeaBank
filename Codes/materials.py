import pandas as pd
import os
import sys

df = pd.read_csv('../Resources/Questions.csv')

def respone_separate(response_content, path_response):
    sections = response_content.split('### ')
    sections = [section.strip() for section in sections if section.strip()]
    
    for section in sections:
        if section.startswith('1'):
            content_creation = section
            with open(os.path.join(path_response, 'Content.md'), 'w') as f:
                f.write('### ' + content_creation)
                
        elif section.startswith('2'):
            ideas = section
            with open(os.path.join(path_response, 'Ideas.md'), 'w') as f:
                f.write('### ' + ideas)
                
        elif section.startswith('3'):
            sample_answer = section
            with open(os.path.join(path_response, 'Sample Answer.md'), 'w') as f:
                f.write('### ' + sample_answer)
                
        elif section.startswith('4'):
            collocations = section
            with open(os.path.join(path_response, 'Collocations.md'), 'w') as f:
                f.write('### ' + collocations)
    
    
def prcc(resource, number):
    row = df[(df['Resource'] == resource) & (df['Number'] == str(number))]
    if not row.empty:
        folder_name = row.iloc[0]['Topic']
        path_response = os.path.join('../Topics',folder_name, resource, resource+'Q'+str(number), f'Materials-{resource}Q{number}')
        with open(os.path.join(path_response, 'Response.md'), 'r') as response:
            respone_separate(response.read(), path_response)
    else:
        print(f"No entry found for {resource} Q{number}")



if __name__ == "__main__":
    # Ensure there are exactly two arguments (excluding the script name)
    if len(sys.argv) != 3:
        print("Usage: python script.py <Resource> <Number>")
        sys.exit(1)

    # Get the arguments
    resource = sys.argv[1]
    number = int(sys.argv[2])
    
    prcc(resource, number)

