@quay.io/kiegroup/kogito-task-console
Feature: kogito-task-console feature

  Scenario: verify if all labels are correctly set on kogito-task-console image
    Given image is built
    Then the image should contain label maintainer with value kogito <bsig-cloud@redhat.com>
    And the image should contain label io.openshift.s2i.scripts-url with value image:///usr/local/s2i
    And the image should contain label io.openshift.s2i.destination with value /tmp
    And the image should contain label io.openshift.expose-services with value 8080:http
    And the image should contain label io.k8s.description with value Runtime image for Kogito Task Console, manage your Business Process easily.
    And the image should contain label io.k8s.display-name with value Kogito Task Console
    And the image should contain label io.openshift.tags with value kogito,task,task-console

  Scenario: Verify if the debug is correctly enabled and test default http port
    When container is started with env
      | variable     | value |
      | SCRIPT_DEBUG | true  |
    Then container log should contain -Dkogito.dataindex.http.url=http://localhost:8180 -Dquarkus.http.host=0.0.0.0 -Dquarkus.http.port=8080 -jar /home/kogito/bin/quarkus-app/quarkus-run.jar
    And container log should contain Data index url not set, default will be used: http://localhost:8180
    And container log should contain started in
    And container log should not contain Application failed to start

  Scenario: Verify if the debug is correctly enabled and set data-index url
    When container is started with env
      | variable                  | value            |
      | SCRIPT_DEBUG              | true             |
      | KOGITO_DATAINDEX_HTTP_URL | http://test:9090 |
    Then container log should contain -Dkogito.dataindex.http.url=http://test:9090 -Dquarkus.http.host=0.0.0.0 -Dquarkus.http.port=8080 -jar /home/kogito/bin/quarkus-app/quarkus-run.jar
    And container log should not contain Data index url not set, default will be used: http://localhost:8180
    And container log should contain started in
    And container log should not contain Application failed to start
