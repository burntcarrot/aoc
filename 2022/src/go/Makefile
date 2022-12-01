build:
	bash ./batch-build.sh

test:
	bash ./batch-test.sh

build-single:
	bash ./single-build.sh $(DAY)

lint-single:
	bash ./single-lint.sh $(DAY)

test-single:
	bash ./single-test.sh $(DAY)

pipeline: build-single test-single
# pipeline: lint-single build-single test-single

batch: build test
