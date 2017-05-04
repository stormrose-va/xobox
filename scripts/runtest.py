#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
    xobox - Unit Test Script
    ~~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


import importlib
import os
import re
import sys
import unittest

try:
    from os import EX_OK
except ImportError:
    EX_OK = 0

try:
    from os import EX_SOFTWARE
except ImportError:
    EX_SOFTWARE = 1


def __get_version(version=None):
    """Derive a PEP440-compliant version number from VERSION."""
    version = version or sys.version_info
    assert len(version) == 5
    assert version[3] in ('alpha', 'beta', 'rc', 'final')
    parts = 2 if version[2] == 0 else 3
    main_part = '.'.join(str(x) for x in version[:parts])

    sub = ''
    if version[3] == 'alpha' and version[4] == 0:
        sub = '.dev'
    elif version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'rc'}
        sub = mapping[version[3]] + str(version[4])

    return main_part + sub


def __filter_files(item):
    """
    Filter for Python modules beginning with *test_*
    
    :param str item: the item to be tested with this filter
    """
    file, ext = os.path.splitext(item)
    if file != '__init__' and ext == '.py' and file[:5] == 'test_':
        return True
    return False


def __filter_members(item):
    """
    Filter function to detect classes within a module or package
    
    :param str item: the item to be tested with this filter
    """
    exclude = (
        re.escape('__builtins__'),
        re.escape('__cached__'),
        re.escape('__doc__'),
        re.escape('__file__'),
        re.escape('__loader__'),
        re.escape('__name__'),
        re.escape('__package__'),
        re.escape('__path__')
    )
    pattern = re.compile('|'.join(exclude))
    return not pattern.search(item)


def __write_untested(label, result):
    """
    Print information on non-executed tests
    
    :param str label: type of the untested (either 'Skipped' or 'Failed')
    :param result:    test result set
    """
    if result:
        print('{} Test Cases:\n'.format(label))
        for res in result:
            if label == "Skipped":
                info = res[2]
            else:
                info = res[3]
            print('   {module} {test}: {info}'.format(
                module=res[0],
                test=' '.join(str(res[1]).split(" ")[0].split('_')),
                info=info.strip())
            )


def main():
    """
    xobox test script main function
    """
    # find out if running from an uninstalled version
    # this being the case, insert the appropriate path into PYTHONPATH
    xobox_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    if os.path.isfile(os.path.join(xobox_path, 'xobox', '__init__.py')):
        sys.path.insert(0, xobox_path)

    test_classes = []
    test_dir = os.path.join(xobox_path, 'tests')

    # look recursively for Python modules in ``test_dir`` and find all classes within those
    # modules derived from :py:class:`~unittest.TestCase`
    for root, dirs, files in os.walk(test_dir):
        module_prefix = '.'.join(str(os.path.relpath(root, os.path.dirname(test_dir))).split(os.path.sep))
        for mod in filter(__filter_files, files):
            try:
                candidate = importlib.import_module('.'.join((module_prefix, os.path.splitext(mod)[0])))
            except ImportError:
                candidate = None
            if candidate:
                for member in filter(__filter_members, dir(candidate)):
                    try:
                        if issubclass(getattr(candidate, member), unittest.TestCase) \
                           and getattr(candidate, member).__name__ != unittest.TestCase.__name__:
                            test_classes.append(getattr(candidate, member))
                    except TypeError:
                        pass

    return_code = EX_OK

    results = {}
    skipped = []
    failed = []

    # Create a unittest runner and run all detected tests
    runner = unittest.TextTestRunner(stream=open(os.devnull, 'w'))
    for test_class in test_classes:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
        result = runner.run(suite)
        if result.skipped:
            for test in result.skipped:
                skipped.append((
                    test_class.__name__,
                    test[0],
                    test[1],
                    getattr(getattr(test_class, str(test[0]).split(" ")[0]), '__doc__').splitlines()[2].strip()
                ))
        if result.failures:
            for test in result.failures:
                failed.append((
                    test_class.__name__,
                    test[0],
                    test[1],
                    getattr(getattr(test_class, str(test[0]).split(" ")[0]), '__doc__').splitlines()[2].strip()
                ))
        if result.errors:
            for test in result.errors:
                failed.append((
                    test_class.__name__,
                    test[0],
                    test[1],
                    getattr(getattr(test_class, str(test[0]).split(" ")[0]), '__doc__').splitlines()[2].strip()
                ))
        results[test_class.__name__] = (len(result.failures) + len(result.errors), len(result.skipped), result.testsRun)
        if result.failures or result.errors:
            return_code = EX_SOFTWARE

    total_tests = 0
    total_passed = 0
    total_failed = 0
    total_skipped = 0

    print("\nxobox Unit Test Result Summary:\n\nPython version: {}\n".format(__get_version()))
    print("Test                               Passed   Failed   Skipped   Total    % passed")
    print("================================================================================")
    for key in sorted(results):
        total_tests += results[key][2]
        total_skipped += results[key][1]
        total_failed += results[key][0]
        total_passed = total_tests - total_failed - total_skipped
        try:
            ratio = float(results[key][2] - results[key][0] - results[key][1]) / float(results[key][2] - results[key][1])
        except ZeroDivisionError:
            ratio = 1
        print(
            "{test: <32}      {passed: >3d}      {failed: >3d}      {skipped: >4d}     {total: >3d}     {ratio: >3.2%}".format(
            test=key,
            passed=results[key][2]-results[key][0]-results[key][1],
            failed=results[key][0],
            skipped=results[key][1],
            total=results[key][2],
            ratio=ratio
        ))
    print("================================================================================")
    try:
        ratio = float(total_passed) / float(total_tests-total_skipped)
    except ZeroDivisionError:
        ratio = 1
    print("{test: <32}      {passed: >3d}      {failed: >3d}      {skipped: >4d}     {total: >3d}     {ratio: >3.2%}\n".format(
        test="TOTAL",
        passed=total_passed,
        failed=total_failed,
        skipped=total_skipped,
        total=total_tests,
        ratio=ratio
    ))
    __write_untested('Skipped', skipped)

    if failed and skipped:
        print('\n')

    __write_untested('Failed', failed)

    if total_passed < (total_tests - total_skipped):
        print("\nOverall Test Result: FAILED.\n")
    else:
        print("\nOverall Test Result: PASSED.\n")
    return return_code


if __name__ == '__main__':
    sys.exit(main())
else:
    raise RuntimeError("This is an executable file. Do not try to import it!")
    # noinspection PyUnreachableCode
    sys.exit(os.EX_SOFTWARE)
