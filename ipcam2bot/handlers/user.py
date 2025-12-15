from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from monitoring.db import CameraRepository

user_private_router = Router()
repo = CameraRepository("cameras.db")


@user_private_router.message(Command("add"))
async def add_camera(message: Message):
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        await message.answer("/add <name> <url>")
        return
    repo.add(message.from_user.id, parts[1], parts[2])
    await message.answer("Camera added")


@user_private_router.message(Command("del"))
async def del_camera(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2 or not parts[1].isdigit():
        await message.answer("/del <id>")
        return
    repo.delete(message.from_user.id, int(parts[1]))
    await message.answer("Camera deleted")


@user_private_router.message(Command("list"))
async def list_cameras(message: Message):
    cams = repo.list_by_user(message.from_user.id)
    if not cams:
        await message.answer("No cameras")
        return
    text = "Your cameras:\n"
    for c in cams:
        text += f"{c['id']}. {c['name']}\n"
    await message.answer(text)