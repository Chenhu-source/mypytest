# conftest.py

def pytest_addoption(parser):
    parser.addoption("--dbp", action="store_true", help="Enable special debugging mode.")

def pytest_configure(config):
    print("1. Running pytest_configure hook")

def pytest_sessionstart(session):
    print("2. Running pytest_sessionstart hook")

def pytest_collection(session):
    print("3. Running pytest_collection hook")

def pytest_generate_tests(metafunc):
    print("3.1 Running pytest_generate_tests hook")

def pytest_make_parametrize_id(config, val, argname):
    print("3.2 Running pytest_make_parametrize_id hook")

def pytest_collection_modifyitems(session, config, items):
    print("3.3 Running pytest_collection_modifyitems hook")

def pytest_deselected(items):
    print("3.4 Running pytest_deselected hook")

def pytest_runtestloop(session):
    print("4. Running pytest_runtestloop hook")

def pytest_runtest_logstart(nodeid, location):
    print("4.1 Running pytest_runtest_logstart hook")

def pytest_runtest_logfinish(nodeid, location):
    print("4.2 Running pytest_runtest_logfinish hook")

def pytest_runtest_setup(item):
    print("4.3 Running pytest_runtest_setup hook")

def pytest_runtest_call(item):
    print("4.4 Running pytest_runtest_call hook")

def pytest_runtest_teardown(item, nextitem):
    print("4.5 Running pytest_runtest_teardown hook")

def pytest_fixture_setup(fixturedef, request):
    print("4.6 Running pytest_fixture_setup hook")

def pytest_fixture_post_finalizer(fixturedef, request):
    print("4.7 Running pytest_fixture_post_finalizer hook")

def pytest_runtest_makereport(item, call):
    print("4.8 Running pytest_runtest_makereport hook")

def pytest_runtest_logreport(report):
    print("4.9 Running pytest_runtest_logreport hook")

def pytest_report_teststatus(report, config):
    print("4.10 Running pytest_report_teststatus hook")

def pytest_sessionfinish(session, exitstatus):
    print("5. Running pytest_sessionfinish hook")

def pytest_unconfigure(config):
    print("6. Running pytest_unconfigure hook")

def pytest_runtest_protocol(item, nextitem):
    # This hook is available starting from pytest 7.0 and is executed before and after each test item.
    # This replaces the combination of runtest_setup, runtest_call, and runtest_teardown hooks.
    print("New-style pytest_runtest_protocol hook")
