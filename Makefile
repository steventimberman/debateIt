init:
	@echo "Installing dependencies from requirements.txt"
	pip install -r packages.txt
.PHONY: init