import os

from jinja2.ext import Extension


class WrapTemplatesWithNames(Extension):
    def __init__(self, environment):
        super().__init__(environment)

    def _add_comment(self, template_name, template_content):
        if template_name.endswith(".html.j2"):
            return f"<!-- TEMPLATE START: {template_name} -->\n{template_content}\n<!-- TEMPLATE END: {template_name} -->"
        elif template_name.endswith(".css.j2") or template_name.endswith(".js.j2"):
            return f"/* TEMPLATE START: {template_name} */\n{template_content}\n/* TEMPLATE END: {template_name} */"

        return template_content

    def preprocess(self, source, name, filename=None):
        template_name = os.path.basename(name) if name else "Unknown"
        source = self._add_comment(template_name, source)
        return source
