from fastapi import FastAPI, HTTPException

from app.db import database, User


app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get("/")
async def read_root():
    return await User.objects.all()


@app.get("/health")
async def health():
    # Liveness check: deliberately cheap and dependency-free. A 200 here only
    # proves the process and the asyncio event loop are responsive. This maps to
    # a Kubernetes livenessProbe -- so it must NOT touch the database, or a brief
    # DB outage would trigger needless container restarts.
    return {"status": "ok"}


@app.get("/ready")
async def ready():
    # Readiness check: verifies the app can actually serve real traffic, i.e. its
    # critical dependency (PostgreSQL) is reachable. Maps to a Kubernetes
    # readinessProbe -- on failure, the pod is removed from the load balancer but
    # NOT restarted, so a transient DB blip just pauses traffic instead of
    # restart-storming every replica.
    try:
        await database.execute("SELECT 1")
    except Exception:
        raise HTTPException(status_code=503, detail="database unavailable")
    return {"status": "ready"}


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
