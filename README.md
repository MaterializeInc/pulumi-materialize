# Pulumi Provider: Materialize

[![Slack Badge](https://img.shields.io/badge/Join%20us%20on%20Slack!-blueviolet?style=flat&logo=slack&link=https://materialize.com/s/chat)](https://materialize.com/s/chat)

A [Pulumi](https://pulumi.com) provider for managing resources in a [Materialize](https://materialize.com/) account.

## Installing

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_materialize
```

## Configuration

The following configuration points are available for the `materialize` provider:

- `materialize:password` (environment: `MZ_PASSWORD`) - Materialize password.
- `materialize:endpoint` (environment: `MZ_ENDPOINT`) - The endpoint for the Frontegg API.
- `materialize:cloud_endpoint` (environment: `MZ_CLOUD_ENDPOINT`) - The endpoint for the Materialize Cloud API.
- `materialize:default_region` (environment: `MZ_DEFAULT_REGION`) - The default region if not specified in the resource.
- `materialize:database` (environment: `MZ_DATABASE`) - Materialize database.

## Testing

To run the tests which will simulate running Pulumi you will need to set the necessary envrionment variables and start the docker compose:

```bash
export MZ_ENDPOINT=http://localhost:3000
export MZ_CLOUD_ENDPOINT=http://localhost:3001
export MZ_PASSWORD=mzp_1b2a3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b
export MZ_SSLMODE=disable

# Start all containers
docker compose -f examples/compose.yaml up -d --build
```

The tests also assume that the SDKs have been built and are present at `sdk/{SDK language}`. These are not committed to git but can be built locally by running `make build_{sdk}`.

You can then run the tests:

```bash
make test
```

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on how to contribute to this provider.

> **Warning**
> The provider is under active development.
