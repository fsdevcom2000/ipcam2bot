import asyncio
import cv2
from pathlib import Path
from aiogram.types import FSInputFile



class MonitoringController:
    def __init__(self, bot, repo, detector, interval: int = 10):
        self.bot = bot
        self.repo = repo
        self.detector = detector
        self.interval = interval
        self._cooldown = {}

    async def run(self):
        while True:
            for cam in self.repo.list_all():
                await self._process(cam)
            await asyncio.sleep(self.interval)

    async def _process(self, cam):
        from monitoring.camera_manager import CameraManager

        frame = CameraManager.get_frame(cam['url'])
        if frame is None:
            return

        if not self.detector.detect(frame):
            return

        now = asyncio.get_event_loop().time()
        last = self._cooldown.get(cam['id'], 0)
        if now - last < 60:
            return

        self._cooldown[cam['id']] = now

        img = Path(f"alert_{cam['id']}.jpg")
        cv2.imwrite(str(img), frame)

        try:
            await self.bot.send_photo(
                chat_id=cam['user_id'],
                photo=FSInputFile(path=str(img)),
                caption=f"Detected: {cam['name']}"
            )
        finally:
            img.unlink(missing_ok=True)

