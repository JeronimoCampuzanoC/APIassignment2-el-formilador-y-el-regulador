import logging
from fastapi import FastAPI, Request
from datetime import datetime
from algorithm1 import Algorithm1LFCO2025JCAP
from algorithm2 import Algorithm2LFCO2025JCAP
from algorithm3 import Algorithm3LFCO2025JCAP

# Configura logging para guardar en un archivo
logging.basicConfig(
    filename="api_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

app = FastAPI()

# Middleware para registrar cada request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    ip = request.client.host
    method = request.method
    path = request.url.path
    timestamp = datetime.utcnow().isoformat()

    logging.info(f"{timestamp} - {ip} - {method} {path}")

    response = await call_next(request)
    return response

stored_strings = []

@app.get("/")
def root():
    return {"Hello": "World"}

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
    explainer = Algorithm3LFCO2025JCAP()
    results = []

    for string in stored_strings:
        sentential_steps = explainer.sentential(string)
        config_steps = explainer.configurationM(string)

        results.append({
            "string": string,
            "sentential": sentential_steps,
            "configuration": config_steps
        })

    return {"results": results}
