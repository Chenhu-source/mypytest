# Describe
listed various hooks in the `pytest` testing framework. These hooks represent different points in the testing lifecycle where you can customize or extend the behavior of `pytest` by providing your own functions (or fixtures) with specific names.

Let's go through each of these hooks:

1. **`pytest_configure`**: This hook is called when `pytest` starts running. It allows you to perform configuration and setup tasks.

2. **`pytest_sessionstart`**: This hook is called at the beginning of the testing session before any tests are collected or run. It's useful for performing setup tasks that need to happen once for the entire test session.

3. **`pytest_collection`**: This is not a direct hook, but it represents the start of the test collection process. During test collection, `pytest` discovers and loads all test modules and functions.

   - **`pytest_generate_tests(metafunc)`**: Called when tests are being generated, for example, during parametrization.

   - **`pytest_make_parametrize_id(config, val, argname)`**: Allows you to customize the ID of a parametrized test.

   - **`pytest_collection_modifyitems(session, config, items)`**: Called after the collection is complete, allowing you to modify the collected items.

   - **`pytest_deselected(items)`**: Called when items are deselected.

4. **`pytest_runtestloop`**: This hook represents the main loop during test execution.

   - **`pytest_runtest_logstart(nodeid, location)`**: Called at the start of each test item.

   - **`pytest_runtest_logfinish(nodeid, location)`**: Called at the end of each test item.

   - **`pytest_runtest_setup(item)`**: Called before the test item is executed.

   - **`pytest_runtest_call(item)`**: Called when the test item is being executed.

   - **`pytest_runtest_teardow(item, nextitem)`**: Called after the test item has been executed.

   - **`pytest_fixture_setup(fixturedef, request)`**: Called when a fixture is being set up.

   - **`pytest_fixture_post_finalizer(fixturedef, request)`**: Called after a fixture's finalization code has been called.

   - **`pytest_runtest_makereport(item, call)`**: Allows you to create a custom report for a test item.

   - **`pytest_runtest_logreport(report)`**: Called with the test report for a test item.

   - **`pytest_report_teststatus(report, config)`**: Allows you to customize the reporting of test statuses.

5. **`pytest_sessionfinish`**: Called at the end of the test session. Useful for cleanup or summary tasks.

6. **`pytest_unconfigure`**: Called when `pytest` is about to shut down. Allows for final cleanup or additional actions.

These hooks provide a powerful way to customize the behavior of `pytest` at various stages of the testing process. You can use them to inject custom behavior, perform additional logging, or implement advanced parametrization strategies.
# The coding order
 - 1 pytest_configure 
 - 2 pytest_sessionstart 
 - 3 pytest_collection 
 - 3.1 pytest_generate_tests(metafunc)
 - 3.2 pytest_make_parametrize_id(config, val, argname) 
 - 3.3 pytest_collection_modifyitems(session, config, items) 
 - 3.4 pytest_deselected(items) 
 - 4 pytest_runtestloop 
 - 4.1 pytest_runtest_logstart(nodeid, location) 
 - 4.2 pytest_runtest_logfinish(nodeid, location) 
 - 4.3 pytest_runtest_setup(item) 
 - 4.4 pytest_runtest_call(item)
 - 4.5 pytest_runtest_teardow(item, nextitem) 
 - 4.6 pytest_fixture_setup(fixturedef, request) 
 - 4.7 pytest_fixture_post_finalizer(fixturedef, request) 
 - 4.8 pytest_runtest_makereport(item, call) 
 - 4.9 pytest_runtest_logreport(report) 
 - 4.10 pytest_report_teststatus(report, config) 
 - 5 pytest_sessionfinish
 - 6 pytest_unconfigure
# Run it
$ pip install -e .  
Defaulting to user installation because normal site-packages is not writeable  
Obtaining file:///home/wchenghu/PycharmProjects/mypytest  
  Preparing metadata (setup.py) ... done  
Installing collected packages: mypkg  
  Running setup.py develop for mypkg  
Successfully installed mypkg-0.1  

$ pytest --order  
1. Running pytest_configure hook  
2. Running pytest_sessionstart hook  
============================================= test session starts =============================================  
platform linux -- Python 3.10.12, pytest-8.0.0.dev319+g442b09ed9.d20231114, pluggy-1.3.0 -- /usr/bin/python3  
cachedir: .pytest_cache  
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/wchenghu/PycharmProjects/mypytest/.hypothesis/examples')  
rootdir: /home/wchenghu/PycharmProjects/mypytest  
configfile: pytest.ini  
plugins: mock-3.6.1, arraydiff-0.5.0, remotedata-0.3.3, astropy-header-0.2.0, hypothesis-6.36.0, doctestplus-0.11.2, filter-subpackage-0.1.1, cov-3.0.0, openfiles-0.5.0  
collecting ...  
3. Running pytest_collection hook  
3.3 Running pytest_collection_modifyitems hook  
collected 1 item                                                                                                
4. Running pytest_runtestloop hook  
New-style pytest_runtest_protocol hook  

tests/test_calculator.py::test_addition  
4.1 Running pytest_runtest_logstart hook  
4.8 Running pytest_runtest_makereport hook  
4.10 Running pytest_report_teststatus hook  
4.9 Running pytest_runtest_logreport hook  
4.8 Running pytest_runtest_makereport hook  
4.10 Running pytest_report_teststatus hook  PASSED                                                          [100%]  
4.9 Running pytest_runtest_logreport hook  
4.8 Running pytest_runtest_makereport hook  
4.10 Running pytest_report_teststatus hook  
4.9 Running pytest_runtest_logreport hook  
4.2 Running pytest_runtest_logfinish hook  
5. Running pytest_sessionfinish hook  


============================================== 1 passed in 0.13s ==============================================  
6. Running pytest_unconfigure hook  

