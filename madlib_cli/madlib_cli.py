import re 


# code challenge help to solve this


def read_template(path):

    try:
        with open(path, 'r') as path_string:
            contents = path_string.read()
            returned_string = str(contents)
            print(returned_string)
            return(returned_string)
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
        

def parse_template(string):
    
    parse = re.findall(r'\{.*?\}', string)
    final_list = []
    for i in parse:
        string_edit = (i[1:-1])
        final_list.append(string_edit)
    correct_list = tuple(final_list)
    print("CORRECT_LIST", correct_list)
    template = re.sub(r'\{.*?\}', "{}", string)
    print("TEMPLATE", template)
    return(template, correct_list)

