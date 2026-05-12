#!/usr/bin/env python3
"""
Run both API and UI integration tests for the FakeStoreAPI project.
Uses a separate logger module.
"""

import subprocess
import sys
import os
from logger import create_logger

def run_command(cmd, description, logger):
    logger.info("=" * 60)
    logger.info("Running: %s", description)
    logger.info("Command: %s", cmd)
    logger.info("=" * 60)

    result = subprocess.run(cmd, shell=True)

    if result.returncode != 0:
        logger.error("%s FAILED with exit code %s", description, result.returncode)
    else:
        logger.info("%s PASSED", description)

    return result.returncode

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir))
    os.chdir(project_root)
    python_exe = sys.executable
    log_file_path = os.path.join(project_root, "run_tests.log")
    logger = create_logger(log_file_path, name="run_tests")

    logger.info("Starting integration test suite (API + UI)")
    logger.info("Log file: %s", log_file_path)

    api_exit = run_command(
        f"\"{python_exe}\" -m pytest tests/api/ -v",
        "API Integration Tests (pytest)",
        logger,
    )

    ui_script = "tests/ui/test_fakestore_ui.py"
    if os.path.exists(ui_script):
        ui_exit = run_command(
            f"\"{python_exe}\" \"{ui_script}\"",
            "UI Integration Test (Playwright)",
            logger,
        )
    else:
        logger.error("UI test script not found at %s", ui_script)
        ui_exit = 1

    logger.info("=" * 60)
    if api_exit == 0 and ui_exit == 0:
        logger.info("ALL TESTS PASSED")
        sys.exit(0)
    else:
        logger.error("SOME TESTS FAILED")
        logger.error("API tests exit code: %s", api_exit)
        logger.error("UI test exit code: %s", ui_exit)
        sys.exit(1)

if __name__ == "__main__":
    main()
