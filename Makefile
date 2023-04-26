VERSION ?= $(patsubst v%,%,$(shell git describe))

PROJECT_NAME := materialize Package

PACK             := materialize
ORG              := MaterializeInc
PROJECT          := github.com/${ORG}/pulumi-${PACK}
PROVIDER_PATH    := provider
VERSION_PATH     := ${PROVIDER_PATH}/pkg/version.Version

TFGEN           := pulumi-tfgen-${PACK}
PROVIDER        := pulumi-resource-${PACK}
VERSION         := $(shell pulumictl get version)

WORKING_DIR     := $(shell pwd)

bin/pulumi-resource-materialize: provider/cmd/pulumi-resource-materialize/schema.json provider/resources.go
	cd provider && go build -o ../bin/pulumi-resource-materialize -ldflags "-X github.com/MaterializeInc/pulumi-materialize/provider/pkg/version.Version=${VERSION}" ./cmd/pulumi-resource-materialize

bin/pulumi-tfgen-materialize: provider/cmd/pulumi-tfgen-materialize/*.go provider/go.sum provider/resources.go
	cd provider && go build -o ../bin/pulumi-tfgen-materialize -ldflags "-X github.com/MaterializeInc/pulumi-materialize/provider/pkg/version.Version=${VERSION}" ./cmd/pulumi-tfgen-materialize

provider/cmd/pulumi-resource-materialize/schema.json: bin/pulumi-tfgen-materialize provider/resources.go
	bin/pulumi-tfgen-materialize schema --out ./provider/cmd/pulumi-resource-materialize
	(cd provider && VERSION=$(VERSION) go generate cmd/pulumi-resource-materialize/main.go)

schema: provider/cmd/pulumi-resource-materialize/schema.json

install_plugins::
	[ -x $(shell which pulumi) ] || curl -fsSL https://get.pulumi.com | sh
	pulumi plugin install resource random 4.3.1

tfgen:: install_plugins
	(cd provider && go build -o $(WORKING_DIR)/bin/${TFGEN} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${TFGEN})
	$(WORKING_DIR)/bin/${TFGEN} schema --out provider/cmd/${PROVIDER}
	(cd provider && VERSION=$(VERSION) go generate cmd/${PROVIDER}/main.go)

provider:: tfgen install_plugins # build the provider binary
	(cd provider && go build -o $(WORKING_DIR)/bin/${PROVIDER} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${PROVIDER})

dotnet_sdk:
	rm -rf sdk/dotnet
	bin/pulumi-tfgen-materialize dotnet
	cd sdk/dotnet/ && \
		echo "${VERSION}" >version.txt && \
		dotnet build /p:Version=${VERSION}

python_sdk:
	rm -rf sdk/python
	bin/pulumi-tfgen-materialize python
	cp README.md sdk/python/
	cd sdk/python/ && \
		sed -i.bak -e "s/0\.0\.0/$(VERSION)/g" setup.py && \
		rm setup.py.bak

go_sdk:
	rm -rf sdk/go
	bin/pulumi-tfgen-materialize go

nodejs_sdk:
	rm -rf sdk/nodejs
	bin/pulumi-tfgen-materialize nodejs
	cd sdk/nodejs && \
		sed -i.bak -e "s/\$${VERSION}/$(VERSION)/g" ./package.json

install_sdks:: dotnet_sdk python_sdk go_sdk nodejs_sdk