from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import logging
from .config import config
from .dependency_checks import check_postgres, check_redis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI(title=config.API_TITLE)

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Secure API is running"}

@app.get("/health")
async def health_check():
    # K8s Liveness Probe target
    return {"status": "healthy"}

@app.get("/health/live")
async def health_live_check():
    # K8s Readiness Probe target
    return {"status": "alive"}

@app.get("/health/deps")
async def health_dependency_check():
    dependencies = {
        "postgres": check_postgres(config),
        "redis": check_redis(config),
    }
    statuses = {info["status"] for info in dependencies.values()}
    if "error" in statuses:
        overall = "error"
        status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    elif "skipped" in statuses:
        overall = "degraded"
        status_code = status.HTTP_200_OK
    else:
        overall = "ok"
        status_code = status.HTTP_200_OK
    return JSONResponse(
        status_code=status_code,
        content={"status": overall, "dependencies": dependencies},
    )
