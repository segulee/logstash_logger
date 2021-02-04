
# unittest:
	
# upload:
# 	python3 setup.py bdist_wheel

clean:
	rm -r dist
	rm -r *.egg-info
	rm -r build
	
local:
	python3 setup.py bdist_wheel