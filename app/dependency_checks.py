from psycopg import connect
from redis import Redis


def _status_error(error):
    return {"status": "error", "error": str(error)}


def check_postgres(config):
    if not config.POSTGRES_HOST:
        return {"status": "skipped", "reason": "not_configured"}

    try:
        with connect(
            host=config.POSTGRES_HOST,
            port=config.POSTGRES_PORT,
            dbname=config.POSTGRES_DB,
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD,
            connect_timeout=config.POSTGRES_CONNECT_TIMEOUT,
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                cur.fetchone()
        return {"status": "ok"}
    except Exception as exc:
        return _status_error(exc)


def check_redis(config):
    if not config.REDIS_HOST:
        return {"status": "skipped", "reason": "not_configured"}

    client = Redis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        password=config.REDIS_PASSWORD or None,
        socket_connect_timeout=config.REDIS_CONNECT_TIMEOUT,
        socket_timeout=config.REDIS_CONNECT_TIMEOUT,
    )
    try:
        client.ping()
        return {"status": "ok"}
    except Exception as exc:
        return _status_error(exc)
    finally:
        client.close()
