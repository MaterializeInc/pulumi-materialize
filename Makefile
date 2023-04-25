VERSION ?= $(patsubst v%,%,$(shell git describe))

bin/pulumi-resource-materialize: provider/cmd/pulumi-resource-materialize/schema.json provider/resources.go
	cd provider && go build -o ../bin/pulumi-resource-materialize -ldflags "-X github.com/MaterializeInc/pulumi-materialize/provider/pkg/version.Version=${VERSION}" ./cmd/pulumi-resource-materialize

bin/pulumi-tfgen-materialize: provider/cmd/pulumi-tfgen-materialize/*.go provider/go.sum provider/resources.go
	cd provider && go build -o ../bin/pulumi-tfgen-materialize -ldflags "-X github.com/MaterializeInc/pulumi-materialize/provider/pkg/version.Version=${VERSION}" ./cmd/pulumi-tfgen-materialize

provider/cmd/pulumi-resource-materialize/schema.json: bin/pulumi-tfgen-materialize provider/resources.go
	bin/pulumi-tfgen-materialize schema --out ./provider/cmd/pulumi-resource-materialize
	(cd provider && VERSION=$(VERSION) go generate cmd/pulumi-resource-materialize/main.go)

schema: provider/cmd/pulumi-resource-materialize/schema.json

dotnet-sdk: bin/pulumi-tfgen-materialize provider/cmd/pulumi-resource-materialize/schema.json
	rm -rf sdk/dotnet
	bin/pulumi-tfgen-materialize dotnet
	cd sdk/dotnet/ && \
		echo "${VERSION}" >version.txt && \
		dotnet build /p:Version=${VERSION}

python-sdk: bin/pulumi-tfgen-materialize provider/cmd/pulumi-resource-materialize/schema.json
	rm -rf sdk/python
	bin/pulumi-tfgen-materialize $(VERSION) python
	cp README.md sdk/python/
	cd sdk/python/ && \
		sed -i.bak -e "s/0\.0\.0/$(VERSION)/g" setup.py && \
		rm setup.py.bak

go-sdk: bin/pulumi-tfgen-materialize provider/cmd/pulumi-resource-materialize/schema.json
	rm -rf sdk/go
	bin/pulumi-tfgen-materialize go

nodejs-sdk: bin/pulumi-tfgen-materialize provider/cmd/pulumi-resource-materialize/schema.json
	rm -rf sdk/nodejs
	bin/pulumi-tfgen-materialize nodejs
	cd sdk/nodejs && \
		sed -i.bak -e "s/\$${VERSION}/$(VERSION)/g" ./package.json

install-sdks:: dotnet-sdk python-sdk go-sdk nodejs-sdk