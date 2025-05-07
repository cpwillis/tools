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

<details>
  <summary>Click Start/End Wrapper</summary>

[log_start_end.py](./python/log_start_end.py)

The `log_start_end` decorator in Python adds a logger event before and after the execution of a cli command.

</details>

<details>
  <summary>Function to Abbreviate Numbers</summary>

```py
def format_abbreviated_number(value: int) -> str:
    """
    Convert a number to a human-readable string:
    - Abbreviates clean round numbers in thousands (k), millions (m), billions (b), etc.
    - Uses comma formatting for numbers with variations or smaller values.
    - Returns the original value if it's not an integer or cannot be converted to one.
    - Returns "None" if the value is zero.
    """

    # Check if the value is an integer
    if not isinstance(value, int):
        return str(value)

    # Check if the value is zero
    if value == 0:
        return "None"

    # Check if a number is followed by all zeros
    # Without this, the modulus check mis-abbreviates numbers like 10022000 as 10022k instead of 10,022,000 (incorrectly divisible by 1000).
    def is_clean_multiple(value):
        return value % 10 ** len(str(value).rstrip("0")) == 0

    # Check for clean multiples and abbreviate them
    if is_clean_multiple(value):
        if value % 1_000_000_000_000_000 == 0:
            return f"{value // 1_000_000_000_000_000}q"  # Quadrillion
        elif value % 1_000_000_000_000 == 0:
            return f"{value // 1_000_000_000_000}t"  # Trillion
        elif value % 1_000_000_000 == 0:
            return f"{value // 1_000_000_000}b"  # Billion
        elif value % 1_000_000 == 0:
            return f"{value // 1_000_000}m"  # Million
        elif value % 1_000 == 0:
            return f"{value // 1_000}k"  # Thousand

    # If the number is not a clean multiple, return the full value with commas
    return f"{value:,.0f}"
```

</details>

### Shell

<details>
  <summary>Shell Colour Echo</summary>

[colour_echo.sh](./shell/colour_echo.sh)

```sh
cecho "I'm an example." "$red"
```

</details>

### VSCode

<details>
  <summary>TODO Highlight Extension Colours</summary>
  
  [todohighlight.json](./vscode/todohighlight.json) --> [Extension (Marketplace)](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight), [Reference Colours](https://github.com/wayou/vscode-todo-highlight/issues/93#issuecomment-390368341)

</details>
