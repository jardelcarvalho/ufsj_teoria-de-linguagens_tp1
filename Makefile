all:
	/usr/bin/python3 src/__main__.py

clean:
	rm -R src/factory/__pycache__
	rm -R src/factory/automato/__pycache__
	rm -R src/uteis/__pycache__