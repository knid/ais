# -*- coding: utf-8 -*-
import sys
from pathlib import Path


def main():
    current_path = Path(__file__).parent.parent.resolve()
    sys.path.append(str(current_path))
    from ais.core import main
    exit_status = main()
    return exit_status.value


if __name__ == "__main__":
    sys.exit(main())
