import csv
import datetime
import os
import subprocess

from golem.core import utils


def new_directory_test_case(root_path, project, parents, directory_name):
    parents_joined = os.sep.join(parents)
    errors = []
    if directory_already_exists(root_path, project, 'tests', parents, directory_name):
        errors.append('A directory with that name already exists')

    if not errors:
        utils.create_new_directory(path_list=[root_path, 'projects', project, 'tests',
                                   parents_joined, directory_name], add_init=True)
    return errors


def new_directory_page_object(root_path, project, parents, directory_name):
    parents_joined = os.sep.join(parents)
    errors = []
    if directory_already_exists(root_path, project, 'pages', parents, directory_name):
        errors.append('A directory with that name already exists')
    
    if not errors:
        utils.create_new_directory(path_list=[root_path, 'projects', project, 'pages',
                                   parents_joined, directory_name], add_init=True)
    return errors


def run_test_case(project, test_case_name):
    timestamp = utils.get_timestamp()
    subprocess.Popen(['python', 'golem.py', 'run', project, test_case_name,
                     '--timestamp', timestamp])
    return timestamp


def run_suite(project, suite_name):
    timestamp = utils.get_timestamp()
    subprocess.Popen(['python', 'golem.py', 'run', project, suite_name, '--timestamp', timestamp])
    return timestamp


def get_time_span(task_id):

    path = os.path.join('results', '{0}.csv'.format(task_id))
    if not os.path.isfile(path):
        log_to_file('an error')
        return
    else: 
        with open(path, 'r') as f:
            reader = csv.DictReader(f, delimiter=';') 
            last_row = list(reader)[-1]
            exec_time = string_to_time(last_row['time'])
            time_delta = datetime.datetime.now() - exec_time
            total_seconds = time_delta.total_seconds()
            return total_seconds


def directory_already_exists(root_path, project, root_dir, parents, dir_name):
    parents_joined = os.sep.join(parents)
    directory_path = os.path.join(root_path, 'projects', project, root_dir,
                                  parents_joined, dir_name)
    if os.path.exists(directory_path):
        return True
    else:
        return False


def file_already_exists(root_path, project, root_dir, parents, filename):
    parents_joined = os.sep.join(parents)

    directory_path = os.path.join(
        root_path, 'projects', project, root_dir, parents_joined, filename + '.py')    

    if os.path.isfile(directory_path):
        return True
    else:
        return False


def time_to_string():
    time_format = '%Y-%m-%d-%H-%M-%S-%f'
    return datetime.datetime.now().strftime(time_format)


def string_to_time(time_string):
    return datetime.datetime.strptime(time_string, '%Y-%m-%d-%H-%M-%S-%f')


def get_global_actions():
    global_actions = [
        {
            'name': 'add_step',
            'parameters': [{'name': 'message', 'type': 'value'}]
        },
        {
            'name': 'capture',
            'parameters': [{'name': 'message (optional)', 'type': 'value'}]
        },
        {
            'name': 'click',
            'parameters': [{'name': 'element', 'type': 'element'}]
        },
        {
            'name': 'close',
            'parameters': []
        },
        {
            'name': 'go to',
            'parameters': [{'name': 'url', 'type': 'value'}]
        },
        {
            'name': 'random',
            'parameters': [{'name': 'args', 'type': 'value'}]
        },
        {
            'name': 'select by index',
            'parameters': [{'name': 'from element', 'type': 'element'},
                           {'name': 'index', 'type': 'value'}]
        },
        {
            'name': 'select by text',
            'parameters': [{'name': 'from element', 'type': 'element'},
                           {'name': 'text', 'type': 'value'}]
        },
        {
            'name': 'select by value',
            'parameters': [{'name': 'from element', 'type': 'element'},
                           {'name': 'value', 'type': 'value'}]
        },
        {
            'name': 'send keys',
            'parameters': [{'name': 'element', 'type': 'element'},
                           {'name': 'value', 'type': 'value'}]
        },
        {
            'name': 'store',
            'parameters': [{'name': 'key', 'type': 'value'},
                           {'name': 'value', 'type': 'value'}]
        },
        {
            'name': 'verify exists',
            'parameters': [{'name': 'element', 'type': 'element'}]
        },
        {
            'name': 'verify is enabled',
            'parameters': [{'name': 'element', 'type': 'element'}]
        },
        {
            'name': 'verify is not enabled',
            'parameters': [{'name': 'element', 'type': 'element'}]
        },
        {
            'name': 'verify not exists',
            'parameters': [{'name': 'element', 'type': 'element'}]
        },
        {
            'name': 'verify selected option',
            'parameters': [{'name': 'select', 'type': 'element'},
                           {'name': 'text option', 'type': 'value'}]
        },
        {
            'name': 'verify text',
            'parameters': [{'name': 'text', 'type': 'value'}]
        },
        {
            'name': 'verify text in element',
            'parameters': [{'name': 'element', 'type': 'element'},
                           {'name': 'text', 'type': 'value'}]
        },
        {
            'name': 'wait',
            'parameters': [{'name': 'seconds', 'type': 'value'}]
        },
        {
            'name': 'wait for element visible',
            'parameters': [{'name': 'element', 'type': 'element'},
                           {'name': 'timeout', 'type': 'value'}]
        },
        {
            'name': 'wait for element enabled',
            'parameters': [{'name': 'element', 'type': 'element'},
                           {'name': 'timeout', 'type': 'value'}]
        }
    ]
    return global_actions
