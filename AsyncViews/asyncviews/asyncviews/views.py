import asyncio
from time import sleep
import httpx
from django.http import HttpResponse

# chamada assincrona
async def http_call_async():
    for num in range(1, 5):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

# chamada sincrona
def http_call_sync():
    for num in range(1, 5):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org")
    print(r)

# Não trata a parte da chamada do loop para depois a requisião, trata a requisião de forma assincrona
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP Request")

# Primeiro trata a parte da chamada do loop para depois a requisião assim sendo de forma sincrona
def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP Request")