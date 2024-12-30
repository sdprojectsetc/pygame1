# Makefile

# Define the Python interpreter
PYTHON = python3

# Define the main script and modules
MAIN_SCRIPT = main.py
PLAYER_MODULE = player.py
SCREEN_MODULE = screen.py
PLATFORM_MODULE = platform.py

# Define the test directory (if you have tests)
TEST_DIR = tests

# Define the clean target to remove compiled files
CLEAN_FILES = __pycache__ *.pyc

.PHONY: run test clean

# Target to run the main script
run:
	$(PYTHON) $(MAIN_SCRIPT)

# Target to run tests (if you have a test suite)
test:
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

# Target to clean up compiled Python files
clean:
	rm -rf $(CLEAN_FILES)

# Optional: Target to run the player module directly (if needed)
run_player:
	$(PYTHON) $(PLAYER_MODULE)

# Optional: Target to run the screen module directly (if needed)
run_screen:
	$(PYTHON) $(SCREEN_MOiDULE)

# Optional: Target to run the platform module directly (if needed)
run_platform:
	$(PYTHON) $(PLATFORM_MODULE)
