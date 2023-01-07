CLEANDIRS := src tests

clean:
	@echo "Hygiene check";
	black $(CLEANDIRS);
	isort $(CLEANDIRS);
	flake8 $(CLEANDIRS);




