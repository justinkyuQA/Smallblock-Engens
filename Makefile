.PHONY: doctor status runtime test clean

doctor:
	@echo "== SmallBlock Doctor =="
	@python3 --version
	@find . -maxdepth 3 -type f | sort

status:
	@echo "== SmallBlock Status =="
	@git status --short
	@echo
	@find smallblock -maxdepth 4 -type f | sort

runtime:
	PYTHONPATH=. python3 examples/game_demo.py  
test:
	@python3 -m unittest discover -v

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete


