#!/usr/bin/env python3
"""Run API (pytest) and UI (Playwright) integration tests for FakeStoreAPI."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

from logger import create_logger

_STANDARD_VENV_DIRS = (".venv", "venv", "env")
_SKIP_PYVENV_PARENT_PARTS = frozenset(
    {".git", "__pycache__", "node_modules", ".pytest_cache", ".tox", "dist", "build"}
)


def _venv_python(venv_root: str) -> str:
    if sys.platform == "win32":
        return os.path.join(venv_root, "Scripts", "python.exe")
    return os.path.join(venv_root, "bin", "python")


def _path_under_project(project_root: str, path: str) -> bool:
    root = os.path.normcase(os.path.abspath(project_root))
    p = os.path.normcase(os.path.abspath(path))
    prefix = root if root.endswith(os.sep) else root + os.sep
    return p == root or p.startswith(prefix)


def _python_beside(pytest_exe: str) -> str | None:
    scripts = os.path.dirname(os.path.abspath(pytest_exe))
    name = "python.exe" if sys.platform == "win32" else "python"
    candidate = os.path.join(scripts, name)
    return candidate if os.path.isfile(candidate) else None


def _imports_pytest(python_exe: str, cwd: str | None) -> bool:
    try:
        proc = subprocess.run(
            [python_exe, "-c", "import pytest"],
            cwd=cwd,
            capture_output=True,
            timeout=20,
        )
        return proc.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def _iter_standard_venv_python(project_root: str):
    for name in _STANDARD_VENV_DIRS:
        exe = _venv_python(os.path.join(project_root, name))
        if os.path.isfile(exe):
            yield exe


def _find_pyvenv_python_with_pytest(project_root: str) -> str | None:
    root = Path(project_root)
    try:
        for cfg in root.rglob("pyvenv.cfg"):
            if _SKIP_PYVENV_PARENT_PARTS.intersection(cfg.parts):
                continue
            exe = _venv_python(str(cfg.parent))
            if os.path.isfile(exe) and _imports_pytest(exe, project_root):
                return exe
    except OSError:
        pass
    return None


def resolve_python_exe(project_root: str) -> str | None:
    """
    Interpreter for pytest and the UI script.

    Only considers Python under *project_root* (never an unrelated activated
    venv). Prefers environments that already have pytest installed.
    """
    project_root = os.path.abspath(project_root)
    venv = os.environ.get("VIRTUAL_ENV")

    if venv and _path_under_project(project_root, venv):
        exe = _venv_python(venv)
        if os.path.isfile(exe) and _imports_pytest(exe, project_root):
            return os.path.normpath(exe)

    for exe in _iter_standard_venv_python(project_root):
        if _imports_pytest(exe, project_root):
            return os.path.normpath(exe)

    for tool in ("pytest", "pytest.exe"):
        found = shutil.which(tool)
        if not found:
            continue
        found = os.path.abspath(found)
        if _path_under_project(project_root, found):
            beside = _python_beside(found)
            if beside:
                return os.path.normpath(beside)

    found = _find_pyvenv_python_with_pytest(project_root)
    if found:
        return os.path.normpath(found)

    for exe in _iter_standard_venv_python(project_root):
        return os.path.normpath(exe)

    launcher = os.path.normpath(sys.executable)
    if _path_under_project(project_root, launcher) and os.path.isfile(launcher):
        return launcher

    return None


def run_command(argv: list[str], description: str, logger) -> int:
    logger.info("=" * 60)
    logger.info("Running: %s", description)
    logger.info("Command: %s", subprocess.list2cmdline(argv))
    logger.info("=" * 60)
    result = subprocess.run(argv)
    if result.returncode != 0:
        logger.error("%s FAILED (exit %s)", description, result.returncode)
    else:
        logger.info("%s PASSED", description)
    return result.returncode


def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir))
    os.chdir(project_root)

    python_exe = resolve_python_exe(project_root)
    log_path = os.path.join(project_root, "run_tests.log")
    logger = create_logger(log_path, name="run_tests")

    logger.info("Starting integration test suite (API + UI)")
    logger.info("Log file: %s", log_path)
    logger.info(
        "Python: %s | sys.executable=%s | VIRTUAL_ENV=%s",
        python_exe or "(none under project)",
        sys.executable,
        os.environ.get("VIRTUAL_ENV", ""),
    )

    if not python_exe:
        logger.error(
            "No Python under project directory:\n  %s\n"
            "Create a venv here and install deps, then run with that interpreter:\n"
            "  python -m venv .venv\n"
            "  .venv\\Scripts\\pip install -r requirements.txt\n"
            "  .venv\\Scripts\\python scripts\\run_tests.py",
            project_root,
        )
        sys.exit(1)

    if not _imports_pytest(python_exe, project_root):
        logger.error(
            "pytest missing for: %s\nInstall with:\n  \"%s\" -m pip install -r requirements.txt",
            python_exe,
            python_exe,
        )
        sys.exit(1)

    api_exit = run_command(
        [python_exe, "-m", "pytest", "tests/api/", "-v"],
        "API integration tests",
        logger,
    )

    ui_script = os.path.join(project_root, "tests", "ui", "test_fakestore_ui.py")
    if os.path.isfile(ui_script):
        ui_exit = run_command(
            [python_exe, ui_script],
            "UI integration test",
            logger,
        )
    else:
        logger.error("UI test not found: %s", ui_script)
        ui_exit = 1

    logger.info("=" * 60)
    if api_exit == 0 and ui_exit == 0:
        logger.info("ALL TESTS PASSED")
        sys.exit(0)
    logger.error("SOME TESTS FAILED (api=%s, ui=%s)", api_exit, ui_exit)
    sys.exit(1)


if __name__ == "__main__":
    main()
