PHONY: clean-pyc clean-build
help:
	@echo "    lint"
	@echo "        Check style with pylint."
	@echo "    test"
	@echo "        Run pytest"
	@echo '    run'
	@echo '        Run the `my_project` service on your local machine.'

lint:
	pylint --rcfile=.pylintrc --output-format=parseable --reports=no sponsors

test:
	pytest --verbose --color=yes sponsors

run:
	scrapy crawl pycon
