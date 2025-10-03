from fastapi import FastAPI



#Create a app for fast api.
app = FastAPI(
    title="Welcome to Taskify...",
    description="Taskify is AI supported to-do list application..."
)


# Health check for basic API test.
@app.get("/health")
def health_check():
    return {"response_code":"200","response":"Ok"}


# Root homepage check for basic API test.
@app.get("/")
def root_check():
    return {"message":"Welcome to Taskify."}


