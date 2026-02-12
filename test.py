import asyncio
import time

async def sync_fun():
    print("sync_fun: 시작")
    time.sleep(2)  # ❌ 이벤트 루프를 2초 동안 멈춤
    print("sync_fun: 끝")

async def async_fun():
    print("async_fun: 시작")
    await asyncio.sleep(2)  # ✅ 이벤트 루프를 막지 않음
    print("async_fun: 끝")

async def main():
    await asyncio.gather(sync_fun(), sync_fun(), async_fun(), async_fun())


asyncio.run(main())
