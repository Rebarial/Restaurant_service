import sys
import os

sys.path = ['', '..'] + sys.path[1:]
sys.path.append(os.getcwd()+"\\app")
sys.path.append(os.getcwd()+"/app")

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool, CheckConstraint

from alembic import context

from config import settings

from models.base import Base

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

config.set_main_option("sqlalchemy.url", settings.database_url_asyncpg + "?async_fallback=True")

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,

            include_schemas=True,
            compare_constraints=True,  # Включение сравнения constraints
            include_object=include_object,  # Функция фильтрации объектов
            user_module_prefix='sa.',
            render_as_batch=True,
        )

        with context.begin_transaction():
            context.run_migrations()


def include_object(object, name, type_, reflected, compare_to):
    if isinstance(object, CheckConstraint) and not reflected:
        return True
    return True

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
