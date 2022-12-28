from fastapi.routing import APIRouter
from jinja2 import Environment, FileSystemLoader
import yaml

memo_router = APIRouter()


def rend(template):
    env = Environment(loader=FileSystemLoader("templates"))
    jinja_template = env.get_template(template)
    with open('./memo/api.yaml') as f:
        routers = yaml.safe_load(f)
    return jinja_template.render(api=routers)


@memo_router.get("/test")
async def test():
    return {"say": "hello"}
