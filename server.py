import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "desafio_python.main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="info",
    )
