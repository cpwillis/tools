def log_start_end(func):
    from xxx.log import get_logger
    from flask import Blueprint
    from functools import wraps
    import click

    cli = Blueprint("xxx", __name__)
    logger = get_logger(__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        command_name = click.get_current_context().command.name
        logger.info(f"START of {cli.name}.{command_name} CLI")
        result = func(*args, **kwargs)
        logger.info(f"END of {cli.name}.{command_name} CLI")
        return result

    return wrapper
