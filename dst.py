# DiscordStatusChanger.py
# author : b6m
# date : 2022-5-7
import logging
import asyncio
import httpx
import json

logging.basicConfig(
        level=logging.INFO,
        format='\u001b[36;1m[\u001b[0m%(asctime)s\u001b[36;1m]\u001b[0m %(message)s\u001b[0m',
        datefmt='%H:%M:%S'
        )

class DiscordStatusChanger:
    def __init__(self):
        self.base_url = "https://discord.com/api/v9"
        self.headers = {'Authorization': str(input('\u001b[36;1m[\u001b[0m?\u001b[36;1m] \u001b[0m Token   • ')), 'Content-Type': 'application/json'}
        self.sfile = str(input('\u001b[36;1m[\u001b[0m?\u001b[36;1m] \u001b[0m Status File Name • '))
        self.delay = int(input('\u001b[36;1m[\u001b[0m?\u001b[36;1m] \u001b[0m Delay  • '))
        self.status = open(self.sfile + ".txt", 'r')
        self.status_list = [line.strip() for line in self.status];self.status.close()
    
    async def change_status(self):
        while True:
            for status in self.status_list:
                async with httpx.AsyncClient() as client:
                    await client.patch(
                        self.base_url + "/users/@me/settings", 
                        headers = self.headers,
                        data = json.dumps(
                            {
                                "custom_status":{
                                    "text" : status
                                    }
                            }
                        )
                    )
                    logging.info(f"Changed To • {status}")
                    await asyncio.sleep(self.delay)

if __name__ == "__main__":
    dst = DiscordStatusChanger()
    asyncio.run(dst.change_status())
