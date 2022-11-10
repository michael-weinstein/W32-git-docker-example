import fastapi
import fastapi.templating
import uvicorn
import rpsSupport

HTMLTEMPATEFOLDER = "html"
RPSWINS = rpsSupport.standardWins
RPSLSWINS = rpsSupport.rpslsWins

DEFAULTGAME = "rps"

app = fastapi.FastAPI()

templates = fastapi.templating.Jinja2Templates(directory = HTMLTEMPATEFOLDER)

@app.get("/", response_class=fastapi.responses.RedirectResponse)
def redirectRoot():
    return fastapi.responses.RedirectResponse(DEFAULTGAME)


@app.get("/rps", response_class=fastapi.responses.HTMLResponse)
def sendRPSPlayPage(request:fastapi.Request):
    return templates.TemplateResponse("play.html", {"request":request, "id": "rps", "game": "Rock, Paper, Scissors", "throws": list(RPSWINS.keys())})


@app.get("/rpsls", response_class=fastapi.responses.HTMLResponse)
def sendRPSLSPlayPage(request:fastapi.Request):
    return templates.TemplateResponse("play.html", {"request":request, "id": "rpsls", "game": "Rock, Paper, Scissors, Lizard, Spock", "throws": list(RPSLSWINS.keys())})


@app.post("/rps", response_class=fastapi.responses.HTMLResponse)
async def sendRPSOutcome(request:fastapi.Request, playerThrow:str=fastapi.Form(...)):
    computerThrow = rpsSupport.game.getComputerThrow(RPSWINS)
    result = rpsSupport.game.determineOutcome(RPSWINS, computerThrow, playerThrow)
    return templates.TemplateResponse("result.html", {"request":request, "id": "rps", "outcome": result[0], "computerThrow": computerThrow})


@app.post("/rpsls", response_class=fastapi.responses.HTMLResponse)
async def sendRPSOutcome(request:fastapi.Request, playerThrow:str=fastapi.Form(...)):
    computerThrow = rpsSupport.game.getComputerThrow(RPSLSWINS)
    result = rpsSupport.game.determineOutcome(RPSLSWINS, computerThrow, playerThrow)
    return templates.TemplateResponse("result.html", {"request":request, "id": "rpsls", "outcome": result[0], "computerThrow": computerThrow})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=44444)
