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


def __get_version_main_part(version):
    """Derive PEP440-compliant main part from a valid version quintuple"""
    parts = 2 if version[2] == 0 else 3
    return '.'.join(str(x) for x in version[:parts])


def __get_version_sub_part(version):
    """Derive PEP440-compliant sub part from a valid version quintuple"""
    sub = ''
    if version[3] == 'alpha' and version[4] == 0:
        sub = '.dev'
    elif version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'rc'}
        sub = mapping[version[3]] + str(version[4])
    return sub


def __get_version():
    """Derive a PEP440-compliant version number from sys.version_info."""
    version = sys.version_info
    main_part = __get_version_main_part(version)
    sub_part = __get_version_sub_part(version)

    return main_part + sub_part


def __get_untested(test_class, test_set):
    """
    Prepare a list of not run tests
    
    :param test_class: test class
    :param test_set:   result set with failed or skipped tests
    :return:           list of tuples 
    """
    result = []
    if test_set:
        for test in test_set:
            result.append((
                test_class.__name__,
                test[0],
                test[1],
                getattr(getattr(test_class, str(test[0]).split(" ")[0]), '__doc__').splitlines()[2].strip()
            ))
    return result


def __get_modules(path, filter_function):
    """
    Generate a list of modules from a given path
    
    :param str path:         location on the file system to scan
    :param filter_function:  reference to the filter function to be used
    :return:                 iterable for modules
    """
    for root, dirs, files in os.walk(path):
        module_prefix = '.'.join(str(os.path.relpath(root, os.path.dirname(path))).split(os.path.sep))
        for mod in filter(filter_function, files):
            yield '.'.join((module_prefix, os.path.splitext(mod)[0]))


def __get_candidates(path, module_filter, member_filter):
    """
    Generate candidates from a given path
    
    :param str path:         location on the file system to scan
    :param module_filter:    reference to the module filter function to be used
    :param member_filter:    reference to the member filter function to be used
    :return:                 iterable for tuples of candidate and member
    """
    for mod in __get_modules(path, module_filter):
        try:
            candidate = importlib.import_module(mod)
        except ImportError:
            candidate = None
        if candidate:
            for member in filter(member_filter, dir(candidate)):
                yield (candidate, member)


def __get_tests(path, test_class, module_filter, member_filter):
    """
    Generate test case classes from a given path
    
    :param str path:         location on the file system to scan
    :param test_class:       class the test case classes have to inherit from
    :param module_filter:    reference to the module filter function to be used
    :param member_filter:    reference to the member filter function to be used
    :return:                 iterable of test case classes
    """
    for candidate, member in __get_candidates(path, module_filter, member_filter):
        try:
            if issubclass(getattr(candidate, member), test_class) \
               and getattr(candidate, member).__name__ != test_class.__name__:
                yield getattr(candidate, member)
        except TypeError:
            pass


def __calc_ratio(dividend, divisor):
    """
    Calculate the ratio dividend:divisor
    
    This is a simple wrapper to perform an arithmetic division calculation.
    In case of failure (e. g. divisor = zero), a result of 1 is returned.
    
    :param dividend: dividend number
    :param divisor:  divisor number
    :return:         float
    """
    try:
        result = float(dividend) / float(divisor)
    except ZeroDivisionError:
        result = 1
    return result


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


def __write_stats(results, skipped, failed):
    """
    Print test stats to stdout
    
    :param dict results: test results dictionary
    :param list skipped: list of skipped tests
    :param list failed:  list of failed tests
    """
    total_tests = 0
    total_passed = 0
    total_failed = 0
    total_skipped = 0

    template = "{test: <32}      {passed: >3d}      {failed: >3d}      {skipped: >4d}     {total: >3d}"
    template += "     {ratio: >3.2%}"

    print("\nxobox Unit Test Result Summary:\n\nPython version: {}\n".format(__get_version()))
    print("Test                               Passed   Failed   Skipped   Total    % passed")
    print("================================================================================")
    for key in sorted(results):
        total_tests += results[key][2]
        total_skipped += results[key][1]
        total_failed += results[key][0]
        total_passed = total_tests - total_failed - total_skipped
        ratio = __calc_ratio(results[key][2] - results[key][0] - results[key][1], results[key][2] - results[key][1])
        print(
            template.format(
                test=key,
                passed=results[key][2] - results[key][0] - results[key][1],
                failed=results[key][0],
                skipped=results[key][1],
                total=results[key][2],
                ratio=ratio
            ))
    print("================================================================================")
    ratio = __calc_ratio(total_passed, total_tests - total_skipped)
    print(
        (template+"\n").format(
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


def main():
    """
    xobox test script main function
    """
    # find out if running from an uninstalled version
    # this being the case, insert the appropriate path into PYTHONPATH
    xobox_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    if os.path.isfile(os.path.join(xobox_path, 'xobox', '__init__.py')):
        sys.path.insert(0, xobox_path)

    from xobox.utils import filters

    test_dir = os.path.join(xobox_path, 'tests')

    # look recursively for Python modules in ``test_dir`` and find all classes within those
    # modules derived from :py:class:`~unittest.TestCase`
    # noinspection PyTypeChecker
    test_classes = list(__get_tests(test_dir, unittest.TestCase, filters.files, filters.members))

    return_code = EX_OK

    results = {}
    skipped = []
    failed = []

    # Create a unittest runner and run all detected tests
    runner = unittest.TextTestRunner(stream=open(os.devnull, 'w'))
    for test_class in test_classes:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
        result = runner.run(suite)
        skipped += __get_untested(test_class, result.skipped)
        failed += __get_untested(test_class, result.failures)
        failed += __get_untested(test_class, result.errors)
        results[test_class.__name__] = (len(result.failures) + len(result.errors), len(result.skipped), result.testsRun)
        if result.failures or result.errors:
            return_code = EX_SOFTWARE

    __write_stats(results, skipped, failed)

    return return_code


if __name__ == '__main__':
    sys.exit(main())
else:
    raise RuntimeError("This is an executable file. Do not try to import it!")
    # noinspection PyUnreachableCode
    sys.exit(os.EX_SOFTWARE)
