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

- `materialize:host` (environment: `MZ_HOST`) -  Materialize host.
- `materialize:user` (environment: `MZ_USER`) - Materialize user.
- `materialize:password` (environment: `MZ_PASSWORD`) - Materialize password.
- `materialize:port` (environment: `MZ_PORT`) - The Materialize port number to connect to at the server host.
- `materialize:database` (environment: `MZ_DATABASE`) - Materialize database.

## Testing

To run the tests which will simulate running Pulumi you will need to set the necessary envrionment variables and start the docker compose:

```bash
export MZ_HOST=localhost
export MZ_USER=mz_system
export MZ_SSLMODE=disable
export MZ_PORT=6877

# Start all containers
docker-compose -f examples/docker-compose.yml up -d --build
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