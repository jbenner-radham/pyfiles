from pathlib import Path
from typing import List
from functional import seq

EXCLUDES = ['.git', '.vscode']

def in_excludes(path: Path) -> bool:
    return any([part in EXCLUDES for part in path.parts])

def implementation_0() -> List[Path]:
    ''' Python Standard Library Implementation '''
    root = Path('.')
    paths = root.glob('**/*')

    return [path for path in paths
            if not in_excludes(path) and path.is_file()]

def implementation_1() -> List[Path]:
    ''' PyFunctional Implementation '''
    root = Path('.')
    paths = root.glob('**/*')

    def is_file(path: Path) -> bool:
        return path.is_file()

    return list(seq(paths)
                .filter_not(in_excludes)
                .filter(is_file))
