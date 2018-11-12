#!groovy​

def label = "mypod-${UUID.randomUUID().toString()}"
podTemplate(label: label, imagePullSecrets: ["regsecret"], containers: [
    containerTemplate(name: 'docker', image: 'docker', ttyEnabled: true, command: 'cat',
        envVars: [containerEnvVar(key: 'DOCKER_CONFIG', value: '/tmp/'),])],
        volumes: [secretVolume(secretName: 'jenkins-docker-secret', mountPath: '/var/run/secrets/registry-account/'),
        hostPathVolume(hostPath: '/var/run/docker.sock', mountPath: '/var/run/docker.sock')
  ]) {
    node(label) {

         def app

        def DOCKER_HUB_ACCOUNT = 'docker.env.liquidvu.com'
        def DOCKER_IMAGE_NAME = 'liquid-uswg-nginx-jenkins'
        def BUILD_NUM = new Date().format("'v'yyyyMMddHHmmssSSS")

        stage('Clone repository') {
            /* Let's make sure we have the repository cloned to our workspace */
            checkout scm
        }

        container('docker') {
                stage('Docker Build & Push Current & Latest Versions') {
                    sh ("""
                    #!/bin/bash
                    set +x
                    DOCKER_USER=`cat /var/run/secrets/registry-account/username`
                    DOCKER_PASSWORD=`cat /var/run/secrets/registry-account/password`
                    docker login -u=\${DOCKER_USER} -p=\${DOCKER_PASSWORD} ${DOCKER_HUB_ACCOUNT}
                    set -x
                    docker build -t ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7 -f python2.7/Dockerfile --build-arg build_num=${BUILD_NUM} ./python2.7/
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7
                    docker tag ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7 ${DOCKER_HUB_ACCOUNT}/python2.7
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7
                    docker build -t ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7-alpine3.7 -f python2.7-alpine3.7/Dockerfile --build-arg build_num=${BUILD_NUM} ./python2.7-alpine3.7/
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7-alpine3.7
                    docker tag ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7-alpine3.7 ${DOCKER_HUB_ACCOUNT}/python2.7-alpine3.7
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7-alpine3.7
                    docker build -t ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7-alpine3.8 -f python2.7-alpine3.8/Dockerfile --build-arg build_num=${BUILD_NUM} ./python2.7-alpine3.8/
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7-alpine3.8
                    docker tag ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7-alpine3.8 ${DOCKER_HUB_ACCOUNT}/python2.7-alpine3.8
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python2.7-alpine3.8
                    docker build -t ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.5 -f python3.5/Dockerfile --build-arg build_num=${BUILD_NUM} ./python3.5/
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.5
                    docker tag ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.5 ${DOCKER_HUB_ACCOUNT}/python3.5
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.5
                    docker build -t ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6 -f python3.6/Dockerfile --build-arg build_num=${BUILD_NUM} ./python3.6/
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6
                    docker tag ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6 ${DOCKER_HUB_ACCOUNT}/python3.6
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6
                    docker build -t ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6-alpine3.7 -f python3.6-alpine3.7/Dockerfile --build-arg build_num=${BUILD_NUM} ./python3.6-alpine3.7/
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6-alpine3.7
                    docker tag ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6-alpine3.7 ${DOCKER_HUB_ACCOUNT}/python3.6-alpine3.7
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6-alpine3.7
                    docker build -t ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6-alpine3.8 -f python3.6-alpine3.8/Dockerfile --build-arg build_num=${BUILD_NUM} ./python3.6-alpine3.8/
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6-alpine3.8
                    docker tag ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6-alpine3.8 ${DOCKER_HUB_ACCOUNT}/python3.6-alpine3.8
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.6-alpine3.8
                    docker build -t ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7 -f python3.7/Dockerfile --build-arg build_num=${BUILD_NUM} ./python3.7/
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7
                    docker tag ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7 ${DOCKER_HUB_ACCOUNT}/python3.7
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7
                    docker build -t ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7-alpine3.7 -f python3.7-alpine3.7/Dockerfile --build-arg build_num=${BUILD_NUM} ./python3.7-alpine3.7/
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7-alpine3.7
                    docker tag ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7-alpine3.7 ${DOCKER_HUB_ACCOUNT}/python3.7-alpine3.7
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7-alpine3.7
                    docker build -t ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7-alpine3.8 -f python3.7-alpine3.8/Dockerfile --build-arg build_num=${BUILD_NUM} ./python3.7-alpine3.8/
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7-alpine3.8
                    docker tag ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7-alpine3.8 ${DOCKER_HUB_ACCOUNT}/python3.7-alpine3.8
                    docker push ${DOCKER_HUB_ACCOUNT}/${DOCKER_IMAGE_NAME}:python3.7-alpine3.8
                    """)
                }
        }

    }
}
