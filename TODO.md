# TODO

## Now

- Refactor

    - Unwind decorators and includes and scans, and manually wire up 
      everything in __init__.py, with copious comments
      
    - Extensive docstrings
    
    - Much better type hinting
    
    - Run ``mypy`` and fix
    
    - Changeset -> Changeset
    
    - Use immutable and slots in Changeset dataclasses  
    
    - Convert JS to ES6

## Next

## Soon

- Mark as 3.6+ and include dataclass backport

- Better logger in the watchgod stuff

- Don't hardwire `watchgod_watcher.DefaultDirWatcher` in threadrunner

## Someday

- watchgod watchers
    - Better docstrings and comments
    - Add type hints
    - Bring back: debounce, normal_sleep, min_sleep
    - Switch to pathlib for operations, return values, etc.
    - Don't immediately run?
    - Consider an ABC
    - Optionally use a hash (MD5 or passed-in) as comparator
    - Mode to remember previous run (and store current run)
        * With marker for "generation" in pickle filename
    - CLI mode
    - multiprocessing support


## Done

