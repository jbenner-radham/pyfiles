from pathlib import Path
from typing import List

EXCLUDES = ['.vscode']

root_path = Path('.')
all_paths = list(root_path.glob('**/*'))
filtered_paths = [path for path in all_paths if all([part not in EXCLUDES for part in path.parts])]
file_paths = [path for path in filtered_paths if path.is_file()]

# TODO: Write to metafile with `Path#as_posix()`?


# ----------


from pathlib import Path
from typing import List
from functional import seq

EXCLUDES = ['.vscode']

def path_in_excludes(path: Path) -> bool:
    return all([part in EXCLUDES for part in path.parts])

root_path = Path('.')
all_paths = list(root_path.glob('**/*'))
filtered_paths = seq(all_paths).filter_not(path_in_excludes)
