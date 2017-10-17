init:
	@echo "Installing dependencies from requirements.txt"
	sudo pip install --ignore-installed six
	sudo pip install -r packages.txt
.PHONY: init