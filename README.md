# tools

### Python

<details>
  <summary>Custom J2 Ext to Wrap Templates with their Filename</summary>

[wrap_templates_extension.py](./python/wrap_templates_extension.py)

Add comments or annotations to template files (`.html.j2`, `.css.j2`, `.js.j2`) before rendering them in a Jinja environment, providing clarity about the start and end of each template block. Example usage;

```py
if os.getenv("LOCAL_MODE") == "yes" and os.getenv("TEST_MODE") != "yes":
    from x.wrap_templates_extension import WrapTemplatesWithNames
    app_jinja_env.add_extension(WrapTemplatesWithNames)
```

</details>

<details>
  <summary>Function Profiler</summary>

[profiler.py](./python/profiler.py)

The `profileme` decorator in Python facilitates function execution profiling, directing the results to a file named after the function being profiled. It offers options to specify the directory and sorting method for the profile statistics.

</details>

### Shell

<details>
  <summary>Shell Colour Echo</summary>

```sh
black=$(tput setaf 0) red=$(tput setaf 1) green=$(tput setaf 2) yellow=$(tput setaf 3) blue=$(tput setaf 4) magenta=$(tput setaf 5) cyan=$(tput setaf 6) white=$(tput setaf 7) reset=$(tput sgr0)
cecho() { echo "${2}${1}${reset}"; } # $1=msg $2=col
```

```sh
cecho "Please try again or exit the script (ctrl+c)." "$red"
```

</details>
