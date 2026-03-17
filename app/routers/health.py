from fastapi import APIRouter

health_router = APIRouter()

@health_router.get("/health")
async def health_check():
    # K8s Liveness Probe target
    return {"status": "healthy"}

@health_router.get("/health/live")
async def health_live_check():
    # K8s Readiness Probe target
    return {"status": "alive"}