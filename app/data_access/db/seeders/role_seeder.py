from typing import List
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from data_access.db.models.roles import Role
# фабрика асинхронной сессии
from data_access.db.session import async_session


# Список ролей, которые хотим добавить
MOCK_ROLES: List[dict] = [
    {"name": "admin", "description": "Администратор системы"},
    {"name": "user", "description": "Обычный пользователь"},
    {"name": "moderator", "description": "Модератор контента"},
]


async def seed_roles():
    async with async_session() as session:  # Асинхронная сессия
        async with session.begin():
            for role_data in MOCK_ROLES:
                # Проверяем, есть ли такая роль
                existing = await session.execute(
                    select(Role).where(Role.name == role_data["name"])
                )
                role = existing.scalars().first()
                if not role:
                    # Добавляем новую роль
                    new_role = Role(**role_data)
                    session.add(new_role)
        # commit будет автоматически через session.begin()
    print("Роли успешно добавлены/проверены.")


if __name__ == "__main__":
    asyncio.run(seed_roles())
