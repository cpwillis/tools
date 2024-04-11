import cProfile
import functools
import inspect
import io
import os
import pstats


def profileme(func=None, directory=None, sortby="cumulative"):
    """
    Decorator for profiling function execution and saving results to a file.

    By default, saves results to `filename.function.profile` in the directory of the file being run.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Validate directory argument
            profile_dir = directory or os.path.dirname(inspect.getfile(func))
            if not os.path.isdir(profile_dir):
                raise ValueError("Invalid directory path.")

            # Prepare profile filename
            filename = os.path.splitext(os.path.basename(inspect.getfile(func)))[0]
            profile_filename = f"{filename}.{func.__name__}.profile"
            datafn = os.path.join(profile_dir, profile_filename)

            # Profile function execution
            prof = cProfile.Profile()
            retval = prof.runcall(func, *args, **kwargs)

            # Generate and save profile stats
            with io.StringIO() as s, open(datafn, "w") as perf_file:
                ps = pstats.Stats(prof, stream=s).sort_stats(sortby)
                ps.print_stats()
                perf_file.write(s.getvalue())

            return retval

        return wrapper

    return decorator if func is None else decorator(func)
