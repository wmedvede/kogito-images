#!/usr/bin/python3
#Script responsible to update the tests with 
#Should be run from root directory of the repository
#Sample usage:  python3 scripts/update-tests.py

import sys
sys.dont_write_bytecode = True

import common

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update Maven information in repo from the given artifact url and '
                                                 'version.')
    parser.add_argument('--repo-url', dest='repo_url', help='Defines the url of the repository to setup into the tests')
    parser.add_argument('--replace-jboss-repo', dest='replace_jboss_repo', default=False, action='store_true',
                        help='Enable if repo-url should replace the main JBoss repository')
    parser.add_argument('--examples-uri', dest='examples_uri', help='To update the examples uri for testing')
    parser.add_argument('--examples-ref', dest='examples_ref', help='To update the examples ref for testing')
    parser.add_argument('--artifacts-version', dest='artifacts_version',
                        help='To update the artifacts version for testing')
    parser.add_argument('--ignore-self-signed-cert', dest='ignore_self_signed_cert', default=False,
                        action='store_true',
                        help='If set to true will relax the SSL for user-generated self-signed certificates')
    parser.add_argument('--runtime-image-jvm', dest='runtime_image_jvm',
                        help='To update the runtime jvm image name in behave tests\'s steps')
    parser.add_argument('--runtime-image-native', dest='runtime_image_native',
                        help='To update the runtime native image name in behave tests\'s steps')
    parser.add_argument('--archetype-maven-mirror-url', dest='archetype_maven_mirror_url',
                        help='Maven mirror URL to be used for archetype generation')
    args = parser.parse_args()

    if args.repo_url:
        common.update_maven_repo_in_behave_tests(args.repo_url, args.replace_jboss_repo)
        common.update_maven_repo_in_setup_maven(args.repo_url, args.replace_jboss_repo)

    if args.examples_uri:
        common.update_examples_uri_in_behave_tests(args.examples_uri)
        common.update_examples_uri_in_clone_repo(args.examples_uri)

    if args.examples_ref:
        common.update_examples_ref_in_behave_tests(args.examples_ref)
        common.update_examples_ref_in_clone_repo(args.examples_ref)

    if args.artifacts_version:
        common.update_artifacts_version_in_behave_tests(args.artifacts_version)
    
    if args.ignore_self_signed_cert:
        common.ignore_maven_self_signed_certificate_in_behave_tests()
        common.ignore_maven_self_signed_certificate_in_setup_maven()
    
    if args.runtime_image_jvm:
        common.update_runtime_image_in_behave_tests(args.runtime_image_jvm, 'jvm')
    
    if args.runtime_image_native:
        common.update_runtime_image_in_behave_tests(args.runtime_image_native, 'native')
    
    if args.archetype_maven_mirror_url:
        common.update_maven_mirror_url_in_quarkus_plugin_behave_tests(args.archetype_maven_mirror_url)
