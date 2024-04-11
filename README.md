# tools

<details>
  <summary>wrap_templates_extension.py</summary>

Add comments or annotations to template files (`.html.j2`, `.css.j2`, `.js.j2`) before rendering them in a Jinja environment, providing clarity about the start and end of each template block. Example usage;

```py
if os.getenv("LOCAL_MODE") == "yes" and os.getenv("TEST_MODE") != "yes":
    from x.wrap_templates_extension import WrapTemplatesWithNames
    app_jinja_env.add_extension(WrapTemplatesWithNames)
```

</details>
