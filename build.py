import os
from pybuilder.core import use_plugin, init
from pybuilder.vcs import VCSRevision

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('copy_resources')
use_plugin("pypi:pybuilder_aws_plugin")



name = "statusCake_customresource"
default_task = "publish"
license = 'Apache License 2.0'


default_task = ['clean', 'analyze', 'package']

@init
def initialize(project):
    project.build_depends_on("unittest2")
    project.build_depends_on("requests_mock")
    project.build_depends_on('mock')
    project.build_depends_on('coverage')
    project.build_depends_on("moto")

    project.depends_on("boto3")
    project.depends_on('requests')

    project.set_property(
            'bucket_name', os.environ.get('BUCKET_NAME_FOR_UPLOAD'))
    project.set_property(
            'lambda_file_access_control',
            os.environ.get('LAMBDA_FILE_ACCESS_CONTROL'))

    project.set_property('template_files', [('templates', 'cfn-custom-resource.yml')])
    project.set_property('template_file_access_control', os.environ.get('LAMBDA_FILE_ACCESS_CONTROL'))
    project.set_property('template_key_prefix', 'cfn_templates/')


    project.set_property('copy_resources_target', '$dir_dist')
    project.get_property('copy_resources_glob').extend(['setup.cfg'])
    project.set_property('bucket_prefix', '%s_' % name)
    project.set_property('install_dependencies_upgrade', True)


@init(environments='teamcity')
def set_properties_for_teamcity_builds(project):
    project.set_property('teamcity_output', True)


    project.default_task = [
        'clean',
        'install_build_dependencies',
        'publish',
        'package_lambda_code',
        'upload_zip_to_s3',
        'upload_cfn_to_s3',
    ]
    project.set_property('install_dependencies_index_url',
                         os.environ.get('PYPIPROXY_URL'))