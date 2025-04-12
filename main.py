from fastapi import FastAPI
from algorithm1 import Algorithm1LFCO2025JCAP
from algorithm2 import Algorithm2LFCO2025JCAP
from algorithm3 import Algorithm3LFCO2025JCAP

import io
from contextlib import redirect_stdout

app = FastAPI()

stored_strings = []

@app.get("/")
def root():
    return {"Hello" : "World"}

@app.post("/fill")
def create_items():
    global stored_strings
    p1 = Algorithm1LFCO2025JCAP()
    stored_strings = []

    for i in range(16):
        if i % 2 == 0:
            stored_strings.append(p1.generate_grammar_strings())
        else:
            stored_strings.append(p1.generate_non_grammar_strings())
    
    return {
        "message": "Generated 16 strings using Algorithm 1",
        "strings": stored_strings
    }

@app.get("/get-strings")
def get_stored_strings():
    return {"stored_strings": stored_strings}

@app.get("/filter")
def filter_items():
    global stored_strings
    pda = Algorithm2LFCO2025JCAP()
    valid_items = [item for item in stored_strings if pda.string_check(item)]
    stored_strings = valid_items
    return {"Valid Strings": valid_items}

@app.get("/show-process")
def show_process():
    global stored_strings
    explainer = Algorithm3LFCO2025JCAP()

    # This will capture all printed output
    f = io.StringIO()
    with redirect_stdout(f):
        for i, string in enumerate(stored_strings):
            print(f"\n=== String #{i+1}: {string} ===\n")
            explainer.sentential(string)
            print("\n--- Configuration ---\n")
            explainer.configurationM(string)
            print("\n=======================\n")

    output = f.getvalue()
    return output