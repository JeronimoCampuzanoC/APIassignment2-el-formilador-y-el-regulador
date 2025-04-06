from fastapi import FastAPI
from algorithm1 import Algorithm1LFCO2025JCAP
from algorithm2 import Algorithm2LFCO2025JCAP

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
