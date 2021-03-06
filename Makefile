# ugh, appengine why can't I just pip install you?!
PYTHONPATH=PYTHONPATH=$(PWD)/lib:$(shell echo $$PYTHONPATH)

lib: requirements-vendor.txt
	rm -rf $@
	mkdir -p $@
	pip install -t $@ -r requirements-vendor.txt


.PHONY: setup
setup: lib requirements-test.txt requirements-local.txt
	pip install -r requirements-local.txt
	pip install -r requirements-test.txt

.PHONY: setupdb
setupdb: deps
	$(PYTHONPATH) python manage.py migrate
	$(PYTHONPATH) python manage.py loaddata fixtures/*.json
	$(PYTHONPATH) python manage.py load_state_polls
	@echo "The admin account is 'admin/password5'"

.PHONY: genfixtures
genfixtures: deps
	$(PYTHONPATH) python manage.py migrate
	$(PYTHONPATH) python manage.py createsuperuser
	$(PYTHONPATH) python manage.py load_state_polls
	$(PYTHONPATH) python manage.py fake_social_network
	$(PYTHONPATH) python manage.py dumpdata -o fixtures/users.json
	sed -i 's/}},/}},\n/g' fixtures/users.json

.PHONY: startcontainer
startcontainer:
	./startcontainers.sh

.PHONY: deps
deps: startcontainer

.PHONY: stop
stop:
	-docker stop voteswap-mysql
	-docker rm voteswap-mysql

test: deps setup
	$(PYTHONPATH) python manage.py test

.PHONY: runserver
runserver: deps
	$(PYTHONPATH) python manage.py runserver
